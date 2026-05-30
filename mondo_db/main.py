from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = AsyncIOMotorClient(MONGO_URL)
db = client["neuron"]
neuron_data = db["neuron_coll"]

app = FastAPI()

class neurondata(BaseModel):
    name : str
    phone_no : int
    city : str
    course : str


@app.post("/euron/insert")
async def neuron_data_inser_helper(data:neurondata):
    result = await neuron_data.insert_one(data.dict())
    # return {"message": "data  inserted in mongodb successfully"}
    return str(result.inserted_id)

def euron_helper(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


@app.get("/euron/getdata")    
async def get_euron_data():
    items=[]
    cursor = neuron_data.find({})
    async for document in cursor:
        items.append(euron_helper(document))
    return items
