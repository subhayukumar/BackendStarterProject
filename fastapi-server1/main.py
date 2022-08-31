import re
from fastapi import FastAPI, HTTPException
from typing import Union
from time import sleep
from bigquery import insert_input_to_bq


app = FastAPI(title="FastAPIServer1")


@app.get("/is_valid_input")
def is_valid_input(x: str):
    if x.isdigit() or check_type(x, float):
        raise HTTPException(400, f"{type(eval(x))} is not allowed")
    
    elif check_type(x, bool):
        raise HTTPException(500)

    elif bool(re.match("^\w+$", x)):
        if x.islower():
            return "Success"
        else:
            return "Fail"
    

@app.post("/process")
async def process(x: str):
    sleep(180)
    insert_input_to_bq(x)
    return "Success"


def check_type(x: str, typ: Union[bool, float]):
    try:
        res = isinstance(eval(x), typ)
    except (NameError, SyntaxError):
        res = False
    return res
