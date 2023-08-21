import PyPDF2
import sys
import os

class PDFMerger:
    def __init__(self):
        self.merger = PyPDF2.PdfMerger()

    def merge_pdfs_in_directory(self, directory="."):
        for file in os.listdir(directory):
            if file.endswith(".pdf"):
                self.merger.append(os.path.join(directory, file))

    def write_merged_pdf(self, output_file="combinedFile.pdf"):
        self.merger.write(output_file)
        self.merger.close()

if __name__ == "__main__":
    pdf_merger = PDFMerger()
    pdf_merger.merge_pdfs_in_directory(directory="./merging")
    pdf_merger.write_merged_pdf("new.pdf")
