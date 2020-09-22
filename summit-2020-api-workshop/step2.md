# Setup

First, we need to do some setup.

## Clone the example code

We need to clone the example code. In this repository we have the skeleton that we will be filling in over the course of this session, as well as the completed code if you'd like to skip ahead and see the finished app.

`git clone https://github.com/PagerDuty-Samples/summit-2020-api-workshop.git app && cd app/skeleton`{{execute}}

## Install some requirements

We will be using the the Python language to build our App. We will also be using some 3rd party Open Source Libraries. We can quickly install these using the commands below.

### 1. Install pipenv:

Pipenv is a helpful tool for managing dependencies, let's install it and install our dependencies.

`pip install pipenv && pipenv install`{{execute}}

### 2. Open the available shell:

Now that our dependencies are installed let's activate a virtual environment where we can use them.

`pipenv shell`{{execute}}

### You should see

After running step 1, you should see "✔ Successfully created virtual environment!"
After running step 2, your prompt should change from "$" to "(skeleton)"

## Need a shortcut?

You can use the following command to catch up really quickly:

`git clone https://github.com/PagerDuty-Samples/summit-2020-api-workshop.git app && cd app/skeleton && pip install pipenv && pipenv install && pipenv shell && echo "Done Setup!"`{{execute}}
