import os
import json
import csv
import logging
from pdf2image import convert_from_path
import pytesseract
from pytesseract import Output
import cv2
from pyzbar.pyzbar import decode

# Setup logging
logging.basicConfig(filename='ticket_processing.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def convert_pdf_to_images(pdf_path):
    """
    Convert a PDF file to images.
    :param pdf_path: Path to the PDF file.
    :return: List of image paths.
    """
    try:
        images = convert_from_path(pdf_path)
        image_paths = []
        for i, image in enumerate(images):
            image_path = f"images/{os.path.splitext(os.path.basename(pdf_path))[0]}_{i + 1}.png"
            image.save(image_path, 'PNG')
            image_paths.append(image_path)
        return image_paths
    except Exception as e:
        logging.error(f"Error converting {pdf_path} to images: {e}")
        return []

def process_image(image_path):
    """
    Perform OCR on the image and decode any barcodes or QR codes.
    :param image_path: Path to the image file.
    :return: Extracted text and codes.
    """
    try:
        img = cv2.imread(image_path)
        # Perform OCR
        text = pytesseract.image_to_string(img, lang='eng', output_type=Output.DICT)
        # Decode barcodes and QR codes
        codes = decode(img)
        return {"text": text['text'], "codes": [{"data": code.data.decode('utf-8'), "type": code.type} for code in codes]}
    except Exception as e:
        logging.error(f"Error processing image {image_path}: {e}")
        return {"text": "", "codes": []}

def extract_ticket_info(ocr_result):
    """
    Extract specific information from OCR result.
    :param ocr_result: OCR result dictionary.
    :return: Dictionary of extracted ticket information.
    """
    # Define the fields you want to extract and any regex patterns if needed
    ticket_info = {"name": "", "seat": "", "barcode": ""}
    # Extract info from OCR result here
    # Example: ticket_info["name"] = extract_with_regex(ocr_result["text"], "Name: (.*)")
    return ticket_info

def save_to_json(data, output_path):
    """
    Save data to a JSON file.
    :param data: Data to be saved.
    :param output_path: Output file path.
    """
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, output_path):
    """
    Save data to a CSV file.
    :param data: Data to be saved.
    :param output_path: Output CSV file path.
    """
    with open(output_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    pdf_directory = 'tickets'
    output_json = 'output.json'
    output_csv = 'output.csv'

    all_data = []
    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            image_paths = convert_pdf_to_images(pdf_path)
            for image_path in image_paths:
                ocr_result = process_image(image_path)
                ticket_info = extract_ticket_info(ocr_result)
                ticket_info['file'] = os.path.basename(pdf_file)
                all_data.append(ticket_info)
    
    save_to_json(all_data, output_json)
    save_to_csv(all_data, output_csv)

if __name__ == '__main__':
    main()
