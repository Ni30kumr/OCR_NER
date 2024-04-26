from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import os
from ocr2 import perform_ocr,pipeline
from pdf2docx import ocr_to_docx,save_text_to_docx # Ensure this function is properly defined
from firebase import upload_file_to_firebase
from mangum import Mangum



app = FastAPI()

handler= Mangum(app)

@app.post("/upload/")
async def upload_file(username: str = Form(...), projectname: str = Form(...), file: UploadFile = File(...)):
    # Create directory path based on file type
    if file.content_type == 'application/pdf':
        subfolder = 'pdfs'
    elif file.content_type in ('image/jpeg', 'image/png'):
        subfolder = 'images'
    else:
        return JSONResponse(status_code=400, content={"message": "Unsupported file type"})

    # Construct the directory path including the subfolder
    directory_path = f"C:/Users/Dell/OCR_NER/{username}/{projectname}/{subfolder}"
    
    # Create directories if they do not exist
    os.makedirs(directory_path, exist_ok=True)
    
    # Define the file path
    file_path = os.path.join(directory_path, file.filename)
    
    # Save the file
    try:
        with open(file_path, "wb") as buffer:
            # Read file content in chunks and write to the file
            for data in iter(lambda: file.file.read(4096), b""):
                buffer.write(data)
        
        # Perform OCR on the saved file if it's a PDF or an image suitable for OCR
        if file.content_type in ('application/pdf', 'image/jpeg', 'image/png'):
            text = perform_ocr(file_path)
            print("you are here")
            docx_path = f"C:/Users/Dell/OCR_NER/{username}/{projectname}/saved_docx/OutputText.docx"
            # os.makedirs(docx_path, exist_ok=True)
            save_text_to_docx(text, docx_path)
            generated_url=upload_file_to_firebase(docx_path)
            print("now you are here")
            ner_results = pipeline(text)
            return JSONResponse(status_code=200, content={
                "message": "File uploaded and processed successfully",
                "ocr_text_path": generated_url,
                "ner_results": ner_results
            })
        else:
            return JSONResponse(status_code=200, content={"message": "File uploaded but not processed for OCR"})

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "An error occurred", "details": str(e)})


