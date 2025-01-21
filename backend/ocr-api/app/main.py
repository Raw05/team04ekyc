from fastapi import FastAPI, File, UploadFile, HTTPException
from app.ocr.preprocessing import preprocess_image
from app.ocr.ocr_utils import perform_ocr
from app.ocr.classification import classify_document
from app.ocr.data_extraction import extract_data_by_type
import os
import shutil
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # Allow all origins, replace with specific URLs as needed
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.post("/predict/")
async def predict(file: UploadFile = File(...), preprocess: str = "thresh"):
    try:
        # Save the uploaded file temporarily
        temp_dir = "temp"
        # Create the temp directory if it doesn't exist
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        temp_path = f"temp/{file.filename}"
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Preprocess the image
        processed_image = preprocess_image(temp_path, preprocess)

        # Perform OCR
        text = perform_ocr(processed_image)

        # Classify document
        document_type = classify_document(text)

        # # Extract data
        # extracted_data = extract_data_by_type(text, document_type)

        # # Cleanup
        # os.remove(temp_path)
        # os.remove(processed_image)

        return {
            "document_type": document_type,
            # "extracted_data": extracted_data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/extract/")
async def extract(file: UploadFile = File(...), preprocess: str = "thresh"):
    try:
        # Save the uploaded file temporarily
        temp_path = f"temp/{file.filename}"
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Preprocess the image
        processed_image = preprocess_image(temp_path, preprocess)

        # Perform OCR
        text = perform_ocr(processed_image)

        # Classify document
        document_type = classify_document(text)

        # Extract data
        extracted_data = extract_data_by_type(text, document_type)

        # Cleanup
        os.remove(temp_path)
        os.remove(processed_image)

        api_url = "http://localhost:8000/api/v1/extract"
        data = {
            "document_type": document_type,
            "extracted_data": extracted_data
        }
        # Send a POST request to the other API
        response = requests.post(api_url, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")

        return {
            "document_type": document_type,
            "extracted_data": extracted_data,
            "status": response.status_code,
            "conclusion": "uploaded to the database successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="localhost", port=3000, reload=True)
