from PyPDF2 import PdfReader

# Class responsible for extracting text from PDF files
class PDFExtractor:
    def __init__(self):
        # Initialize an empty string to store the extracted text
        self.__text = ""

    def extract_text_from_pdf(self, pdf_file):
        try:
            # Open the PDF file in binary read mode
            with open(pdf_file, 'rb') as file:
                # Create a PdfReader object to read the PDF content
                pdf_reader = PdfReader(file)

                # Iterate through each page in the PDF
                for page_num in range(len(pdf_reader.pages)):
                    # Get the current page
                    page = pdf_reader.pages[page_num]

                    # Extract text from the current page and append it to the text attribute
                    self.__text += page.extract_text()
                return self.__text
        except Exception as e:
            # Handle any exceptions that may occur during PDF reading
            print(f"Error reading PDF file '{pdf_file}': {e}")
            return ""