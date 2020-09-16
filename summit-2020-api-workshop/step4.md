# What are we building?

We'll be building a simple Twitter integration.

We will run an app that upon startup will do the following:

1. Create and get necessary information from our PagerDuty account.
1. Query Twitter for Tweets that contain "#pdsummit", or "@pagerduty"
1. Send all of the matching Tweets to PagerDuty
1. Use an Event Rule in PagerDuty to create an Alert when one of those Tweets also contains a mention of PagerDuty CEO Jennifer Tejada ([@jenntejada](https://twitter.com/jenntejada))
