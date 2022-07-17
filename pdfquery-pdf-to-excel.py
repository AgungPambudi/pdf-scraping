#author          : Agung Pambudi
#email           : mail@agungpambudi.com
#linkedin        : http://linkedin.com/in/agungpambudi
#version         : 0.5
#
#
# sumber (https://medium.com/@vince.shields913/handling-data-stored-across-multiple-pdf-files-with-python-33c6c26425c8)
#
#==============================================================================
#                                   _         _ _
# ___ ___ _ _ ___ ___ ___ ___ _____| |_ _ _ _| |_|  ___ ___ _____
#| .'| . | | |   | . | . | .'|     | . | | | . | |_|  _| . |     |
#|__,|_  |___|_|_|_  |  _|__,|_|_|_|___|___|___|_|_|___|___|_|_|_|
#    |___|       |___|_|


import pandas as pd
import numpy as np
import pdfquery
import argparse

pdf = pdfquery.PDFQuery('sample_pdf.pdf')
pdf.load()

# pdf.tree.write('sample_pdf.xml', pretty_print=True)

# project_name = pdf.pq('LTTextLineHorizontal:in_bbox("268.56, 741.12, 344.76, 750.12")').text()
# print(project_name, end='\n\n')

# web_url = pdf.pq('LTTextBoxHorizontal:in_bbox("481.56, 568.8, 562.32, 575.8")').text()
# print(web_url, end='\n\n')

# for i in range(0, 5):
#     project_name = pdf.pq('LTTextLineHorizontal:overlaps_bbox("235.44, 740.76, 344.76, 748.12")').text()
#     print(project_name, end='\n\n')



def extract_cells(page, header, cell_width):
    name_element = pdf.pq('LTPage[pageid=\'%s\'] LTTextLineHorizontal:contains("%s")' % (page, header))[0]
    x = float(name_element.get('x0'))
    y = float(name_element.get('y0'))
    cells = pdf.extract( [
         ('with_parent','LTPage[pageid=\'%s\']' %(page)),
         ('cells', 'LTTextLineHorizontal:in_bbox("%s,%s,%s,%s")' % (x, y-500, x+cell_width, y))
    ])
    return [cell.text.encode('utf-8').strip() for cell in cells['cells']]
    