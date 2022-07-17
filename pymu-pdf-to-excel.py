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


import fitz
import pandas as pd 

doc = fitz.open('sample_pdf.pdf')
page1 = doc[0]
words = page1.get_text("Alberni")

print(words[0])