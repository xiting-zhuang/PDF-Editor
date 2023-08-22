from pdfReader import PDFMerger as PDFReaderMerger
from pdfMerger import PDFMerger as PDFMergerMerger

if __name__ == "__main__":
    # Using PDFReaderMerger to extract text
    pdf_reader = PDFReaderMerger("new.pdf")
    page_number = 2  # Extract text from the second page
    extracted_text = pdf_reader.extract_text_from_page(page_number)
    print("Extracted Text:")
    print(extracted_text)

    # Using PDFMergerMerger to merge PDFs
    pdf_merger = PDFMergerMerger()
    pdf_merger.merge_pdfs_in_directory(directory="./merging")
    pdf_merger.write_merged_pdf("combinedFile.pdf")
    print("PDFs merged successfully.")
