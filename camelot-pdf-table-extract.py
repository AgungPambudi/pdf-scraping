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


import camelot

# PDF file to extract tables from
file = "foo.pdf"


# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted : ", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# export individually as CSV
tables[0].to_csv("foo.csv")

# export individually as Excel (.xlsx extension)
# tables[0].to_excel("foo.xlsx")

# or export all in a zip
# tables.export("foo.csv", f="csv", compress=True)

# export to HTML
# tables.export("foo.html", f="html")



