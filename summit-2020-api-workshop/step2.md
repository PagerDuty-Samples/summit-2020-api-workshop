# Setup Credentials

Before we get started coding, we need to enter some API Keys and Credentials.

## Setup the .env file

We will be storing our credentials in a file which will be automatically loaded by our code.

We have created a sample of this file so let's first make a copy of it.

Make a copy of the file and remove 'sample' from the name.

`cp .env-sample .env`{{execute}}

## Enter your keys into the .env file.

Open up the `.env` file for editing.

**Click here to open** -> `./app/skeleton/.env`{{open}}

### 1. (Required) Enter in your PagerDuty REST API Key

First we will get our PagerDuty REST API Key, we will need this to read and write information to our PagerDuty account.

If you missed the pre-requisite to sign up for a Developer account, you can quickly [sign up here](https://developer.pagerduty.com/sign-up/).

1. Open your PagerDuty Developer account.
1. On your PagerDuty Developer account navigate to the main dashboard by clicking "Return to PagerDuty Account."
1. In the top navigation bar click "Configuration."
1. In the Configuration dropdown click "API Access."
1. On the "API Access Keys" page click the green "Create New API Key" button.
1. Enter a short description. Suggested: `Summit Twitter App."
1. Copy the highlighted API Key. It will be a 20 character alphanumeric string.
1. Back in the editor paste in your copied API Key inbetween the quotes of the key `PAGERDUTY_REST_API_KEY` in the `.env` file.

For example: `PAGERDUTY_REST_API_KEY="my-key-goes-here"`

### 2. (Optional, recommended) Enter in your Twitter Bearer Token

Second we will get the Bearer Token for our Twitter Developer account.

If you missed this pre-requisite, you can skip it and the App will use a mock server we created. Alternately you can try to quickly sign up [here](https://developer.twitter.com/en/apply-for-access), however this may take several minutes.

1. Access your Twitter Developer Account by navigating to the [Dashboard](https://developer.twitter.com/en/portal/dashboard). 
1. Click "Projects & Apps" in the left sidebar.
1. Click "Overview" in the expanded options in the left sidebar.
1. Create a new "App" by clicking the blue outlined button "Create App" at the bottom of the "Overview" page.
1. Enter a helpful name. Suggested: "PagerDuty Summit App"
1. Click "Complete"
1. Copy the "Bearer token", a 116 length string.
1. Back in the editor paste in the copied Bearer Token inbetween the quotes of the key `TWITTER_BEARER_TOKEN`.in the `.env` file.

For example: `TWITTER_BEARER_TOKEN="my-key-goes-here"`
