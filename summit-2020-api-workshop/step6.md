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
services = PagerDutyAPISession.rget(
    '/services',
    params={'query': SERVICE_NAME}
)
service_id = None
if len(services) == 1:
    print ("Found already existing service.")
    service_id = services[0]['id']
elif len(services) == 0:
    print ('Creating service.')
    new_service = PagerDutyAPISession.rpost(
        '/services',
        json={
            'name': SERVICE_NAME,
            'type': 'service',
            'description': 'PagerDuty Summit Twitter Matches',
            "escalation_policy": {
                "id": escalation_policy_id,
                "type": "escalation_policy_reference"
            },
            "alert_creation": "create_alerts_and_incidents"
        })
    service_id = new_service['id']
else:
    raise Exception(f"Found more services than expected. Found {len(services)}")
return service_id
```{{copy}}

## Run the server again

`flask run`{{execute}}

### Need a shortcut

You can use this command to copy over completed code and skip this step.

`cp ../completed/startup-step6.py startup.py && flask run`{{execute}}
