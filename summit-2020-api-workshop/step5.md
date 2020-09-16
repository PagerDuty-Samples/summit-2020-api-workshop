# Escalation Policy

To setup our account we're going to need a few things:
 - Service: this represents an entity that you would like to monitor. In this case, it's the Twitter feed.
 - Escalation Policy: this determines who will be alerted if the service has an incident.
 - Event Rule: these allow you to set up simple yet powerful rules for interpreting the events sent to PagerDuty, and whether incidents should be created from them or not.

## Service requires an Escalation Policy

As you can see in the ["Create Service" endpoint](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1services/post), the `escalation_policy` object is required. So we are going to need to first create or get an Escalation Policy.

## Get the Default Escalation Policy

PagerDuty accounts come with a Default Escalation Policy, so let's use that for our first service.

We can list the existing Escalation Policies via the["List Escalation Policies" endpoint](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1escalation_policies/get).

## Open `startup.py`

We'll be doing most of our work in this file. When our Flask server starts up it enter this file through the `startup()` function.

**Click here to open** -> `./app/skeleton/startup.py`{{open}}

## Using PDPyras

[PDPyras](https://github.com/PagerDuty/pdpyras) is a lightweight Python client for our API.

The skeleton already instantiates a Session in `startup.py:8`.

## Get Default Escalation Policy

Paste the below python code into the `get_default_escalation_policy_id()` function definition in `startup.py:28`

```python
escalation_policy = PagerDutyAPISession.rget(
    '/escalation_policies',
    params={'query': 'Default'})
if len(escalation_policy) == 1:
    default_escalation_policy_id = escalation_policy[0]['id']
    print(f"Found 1 escalation policy: {default_escalation_policy_id}")
    return default_escalation_policy_id
else:
    raise
```{{copy}}

This code uses the `rget` PDPyras method to get information from the List Escalation Policies endpoint.

## Run the server again

`flask run`{{execute}}
