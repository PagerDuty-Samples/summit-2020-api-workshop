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
    ruleset_id, integration_key = get_or_create_event_ruleset_id_and_routing_key()
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
            raise Exception(f"Found unexpected number of escalation_policies {len(escalation_policies)}")
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def get_or_create_service_id(escalation_policy_id):
    print("Create or get Services.")
    try:
        raise NotImplementedError("get_or_create_service_id")
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def get_or_create_event_ruleset_id_and_routing_key():
    print("Get Events Integration Key.")
    try:
        raise NotImplementedError("get_or_create_event_ruleset_id_and_routing_key")
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def create_event_rule(ruleset_id, service_id):
    print("Create Event Rule.")
    try:
        raise NotImplementedError("create_event_rule")
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def send_twitter_statuses_to_events_API(integration_key, statuses):
    print("Send Twitter Statuses to Events API.")
    raise NotImplementedError("send_twitter_statuses_to_events_API")
