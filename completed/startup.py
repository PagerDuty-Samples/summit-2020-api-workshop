from pdpyras import APISession, PDClientError, EventsAPISession
from os import environ as ENV

import twitter


SERVICE_NAME="PDSummit Twitter Service"
PagerDutyAPISession = APISession(ENV.get('PAGERDUTY_REST_API_KEY'))

def startup():
    print("doing startup things.")
    escalation_policy_id = get_default_escalation_policy_id()
    service_id = get_or_create_service_id(escalation_policy_id)
    ruleset_id, integration_key = get_or_create_events_v2_integration_key(service_id)
    create_event_rule(ruleset_id, service_id)

    # Loop until the program is exited!
    while True:
        twitter_statuses = twitter.query_twitter()
        send_twitter_statuses_to_events_API(integration_key, twitter_statuses)
        time.sleep(15)

def get_default_escalation_policy_id():
    print("Get default Escalation Policy")
    try:
        escalation_policy = PagerDutyAPISession.rget(
            '/escalation_policies',
            params={'query': 'Default'})
        if len(escalation_policy) == 1:
            default_escalation_policy_id = escalation_policy[0]['id']
            print(f"Found 1 escalation policy: {default_escalation_policy_id}")
            return default_escalation_policy_id
        else:
            raise Exception(f"Found unexpected number of escalation_policies {len(escalation_policy)}")
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def get_or_create_service_id(escalation_policy_id):
    print("Get or Create Service.")
    escalation_policy_id = get_default_escalation_policy_id()
    try:
        services = PagerDutyAPISession.rget(
            '/services',
            params={'query': SERVICE_NAME}
        )
        service_id = None
        if len(services) == 1:
            print ("Found already existing service.")
            service_id = services[0]['id']
        elif len(services) == 0:
            print ('Creating service.')
            new_service = PagerDutyAPISession.rpost(
                '/services',
                json={
                    'name': SERVICE_NAME,
                    'type': 'service',
                    'description': 'hey',
                    "escalation_policy": {
                        "id": escalation_policy_id,
                        "type": "escalation_policy_reference"
                    },
                    "alert_creation": "create_alerts_and_incidents"
                })
            service_id = new_service['id']
        else:
            raise Exception(f"Found more services than expected. Found {len(services)}")
        return service_id
    except PDClientError as e:
        print(e.msg)

def get_or_create_events_v2_integration_key(service_id):
    print("Get or Create Events Integration Key.")
    try:
        rulesets = PagerDutyAPISession.rget(
            f'/rulesets'
        )
        if len(rulesets) == 1:
            return rulesets[0]['id'], rulesets[0]['routing_keys'][0]
        else:
            raise Exception(f"Found more global event rulesets than expected. Found {len(rulesets)}")
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def send_twitter_statuses_to_events_API(integration_key, statuses):
    session = EventsAPISession(integration_key)

    for status in statuses:
        print("Triggering on Events API")
        response = session.trigger(
            f"Matching tweet from user @{status['user']['screen_name']}",
            'twitter.com',
            severity='info',
            custom_details=status)

def create_event_rule(ruleset_id, service_id):
    try:
        events_rules = PagerDutyAPISession.rget(
            f'/rulesets/{ruleset_id}/rules'
        )
        if (len(events_rules)) == 2:
            print("Event Rule already exists, moving on.")
            return
        print("Event Rule doesn't exist, creating.")
        event_rule = PagerDutyAPISession.rpost(
            f'/rulesets/{ruleset_id}/rules',
            json={
                "rule": {
                    "conditions": {
                        "operator": "or",
                        "subconditions": [
                            {
                                "parameters": {
                                    "value": "jenntejada",
                                    "path": "payload.custom_details.entities.user_mentions"
                                },
                                "operator": "contains"
                            }
                        ],
                    },
                    "actions": {
                        "severity": {
                            "value": "critical"
                        },
                        "priority": {
                            "value": "PD6DVC6"
                        },
                        "route": {
                            "value": service_id
                        }
                    }
                }
            }
        )
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)
