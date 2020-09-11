from pdpyras import APISession, PDClientError, EventsAPISession
from os import environ as ENV

import twitter
import time


SERVICE_NAME="PDSummit Twitter Service"
PagerDutyAPISession = APISession(ENV.get('PAGERDUTY_REST_API_KEY'))

def startup():
    print("Starting Up!")
    escalation_policy_id = get_default_escalation_policy_id()
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

def get_default_escalation_policy_id():
    print("Get default Escalation Policy")
    try:
        raise NotImplementedError
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def get_or_create_service_id(escalation_policy_id):
    print("Create or get Services.")
    try:
        raise NotImplementedError
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def get_events_v2_integration_key():
    print("Get Events Integration Key.")
    try:
        raise NotImplementedError
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def create_event_rule(ruleset_id, service_id):
    print("Create Event Rule.")
    try:
        raise NotImplementedError
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)

def send_twitter_statuses_to_events_API(integration_key, statuses):
    print("Send Twitter Statuses to Events API.")
    raise NotImplementedError
