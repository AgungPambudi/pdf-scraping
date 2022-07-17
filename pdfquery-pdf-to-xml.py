#author          : Agung Pambudi
#email           : mail@agungpambudi.com
#linkedin        : http://linkedin.com/in/agungpambudi
#version         : 0.5
#
#
# sumber (https://www.annytab.com/extract-text-from-pdf-or-image-in-python/)
#
#==============================================================================
#                                   _         _ _
# ___ ___ _ _ ___ ___ ___ ___ _____| |_ _ _ _| |_|  ___ ___ _____
#| .'| . | | |   | . | . | .'|     | . | | | . | |_|  _| . |     |
#|__,|_  |___|_|_|_  |  _|__,|_|_|_|___|___|___|_|_|___|___|_|_|_|
#    |___|       |___|_|


import pandas as pd
import pytesseract
import pdf2image


# Read a pdf file as image pages
pages = pdf2image.convert_from_path(pdf_path='sample pdf.pdf', dpi=500, poppler_path=
    r'D:\Upwork\PDFScraping\poppler-22.01.0-0\poppler-22.01.0\Library\bin')
# Convert a page to hocr (page 2)
# content = pt.image_to_pdf_or_hocr(pages[1], lang='swe', nice=0, extension='hocr')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
content = pytesseract.image_to_pdf_or_hocr(pages, lang='swe', nice=0, extension='hocr')
# Write content to a new file, owerwrite w or append a (b=binary)
f = open('sample_pdf.hocr', 'w+b')
f.write(bytearray(content))
f.close()