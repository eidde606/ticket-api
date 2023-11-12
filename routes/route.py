from fastapi import APIRouter
from models.ticket import Ticket
from config.database import collection_name

from schema.schema import list_serial
from bson import ObjectId

router = APIRouter()


# GET request method
@router.get("/")
async def get_tickets():
    tickets = list_serial(collection_name.find())
    return tickets


# POST
@router.post("/")
async def post_ticket(ticket: Ticket):
    collection_name.insert_one(dict(ticket))


# PUT
@router.put("/{id}")
async def put_ticket(id: str, ticket: Ticket):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(ticket)})


# DELETE
@router.delete("/{id}")
async def delete_ticket(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
