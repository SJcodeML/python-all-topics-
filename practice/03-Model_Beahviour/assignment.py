from pydantic import Field, BaseModel, computed_field 

# create Booking model
# Feilds:
# user_id :int
# room_id:int
# nights :int(must be >=1)
# rate_per_night :float
# Also, add computed field :total_amount = nights *rate_per_night 



class Booking_hotel(BaseModel):
    user_id:int
    room_id:int
    nights :int = Field (... , ge = 1)
    rate_per_night : float 



    @computed_field
    @property
    def toal_amount (self)->int:
        return self.nights * self.rate_per_night



