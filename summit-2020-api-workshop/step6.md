# Services

## Create a Service

We want to have a Service where we can trigger Incidents and Alerts.

Let's use the [Create Service](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1services/post) endpoint to create a Service.

## Get or Create

Now that we've created the service, we are going to want to make sure that we don't create a new service every single time.

Use the [List Services](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1services/get) endpoint to list the services.

Use a simple check on the number of services to determine if one already exists.

## Finished Code

```python
def get_or_create_service_id(escalation_policy_id):
    print("Get or Create Service.")
    try:
        services = PagerDutyAPISession.rget(
            "/services",
            params={"query": "My Service"}
        )
        service_id = None
        if len(services) == 1:
            print ("Found already existing service.")
            service_id = services[0]["id"]
        elif len(services) == 0:
            print ("Creating service.")
            new_service = PagerDutyAPISession.rpost(
                "/services",
                json={
                    "name": "My Service",
                    "type": "service",
                    "description": "PagerDuty Summit Twitter Matches",
                    "escalation_policy": {
                        "id": escalation_policy_id,
                        "type": "escalation_policy_reference"
                    },
                    "alert_creation": "create_alerts_and_incidents"
                })
            service_id = new_service["id"]
        else:
            raise Exception(f"Found unexpected number of services. Found {len(services)}")
        return service_id
    except PDClientError as e:
        print(e.msg)
        print(e.response.text)
```{{copy}}

## Run the server again

`flask run`{{execute}}

## You should see: a service

```
Starting Up!
Get or create Escalation Policy
Found 1 escalation policy: PXXXXXX
Got an Escalation Policy Id: PXXXXXX
Get or Create Service.
Creating service.
Got a Service Id: PXXXXXX
Get Events Integration Key.
----
  File "/root/app/skeleton/startup.py", line XXX, in get_or_create_event_ruleset_id_and_routing_key
NotImplementedError caught! Looks like you need to implement: get_or_create_event_ruleset_id_and_routing_key
```

### Need a shortcut

You can use this command to copy over completed code and skip this step.

`cp ../completed/completed-startup-step6.py startup.py && flask run`{{execute}}

**Close the file editor, and click here to refresh it** -> `./app/skeleton/startup.py`{{open}}
