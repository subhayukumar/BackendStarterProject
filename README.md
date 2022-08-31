# BackendStarterProject

Note - this task as is, is just a skeleton which closely resembles the actual starter task once the long term hiring decision is made. The long term hiring decision will be made based on the time estimate + actual delivery time + code quality + quality of work on this skeleton task. 

## Problem statement

Create a fastapi + gcp workflow + bigquery + gcp firebase stack that satisfies the requirements. 

## Details on each step

---
### Fastapi service 1

Fast api service needs to have 2 primary endpoints(and more auxiliary helper end points as you prefer)   -

GET endpoint -  is_valid_input(x) : which returns the string “Success” if the input is a string all in lower case, “Fail” is the input is a string that has upper case, returns a 4XX error with a message (“{data_type}” is not allowed) if the data type is an int or float and a 5XX( run time exception if the input is a Boolean) 

Post end point - process(x) which should sleep for 3 mins, write x as a string to a bigquery table(that has just one field with the name input) before returning “Success”

> **Server definition for FastAPI service 1 can be found under [fastapi-server1](fastapi-server1) directory**


---
## Gcp workflow

 (Link - [https://cloud.google.com/workflows](https://cloud.google.com/workflows))

The workflow should do the following

1. Accept an input called name 
2. Call the is_valid_input argument with the input name. 
    1. If the resultant http error code is 429, retry with exponential back off upto 3 times
    2. If the result is a 4XX/5XX, or a 2XX with message as “Fail” go directly to step 6 and write the error message onto bigquery 

   3. Update to fire base with the key as x and value as {“done”:[“valid_input_check”]}

1. Call process with x 
2. Update to firebase with the document id x and append [“process”] to the key “done” 
3. Load the result of valid_input_check and process to big query into a table which has 4 columns (name, valid_input_check, process, timestamp) 
4. Return (name, valid_input_check, process) as output from workflow


> **Workflow definition can be found in [WorkFlow.yaml](WorkFlow.yaml)**

---

## Fast api service 2

It has 2 endpoints - 

trigger workflow(x) which should trigger the workflow and return the workflow id 

check status(x) which should 

1. Check if workflow is done by checking the workflow status api - [https://cloud.google.com/workflows/docs/reference/rest/v1beta/projects.locations.workflows/get](https://cloud.google.com/workflows/docs/reference/rest/v1beta/projects.locations.workflows/get)
2. If the workflow is not done, check the state from firebase and return the state. 

> **Server definition for FastAPI service 2 can be found under [fastapi-server2](fastapi-server2) directory**

---

## Firebase

Use a firestore ([https://firebase.google.com/products/firestore](https://firebase.google.com/products/firestore)) to have a simple key value pair that will be used to update state in the workflow and check state in fast api service 2. 

---

## Task instructions

Use your own cloud for this task(most of these would be free for a small scale). 

Send the GitHub link to check the code once approved to start the task(if the estimate sounds reasonable)

---

## Deployment

1. Clone the repo in a server with: `git clone https://github.com/subhayukumar/BackendStarterProject`
2. Run `cd BackendStarterProject/fastapi-server1 && pip install -r requirements.txt && cd -` to install the dependencies for API server 1.
3. Run `cd BackendStarterProject/fastapi-server2 && pip install -r requirements.txt && cd -` to install the dependencies for API server 2.
4. Get a JSON key file for authenticating to Google Cloud and then run `export GOOGLE_APPLICATION_CREDENTIALS="<path to JSON key file>"`
5. Run `cd fastapi-server1 && uvicorn main:app --reload --host 0.0.0.0 --port <PORT_1>` in one terminal.
6. Run `cd fastapi-server2 && uvicorn main:app --reload --host 0.0.0.0 --port <PORT_2>` in another terminal.
7. Now visit [(http://<PUBLIC_IP>:<PORT_2>/docs)](http://<PUBLIC_IP>:<PORT_2>/docs) for viewing available routes.# BackendStarterProject
