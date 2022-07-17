#author          : Agung Pambudi
#email           : mail@agungpambudi.com
#linkedin        : http://linkedin.com/in/agungpambudi
#version         : 0.5
#
#
#==============================================================================
#                                   _         _ _
# ___ ___ _ _ ___ ___ ___ ___ _____| |_ _ _ _| |_|  ___ ___ _____
#| .'| . | | |   | . | . | .'|     | . | | | . | |_|  _| . |     |
#|__,|_  |___|_|_|_  |  _|__,|_|_|_|___|___|___|_|_|___|___|_|_|_|
#    |___|       |___|_|


import tabula
import os

file1 = "sample_pdf.pdf"
# table = tabula.read_pdf(file1, pages=1)   # to read table in [first page] of PDF File
# # tables = tabula.read_pdf(file1, pages=1, multiple_tables=True)   # reads multiple tables as independent tables

# print(table[0])


# tables = tabula.read_pdf("sample_pdf.pdf", pages="all")  # read PDF file


tabula.convert_into(file1, "data-table.csv", pages="all")    # converting all table in PDF File to CSV
# tabula.convert_into(tables, "sample_pdf.xlsx", output_format="xlsx")     # export PDF into Excel