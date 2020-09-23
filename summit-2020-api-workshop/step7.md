# Events Integration

We'll be using the Global Events API to send our Tweets into PagerDuty.

## Get the Routing Key

The routing key (aka integration key) is used to identify the ruleset that we want to use.

Get the Routing Key from the Default Ruleset using the [Rulesets API](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1rulesets/get). We should only have 1 ruleset with 1 routing key.

Fill out the `get_or_create_event_ruleset_id_and_routing_key()` function in `startup.py`.

```python
def get_or_create_event_ruleset_id_and_routing_key():
    print("Get Events Integration Key.")
    try:
        rulesets = PagerDutyAPISession.rget(
            f'/rulesets',
            params={'query': 'PagerDuty Summit Ruleset'}
        )
        if len(rulesets) == 1:
            print("Get existing Ruleset")
            return rulesets[0]['id'], rulesets[0]['routing_keys'][0]
        elif len(rulesets) == 0:
            print("Creating new Ruleset")
            ruleset = PagerDutyAPISession.rpost(
                f'/rulesets',
                json={
                    'name': 'PagerDuty Summit Ruleset'
                }
            )
            return ruleset['id'], rulesets[0]['routing_keys'][0]
        else:
            raise Exception(f"Found unexpected global event rulesets than expected. Found {len(rulesets)}")
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)
```{{copy}}


## Run the server again

`flask run`{{execute}}

### You should see: an integration key

    Starting Up!
    Get or create default Escalation Policy
    Found 1 escalation policy: PXXXXXX
    Got an Escalation Policy Id: PXXXXXX
    Get or Create Service.
    Found already existing service.
    Got a Service Id: PXXXXXX
    Get Events Integration Key.
    Got an Integration Key: RXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    Create Event Rule.
    ----
      File "/root/app/skeleton/server.py", line 8, in create_app
    NotImplementedError caught! exiting...

### Need a shortcut

You can use this command to copy over completed code and skip this step.

`cp ../completed/completed-startup-step7.py startup.py && flask run`{{execute}}
