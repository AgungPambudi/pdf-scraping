#author          : Agung Pambudi
#email           : mail@agungpambudi.com
#linkedin        : http://linkedin.com/in/agungpambudi
#version         : 0.5
#
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

file1 = "data-table.pdf"
table = tabula.read_pdf(file1, pages=1)   # to read table in [first page] of PDF File
# tables = tabula.read_pdf(file1, pages=1, multiple_tables=True)   # reads multiple tables as independent tables

print(table[0])


tables = tabula.read_pdf("data-table.pdf", pages="all")  # read PDF file

# ------------------ iterating over all extracted tables and saving them as Excel spreadsheets
# save them in a folder
folder_name = "tables"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

# iterate over extracted tables and export as excel individually
for i, table in enumerate(tables, start=1):
    table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)

# This will create tables folder and put all detected tables in Excel format into that folder
# --------------------------------------------------------------------------------------------

# If you have multiple PDF files and you want to run the above on all of them, then you can use convert_into_by_batch() method:
# convert all PDFs in a folder into CSV format
# `pdfs` folder should exist in the current directory
# tabula.convert_into_by_batch("pdfs", output_format="csv", pages="all")


# output just the first page tables in the PDF to a CSV
# tabula.convert_into(file1, "data-table.csv")
# tabula.convert_into(file1, "output.csv", output_format="csv", pages="all")


tabula.convert_into(file1, "data-table.csv", all=True)    # converting all table in PDF File to CSV
tabula.convert_into(file1, "data-table.xlsx", output_format="xlsx")     # export PDF into Excel