Next let's put in our API keys.

## Setup the .env file

`cp .env-sample .env`{{execute}}

## Enter your keys into the .env file.

Open up the `.env` file for editing

**Click here to open** -> `./app/skeleton/.env`{{open}}

## 1. (Required) Enter in your PagerDuty REST API Key

1. On your PagerDuty Developer account navigate to the main dashboard by clicking "Return to PagerDuty Account."
1. In the top navigation bar click "Configuration."
1. In the Configuration dropdown click "API Access."
1. On the "API Access Keys" page click the green "Create New API Key" button.
1. Enter a short description. Suggested: `Summit Twitter App."
1. Copy the highlighted API Key. It will be a 20 character alphanumeric string.
1. Back in the editor paste in your copied API Key inbetween the quotes of the key `PAGERDUTY_REST_API_KEY` in the `.env` file.

For example: `PAGERDUTY_REST_API_KEY="my-key-goes-here"`

## 2. (Required) Enter in your PagerDuty Events Routing Key

1. On your PagerDuty Developer account navigate to the main dashboard by clicking "Return to PagerDuty Account."
1. In the top navigation bar click "Configuration."
1. In the Configuration dropdown click "Event Rules."
1. On the "Rulesets" page click the "Default Global Ruleset" ruleset.
1. Copy the Integration Key, a 32 character alphanumeric string.
1. Back in the editor paste in the copied Integration Key inbetween the quotes of the key `PAGERDUTY_EVENTS_ROUTING_KEY`.in the `.env` file.

For example: `PAGERDUTY_EVENTS_ROUTING_KEY="my-key-goes-here"`

## 3. (Optional, recommended) Enter in your Twitter Bearer Token

1. Access your Twitter Developer Account by navigating to the [Dashboard.](https://developer.twitter.com/en/portal/dashboard) https://developer.twitter.com/en/portal/dashboard
1. Click "Projects & Apps" in the left sidebar.
1. Click "Overview" in the expanded options in the left sidebar.
1. Create a new "App" by clicking the blue outlined button "Create App" at the bottom of the "Overview" page.
1. Enter a helpful name. Suggested: "PagerDuty Summit App."
1. Click "Complete."
1. Copy the "Bearer token", a 116 length string.
1. Back in the editor paste in the copied Bearer Token inbetween the quotes of the key `TWITTER_BEARER_TOKEN`.in the `.env` file.

For example: `TWITTER_BEARER_TOKEN="my-key-goes-here"`
