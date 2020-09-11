# Event Rules

We will need to create an Event Rule to filter our tweets.

Let's create an event rule that escalates the event to an Incident if the tweet contains a mention of PagerDuty CEO @jenntejada.

We can use the Rulesets API for this again, this time we will use the [Rule Creation endpoint.](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1rulesets~1%7Bid%7D~1rules/post)

Fill out the `create_event_rule()` function in `startup.py`.

## Completed Code

```python
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
```{copy}
