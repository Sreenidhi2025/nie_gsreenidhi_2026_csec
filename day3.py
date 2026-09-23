from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
app = FastAPI()
URL = "mongodb://127.0.0.1:8000"
client=MongoClient(URL)
db = client["service_ticket_db"]
ticket_collection = db["tickets"]
class TicketCreate(BaseModel):
    title : str
    deacription :str
    category : str
    status :str
class TicketResponse(TicketCreate):
    id : str
#helper 
def 