from fastapi import FastAPI
from workflow import execute_workflow, get_execution_status
from firestore import get_state


app = FastAPI(title="FastAPIServer2")


@app.post("/trigger_workflow")
async def trigger_workflow(x: str):
    res = execute_workflow(x)
    return res
    

@app.get("/check_status")
async def check_status(x: str):
    status = get_execution_status(x)

    if status == "ACTIVE":
        state = get_state(x)
        return state
    return status

