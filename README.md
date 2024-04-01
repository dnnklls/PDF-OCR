

# PDF-OCR

## Project Description
This Processing System is a Python-based tool designed to automate the handling of event data. It efficiently converts ticket PDFs into images, utilizes Optical Character Recognition (OCR) to read text, and scans for barcodes/QR codes. The system extracts essential ticket information and saves it in both JSON and CSV formats, facilitating easy data management and analysis.

## Features
- **PDF to Image Conversion**: Converts PDFs into image files for processing.
- **OCR Functionality**: Extracts text data from images using Tesseract OCR.
- **Barcode and QR Code Scanning**: Identifies and decodes barcode information.
- **Data Extraction**: Retrieves specific information from data, such as name, order number, and seat details.
- **Data Storage**: Saves extracted data in JSON and CSV formats for further use.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Poppler – for PDF to image conversion
- Tesseract OCR – for optical character recognition

### Installation Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dnnklls/PDF-OCR.git
   ```
2. **Navigate to the Project Directory**
   ```bash
   cd path/to/project
   ```
3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Manual Dependencies Installation**
   - Manually install Poppler and Tesseract OCR and add their executables to your system's PATH.

### Usage Instructions
1. Place your PDF tickets in the `tickets` directory.
2. Run the script:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the name of your main Python script.

## Contributing
Contributions to the Ticket Processing System are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Tesseract OCR
- Poppler
- The Python community for various helpful resources

---
