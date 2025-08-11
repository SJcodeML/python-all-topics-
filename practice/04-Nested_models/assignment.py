# NESTED CLASS 
# ek class dosri class ko reference karhi h 


from pydantic import BaseModel
from typing import List ,Optional



class Address (BaseModel):
    street: str
    city : str
    postal_code : str


class User(BaseModel):
    id:int 
    name :str
    address : Address


# making instances


address = Address(street= 'karachi' , city = 'Peshawar' , postal_code='skjdhf235')

user = User(
    id = 1,
    name = 'sidra' , 
    address = address

)


# This example above mentions nested/reference model means ek class dosri class ko refer karhi h 



# SELF REFERENCE
# In this one class is referencing it self in the same class



class Comment (BaseModel):
    id : int
    content : str 
    replies : Optional[List['Comment']] = None


# above example is called forward referencing so we need to pass below method to the class or inthe file model_rebuild is not in the Comment class
#

Comment.model_rebuild()    


# making instance of Comment class

comment  = Comment(
    id = 156,
    content = 'skdjkjdfkkcjkmkcmlkclksd',
    replies= [
        Comment(id = 3562 , content='sdkjskd' , replies= [
            Comment(id = 561 , content= 'dkjsdcjknckn'),
            Comment(id = 562 , content = 'anjkdvkjdkv')
            
        ])
        ]
        )
    
