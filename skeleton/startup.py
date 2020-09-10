from pdpyras import APISession, PDClientError, EventsAPISession
from os import environ as ENV

import twitter


SERVICE_NAME="PDSummit Twitter Service"
PagerDutyAPISession = APISession(ENV.get('PAGERDUTY_REST_API_KEY'))

def startup():
    print("Starting Up!")
    escalation_policy_id = get_default_escalation_policy_id()
    service_id = create_or_get_service_id(escalation_policy_id)
    print (f"Service ID: {service_id}")
    ruleset_id, integration_key = get_or_create_events_v2_integration_key(service_id)
    print (f"Integration Key: {integration_key}")
    create_event_rule(ruleset_id, service_id)

    # Loop until the program is exited!
    while True:
        twitter_statuses = twitter.query_twitter()
        send_twitter_statuses_to_events_API(integration_key, twitter_statuses)
        time.sleep(15)

def get_default_escalation_policy_id():
    print("Get default Escalation Policy")
    try:
        raise NotImplementedError
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def create_or_get_service_id(escalation_policy_id):
    print("Create or get Services.")
    try:
        raise NotImplementedError
    except PDClientError as e:
        print(e.msg)

def get_or_create_events_v2_integration_key(service_id):
    print ("creating events integration")
    try:
        raise NotImplementedError
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def send_twitter_statuses_to_events_API(integration_key, statuses):
    print("Triggering on Events API")
    raise NotImplementedError

def create_event_rule(ruleset_id, service_id):
    try:
        raise NotImplementedError
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)
