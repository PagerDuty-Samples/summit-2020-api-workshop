# Escalation Policy

To setup our account we're going to need a few things:
 - Service: this represents an entity that you would like to monitor. In this case, it's the Twitter feed.
 - Escalation Policy: this determines who will be alerted if the service has an incident.
 - Event Rule: these allow you to set up simple yet powerful rules for interpreting the events sent to PagerDuty, and whether incidents should be created from them or not.

## Service requires an Escalation Policy

As you can see in our documentation for the ["Create Service" endpoint](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1services/post), the `escalation_policy` object is required. So we are going to need to first create or get an Escalation Policy.

PagerDuty Developer Accounts don't come with a default escalation policy, so you'll first need to call the ["Create Escalation Policy" endpoint](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1escalation_policies/post) to create one.

We can also list the existing Escalation Policies via the["List Escalation Policies" endpoint](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1escalation_policies/get).

## Completed Code

```python
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
```{{copy}}

This code uses the `rget` PDPyras method to get information from the List Escalation Policies endpoint.

## Run the server again

`flask run`{{execute}}

### You should see: an escalation policy

    Starting Up!
    Get or create default Escalation Policy
    Found 1 escalation policy: PXXXXXX
    Got an Escalation Policy Id: PXXXXXX
    Create or get Services.
    ----
      File "/root/app/skeleton/server.py", line 8, in create_app
    NotImplementedError caught! exiting...

### Need a shortcut

You can use this command to copy over completed code and skip this step.

`cp ../completed/completed-startup-step5.py startup.py && flask run`{{execute}}
