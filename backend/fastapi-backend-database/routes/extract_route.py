from config.database import collection_name
from models.todos import Todo
from models.aadhar import AadharCard
from schema.schemas import list_serialise
from bson import ObjectId
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict

extract_router = APIRouter(prefix="/api/v1/extract")


class Document(BaseModel):
    document_type: str
    extracted_data: Dict


@extract_router.get("/")
async def get_todos():
    todos = list_serialise(collection_name.find())
    return todos
    return {"msg": "this is export route"}


@extract_router.post("/")
async def post_todo(document: Document):
    collection_name.insert_one(document.dict())
    return document


@extract_router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(todo)})


@extract_router.delete("/{id}/")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
