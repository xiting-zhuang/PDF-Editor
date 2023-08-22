import PyPDF2

class PDFMerger:
    def __init__(self, filename):
        self.filename = filename

    def extract_text_from_page(self, page_number):
        with open(self.filename, 'rb') as pdfFile:
            reader = PyPDF2.PdfReader(pdfFile)
            page = reader.pages[page_number - 1]
            text = page.extract_text()
            return text

if __name__ == "__main__":
    pdf_filename = 'new.pdf'
    pdf_text_extractor = PDFMerger(pdf_filename)
    page_number = 2  # Extract text from the second page
    extracted_text = pdf_text_extractor.extract_text_from_page(page_number)
    print(extracted_text)