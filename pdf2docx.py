from docx import Document
import os
from ocr2 import perform_ocr

def save_text_to_docx(text, output_path):
    print("here you are getting permission error")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print("folder created")
    # Create a new Document
    doc = Document()
    # Add the text to the document
    doc.add_paragraph(text)
    # Save the document to the specified path
    doc.save(output_path)
    print(f"The document has been saved to {output_path}")
    
def ocr_to_docx(file_path, docx_output_path):
    document = perform_ocr(file_path)
    save_text_to_docx(document.text, docx_output_path)
    
# pdf_or_image_path = "C:\\Resume\\Nitesh-Kumar (2).pdf"
# docx_output_path = "C:\\Users\\Dell\\OCR_NER\\saved_docx\\OutputText2.docx"
# ocr_to_docx(pdf_or_image_path, docx_output_path)
    
    
