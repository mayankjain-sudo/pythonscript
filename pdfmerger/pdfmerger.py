import os

from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

path_to_files = r'pdfmerger/pdffiles/'
file = []
for items in os.listdir(path_to_files):
    if items.endswith('.pdf'):
        merger.append( path_to_files + items)
        file.append(items)
merger.write(path_to_files + "Final_pdf.pdf")
merger.close()


