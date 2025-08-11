from pydantic import BaseModel , field_vaidator  , model_validator , computed_field

# FIELD_VALIDATOR
# kisi bhi value ko validate karne k liye hum field validator use karte hain 
# ap apne custom validators bana ssakte hain . or ye pehle run hote h pydantic k jane se pehle. 





class User (BaseModel) :
    username:str



    @field_vaidator('username')
    def username_length (cls , v):
        if len(v) < 4 :
            raise ValueError("username must be atleast of 4  characters")
        return v
    



# MODEL_VALIDATOR
# ye sub kuch hone k baad perform hoga is ka mode 'after' ka h 


class Sign_up(BaseModel):
    password:str
    confirm__password : str


    @model_validator(mode = 'after')
    def validation (cls , values):
        if values.password != values.confirm__password :
            raise ValueError("pelase type correct password")
        return values
          



# COMPUTED_PROPERTIES
# ye vaues koi operation perform karne k baad aati hain . like in example 


class Product(BaseModel):
    price:int
    quantity : float


    @computed_field
    @property
    def calculation(self ) -> float:
        return self.price * self.quantity