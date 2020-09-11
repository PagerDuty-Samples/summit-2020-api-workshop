# Services

## Create a Service

We want to have a Service which Incidents and Alerts will be trigger on.

Let's use the [Create Service](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1services/post) endpoint to create a Service.

```python
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
```{{copy}}


## Get or Create

Now that we've created the service we are going to want to make sure that we don't create a new service every single time.

Use the [List Services](https://developer.pagerduty.com/api-reference/reference/REST/openapiv3.json/paths/~1services/get) endpoint to list the services.

Use a simple check on the number of services to check if one already exists.

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
