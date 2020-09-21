# Events Integration

We'll be using the Global Events API to send our Tweets into PagerDuty.

## Get the Routing Key

The routing key (aka integration key) is used to identify the ruleset that we want to use.

Get the Routing Key from the Default Ruleset using the [Rulesets API](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1rulesets/get). We should only have 1 ruleset with 1 routing key.

Fill out the `get_events_v2_integration_key()` function in `startup.py`.

```python
rulesets = PagerDutyAPISession.rget(
    f'/rulesets'
)
if len(rulesets) == 1:
    return rulesets[0]['id'], rulesets[0]['routing_keys'][0]
else:
    raise Exception(f"Found more global event rulesets than expected. Found {len(rulesets)}")
```{{copy}}


## Run the server again

`flask run`{{execute}}


### Need a shortcut

You can use this command to copy over completed code and skip this step.

`cp ../completed/startup-step7.py startup.py && flask run`{{execute}}
