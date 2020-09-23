# Event Rules

We will need to create an Event Rule to filter our tweets -- otherwise our service will be too noisey!

Let's create an event rule that escalates the event to an Incident if the tweet contains a mention of PagerDuty CEO @jenntejada.

We can use the Rulesets API for this again, this time we will use the [Rule Creation endpoint](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1rulesets~1%7Bid%7D~1rules/post).

Fill out the `create_event_rule()` function in `startup.py`.

## Event Rule JSON

```json
{
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
```{{copy}}


## Completed Code

```python
def create_event_rule(ruleset_id, service_id):
    print("Create Event Rule.")
    try:
        events_rules = PagerDutyAPISession.rget(
            f"/rulesets/{ruleset_id}/rules"
        )
        if (len(events_rules)) == 2:
            print("Event Rule already exists, moving on.")
        else:
            print("Event Rule does not exist, creating.")
            event_rule = PagerDutyAPISession.rpost(
                f"/rulesets/{ruleset_id}/rules",
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
```{{copy}}

## Run the server again

`flask run`{{execute}}

### You should see: 1 or more tweets from Twitter

    Starting Up!
    Get or create Escalation Policy
    Found 1 escalation policy: P8H24LX
    Got an Escalation Policy Id: P8H24LX
    Get or Create Service.
    Found already existing service.
    Got a Service Id: PJE2JT3
    Get Events Integration Key.
    Got an Integration Key: R013E1ZC6XJJ21QDEZ7M4C1R30EDPG0C
    Create Event Rule.
    Event Rule does not exist, creating.
    Event Rule Created!
    Querying Twitter...
    Twitter returned 1 tweets.
    Send Twitter Statuses to Events API.
    ----
      File "/root/app/skeleton/server.py", line 8, in create_app
    NotImplementedError caught! exiting...

### Need a shortcut

You can use this command to copy over completed code and skip this step.

`cp ../completed/completed-startup-step8.py startup.py && flask run`{{execute}}

**Close the file editor, and click here to refresh it** -> `./app/skeleton/startup.py`{{open}}
