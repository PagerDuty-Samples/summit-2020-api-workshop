# Run the Skeleton App for the first time!

## Set the FLASK_APP environment variable

First we will need to set the `FLASK_APP` environment variable, so that the Flask server knows where the entry point is.

Note: this can't be done through the `.env` file we set up in the previous step, because the environment variable needs to exist _before_ we start the server.

`export FLASK_APP=server.py`{{execute}}

## Run the server for the first time


Next we'll run the Flask Server.

`flask run`{{execute}}

## NotImplementedError

We get a `NotImplemetedError`, this is expected as we need to implement some of our functions.

Let's get started implementing!

## Open `startup.py`

We'll be doing most of our work in this file. When our Flask server starts up, it enters this file through the `startup()` function.

**Click here to open** -> `./app/skeleton/startup.py`{{open}}

## Using PDPyras

[PDPyras](https://github.com/PagerDuty/pdpyras) is a lightweight Python client for our API.

The skeleton already instantiates a Session for making API requests in `startup.py`

### Need a shortcut?

You can use this commands to catch up and skip this step.

`export FLASK_APP=server.py`{{execute}}

`flask run`{{execute}}

**Click here to open** -> `./app/skeleton/startup.py`{{open}}
