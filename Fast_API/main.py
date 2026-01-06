from fastapi import FastAPI
from pydantic import BaseModel
from typing import List 


app = FastAPI()

class Tea(BaseModel):
    id:int
    name: str
    origin : str


teas:List[Tea] =[]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API"}


@app.get("/teas")
def get_teas():
    return teas


@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea



# enumerate is a handy built-in in Python for when you need both the index and the item while iterating 
# over a sequence. Here are the main reasons to use it:
# for i, item in enumerate(my_list):
    # print(i, item)
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea): 
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}   


@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea
    return {"error": "Tea not found"}