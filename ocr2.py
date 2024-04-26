from google.cloud import documentai_v1beta3 as documentai
from google.cloud.documentai_v1beta3 import types
import os
from inference import query

def perform_ocr(file_path):
    # Set up your GCP project and the region (e.g., 'us' or 'eu')
    project_id = 'documentparsingforner'
    location = 'us'  # Format is 'us' or 'eu'
    
    # Set the input configuration
    mime_type = 'application/pdf' if file_path.endswith('.pdf') else 'image/jpeg'
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # Set up the document processor resource name
    processor_id = '35fac3e2a22d3d16'  # This is the ID of the processor to use, e.g. for OCR
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    
    # Set up the Document AI client
    client = documentai.DocumentProcessorServiceClient()
    
    # Create the request
    request = types.document_processor_service.ProcessRequest(
        name=name,
        raw_document=types.RawDocument(content=content, mime_type=mime_type),
    )
    
    # Use the client to send the request
    result = client.process_document(request=request)
    
    # The result contains the document with OCR output
    document = result.document
    
    # The document text is in the document_text property
    print(f"Document text: {document.text}")
    return document.text

def chunk_text(text, max_chunk_size=100):
    """
    Splits the text into chunks with a maximum size of max_chunk_size.
    """
    for i in range(0, len(text), max_chunk_size):
        yield text[i:i + max_chunk_size]
        
        
def pipeline(text):
    # text = perform_ocr(filepath)
    
    # Split the document text into smaller chunks if necessary
    chunks = list(chunk_text(text))
    all_ner_results = []
    
    # Process each chunk with the NER model
    for chunk in chunks:
        NER_result = query({"inputs": chunk})
        all_ner_results.append(NER_result)
        
    return all_ner_results

# def pipeline(filepath):
#     text=perform_ocr(filepath)
#     NER=query({
# 	"inputs": text,
# })
#     print(NER)
    
# pipeline("C:\\Resume\\Nitesh-Kumar (2).pdf")
    
    



# Example usage
# Replace 'path-to-your-document' with the path to the PDF or image file you want to process.
# perform_ocr("C:\\Users\\Dell\\Pictures\\Screenshots\\Screenshot 2024-04-01 231453.png")