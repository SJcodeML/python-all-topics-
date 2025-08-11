from pydantic import BaseModel


class User(BaseModel):
    id: int
    name : str 
    is_active : bool


input_data = {"id" : 12, "name" :'sidra' , "is_active": 'True' }
print(input_data)      

user  = User(**input_data)
print (user)