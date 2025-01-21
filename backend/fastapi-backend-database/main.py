from fastapi import FastAPI
from routes.predict_route import predict_router
# Ensure extract_router is an instance of APIRouter
from routes.extract_route import extract_router
from config.database import collection_name
from schema.schemas import list_serialise
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(predict_router)
app.include_router(extract_router)

app.add_middleware(
    CORSMiddleware,
    # Allow all origins, replace with specific URLs as needed
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/get-details")
async def get_details():
    details = list_serialise(collection_name.find())
    return details

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
