import argparse
from pdf_extractor import PDFExtractor
from signature_generator import SignatureGenerator
from signature_saver import SignatureSaver
import os
def main():
    # Create a command-line argument parser with a description
    parser = argparse.ArgumentParser(description="Extract unique marker lines from PDF files and generate a signature.")

    # Define two required command-line arguments: input_folder and output_file
    parser.add_argument("input_folder", help="Path to the folder containing PDF files")
    parser.add_argument("output_file", help="Output JSON file name for the signature")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Generate a list of full paths to PDF files in the input folder
    pdf_files = [os.path.join(args.input_folder, filename) for filename in os.listdir(args.input_folder) if filename.endswith(".pdf")]

    # Initialize a list to store unique marker lines for each document
    document_marker_lines = []

    # Iterate through the PDF files in the input folder
    for pdf_file in pdf_files:
        # Create an instance of PDFExtractor
        pdf_extractor = PDFExtractor()

        # Extract text from the current PDF file and find unique markers
        text = pdf_extractor.extract_text_from_pdf(pdf_file)
        signature_generator = SignatureGenerator(text)
        signature_lines = signature_generator.find_unique_marker_lines()

        # Append the unique marker lines from the current document to the list
        document_marker_lines.append(signature_lines)

    # Find common marker lines across all documents
    common_marker_lines = set.intersection(*document_marker_lines)

    # Create an instance of SignatureSaver with the generated signature lines and the output file name
    signature_saver = SignatureSaver(common_marker_lines, args.output_file)

    # Save the signature lines to a JSON file
    signature_saver.save_signature_to_json()


if __name__ == "__main__":
    #sample input: python main.py data output.json
    main()