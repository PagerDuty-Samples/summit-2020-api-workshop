# Send Tweets to the Global Events API

The final part of our startup file will be to send any tweets that we get to the Global Events endpoint.

We will need to use the [Events API](https://github.com/PagerDuty/pdpyras#events-api-usage) for this.

Fill out the `send_twitter_statuses_to_events_API()` function in `startup.py`

## Completed Code

```python
session = EventsAPISession(integration_key)

for status in statuses:
    print("Triggering on Events API")
    response = session.trigger(
        f"Matching tweet from user @{status['user']['screen_name']}",
        'twitter.com',
        severity='info',
        custom_details=status)
```{{copy}}

## Run the server again

`flask run`{{execute}}

### Need a shortcut

You can use this command to copy over completed code and skip this step.

`cp ../completed/startup-step9.py startup.py`{{execute}}
