from model.lin_reg_loading import load_model
from predict.predict_price import predict_price
from preprocessing.cleaning_data import preprocess
from typing import Optional
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import sklearn

model = load_model()

class PropertyName(str, Enum):
    apartment = "APARTMENT"
    house = "HOUSE"
    others = "OTHERS"

class BuildingState(str, Enum):
    new = "NEW"
    good = "GOOD"
    to_renovate = "TO RENOVATE"  
    just_renovated = "JUST RENOVATED"
    to_rebuild = "TO REBUILD"

class BuildingData(BaseModel):
    area: int
    property_type: Optional[PropertyName]
    rooms_number: Optional[int]
    zip_code: int
    land_area: Optional[int]
    garden: Optional[bool]
    garden_area: Optional[int]
    equipped_kitchen: Optional[bool]
    full_address: Optional[str]
    swimming_pool: Optional[bool]
    furnished: Optional[bool]
    open_fire: Optional[bool]
    terrace: Optional[bool]
    terrace_area: Optional[int]
    facades_number: Optional[int]
    building_state: Optional[BuildingState]

class PropertyName(str, Enum):
    apartment = "APARTMENT"
    house = "HOUSE"
    others = "OTHERS"

class BuildingState(str, Enum):
    new = "NEW"
    good = "GOOD"
    to_renovate = "TO RENOVATE"  
    just_renovated = "JUST RENOVATED"
    to_rebuild = "TO REBUILD"

app = FastAPI()
# run with uvicorn main:app --reload

@app.get("/")
async def is_alive():
    return "alive"

@app.post("/predict/")
async def predict_request(data : BuildingData):
    data_dict = {i[0]: i[1] for i in data}
    print(data_dict)
    df = preprocess(data_dict)
    prediction = 10**predict_price(model, df)[0]
    return {"prediction" : prediction}

@app.get("/predict/")
async def predict_specs():
    message = """This endpoint lets you predict price with a linear regression model
    trained on data from ImmoWeb.
    A proper request body looks like this;
     - with OPTIONAL denoting an optional input (area and zip_code are required)
     - several strings meaning you have to pick one out of them:
'{
  "area": int,
  "property_type": OPTIONAL "APARTMENT", "HOUSE", "OTHERS"
  "rooms_number": OPTIONAL int, 
  "zip_code": int,
  "land_area": OPTIONAL int,
  "garden": OPTIONAL true, false
  "garden_area": OPTIONAL int,
  "equipped_kitchen": OPTIONAL true, false
  "full_address": OPTIONAL "string",
  "swimming_pool": OPTIONAL true, false
  "furnished": OPTIONAL true, false
  "open_fire": OPTIONAL true, false
  "terrace": OPTIONAL true, false
  "terrace_area": OPTIONAL int,
  "facades_number": OPTIONAL int,
  "building_state": OPTIONAL "NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED","TO REBUILD"
}'
    
    The API give an output such as:
    {"prediction" : prediction}

    """
    return {"message" : message}
