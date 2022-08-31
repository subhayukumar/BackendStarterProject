from google.cloud.workflows.executions_v1beta.services.executions import ExecutionsClient
from google.cloud.workflows.executions_v1beta.types import ListExecutionsRequest, Execution
from google.cloud.workflows.executions_v1beta.types import executions
import json

client = ExecutionsClient()
project = "backendstarterproject-361103"
location = "us-central1"
workflow = "workflow1"
parent = f"projects/{project}/locations/{location}/workflows/{workflow}"


def execute_workflow(x: str):
    arguments = {"name": x}
    execution = Execution(argument = json.dumps(arguments))

    try:
        response = client.create_execution(parent=parent, execution=execution).name
    except:
        response = "Error occurred when triggering workflow execution", 500

    return response



def get_execution_status(x: str):
    # Initialize request argument(s)
    request = ListExecutionsRequest(
        parent=parent,
    )
    
    # Make the request
    page_result = client.list_executions(request=request)
    result = list(page_result)[0]
    state = result.state.__str__().split(".")[1]
    return state

