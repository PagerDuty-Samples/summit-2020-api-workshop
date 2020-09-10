from pdpyras import APISession, PDClientError, EventsAPISession
from os import environ as ENV

import twitter


SERVICE_NAME="PDSummit Twitter Service"
PagerDutyAPISession = APISession(ENV.get('PAGERDUTY_REST_API_KEY'))

def startup():
    print("doing startup things.")
    service_id = create_or_get_service_id()
    print (f"Service ID: {service_id}")
    ruleset_id, integration_key = get_or_create_events_v2_integration_key(service_id)
    print (f"Integration Key: {integration_key}")
    create_event_rule(ruleset_id, service_id)

    # Loop until the program is exited!
    while True:
        twitter_statuses = twitter.query_twitter()
        send_twitter_statuses_to_events_API(integration_key, twitter_statuses)
        time.sleep(15)


def create_or_get_service_id():
    print("Create or get Services.")
    escalation_policy_id = get_default_escalation_policy_id()
    try:
        service = PagerDutyAPISession.rget(
            '/services',
            params={'query': SERVICE_NAME}
        )
        if len(service) == 1:
            print ("Service already exists.")
            return service[0]['id']
        elif len(service) == 0:
            print ('Create service.')
            #create service
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
            return new_service['id']
    except PDClientError as e:
        print(e.msg)

def get_default_escalation_policy_id():
    print("Get default Escalation Policy")
    try:
        escalation_policy = PagerDutyAPISession.rget(
            '/escalation_policies',
            params={'query': 'Default'})
        if len(escalation_policy) == 1:
            return escalation_policy[0]['id']
        else:
            raise Exception
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def get_or_create_events_v2_integration_key(service_id):
    print ("creating events integration")
    try:
        rulesets = PagerDutyAPISession.rget(
            f'/rulesets'
        )
        if len(rulesets) == 1:
            return rulesets[0]['id'], rulesets[0]['routing_keys'][0]
        else:
            print("Found more global event rulesets than expected!")
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
