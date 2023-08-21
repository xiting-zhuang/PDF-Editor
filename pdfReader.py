import PyPDF2
import sys
import os

class PDFReader(): # with decrypt function

    def  __init__(self):
        self.reader = None

    def read_pdfs_in_directory(self, filename='./sample.pdf'):
        with open(filename, 'rb') as pdfFile:
            self.reader = PyPDF2.PdfFileReader(pdfFile)




if __name__ == "__main__":
    pdf_reader = PDFReader()
    pdf_reader.read_pdfs_in_directory(filename="./combinedFile.pdf")
