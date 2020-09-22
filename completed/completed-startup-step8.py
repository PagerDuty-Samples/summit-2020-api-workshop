from pdpyras import APISession, PDClientError, EventsAPISession
from os import environ as ENV

import twitter
import time


SERVICE_NAME="PDSummit Twitter Service"
PagerDutyAPISession = APISession(ENV.get('PAGERDUTY_REST_API_KEY'))

def startup():
    print("Starting Up!")
    escalation_policy_id = get_or_create_default_escalation_policy_id()
    print(f"Got an Escalation Policy Id: {escalation_policy_id}")
    service_id = get_or_create_service_id(escalation_policy_id)
    print(f"Got a Service Id: {service_id}")
    ruleset_id, integration_key = get_events_v2_integration_key()
    print(f"Got an Integration Key: {integration_key}")
    create_event_rule(ruleset_id, service_id)
    print(f"Event Rule Created!")

    # Loop until the program is exited!
    while True:
        twitter_statuses = twitter.query_twitter()
        print(f"Twitter returned {len(twitter_statuses)} tweets.")
        send_twitter_statuses_to_events_API(integration_key, twitter_statuses)
        time.sleep(15)


def get_or_create_default_escalation_policy_id():
    print("Get or create default Escalation Policy")
    try:
        escalation_policies = PagerDutyAPISession.rget(
            '/escalation_policies',
            params={'query': 'Default'})
        if len(escalation_policies) == 1:
            default_escalation_policy_id = escalation_policies[0]['id']
            print(f"Found 1 escalation policy: {default_escalation_policy_id}")
            return default_escalation_policy_id
        elif len(escalation_policies) == 0:
            print("No Escalation Policies found, creating one.")
            users = PagerDutyAPISession.rget(
                '/users'
            )
            new_escalation_policy = PagerDutyAPISession.rpost(
                '/escalation_policies',
                json={
                    "type": "escalation_policy",
                    "name": "Default Escalation Policy",
                    "escalation_rules": [
                        {
                            "escalation_delay_in_minutes": 5,
                            "targets": [
                                {
                                    "id": users[0]['id'],
                                    "type": "user_reference"
                                }
                            ]
                        }
                    ]
                }
            )
            return new_escalation_policy['id']
        else:
            raise Exception(f"Found unexpected number of escalation_policies {len(escalation_policy)}")
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def get_or_create_service_id(escalation_policy_id):
    print("Get or Create Service.")
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
                    'description': 'PagerDuty Summit Twitter Matches',
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
        print(e.response.text)

def get_events_v2_integration_key():
    print("Get Events Integration Key.")
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


def create_event_rule(ruleset_id, service_id):
    print("Create Event Rule.")
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

def send_twitter_statuses_to_events_API(integration_key, statuses):
    print("Send Twitter Statuses to Events API.")
    raise NotImplementedError
