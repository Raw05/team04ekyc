from config.database import collection_name
from models.todos import Todo
from schema.schemas import list_serialise
from bson import ObjectId
from fastapi import APIRouter

predict_router = APIRouter(prefix="/api/v1/predict")


@predict_router.get("/")
async def get_todos():
    # todos = list_serialise(collection_name.find())

    return {"msg": "this is predict route"}


@predict_router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return todo


@predict_router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(todo)})


@predict_router.delete("/{id}/")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
