import fitz  # PyMuPDF

def convert_pdf2txt(pdf_file_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_file_path)
        
        # Extract text from each page of pdf file
        text = ""
        for page in pdf_document:
            text += page.get_text()
        
        # Save extracted text to a text file
        text_file_path = "text.txt"
        with open(text_file_path, "w") as text_file:
            text_file.write(text)
        
        return(f"File converted and data saved in {text_file_path}")
    
    except Exception as e:
        return f"Error: {e}"

# Usage example:
pdf_file_path = "pdf_file.pdf"
result = convert_pdf2txt(pdf_file_path)
print(result)
