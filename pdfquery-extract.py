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


def write_to_excel(df):
	writer = pd.ExcelWriter('example_patient_data.xlsx')
	df.to_excel(writer,'Main',index=False)
	writer.save()

def clean_text_data(text):
	return text.split(':')[1]

def pdf_to_df(pdf_list):	
	patient_data = {"Patient Number": [],
	               "Patient Name": [],
	               "DOB": [],
	               "Height": [],
	               "Weight": [],
	               "Diagnosis": [],
	               "Treatment": [],
	               "Recommendation": []}

	for i in pdf_list:
		pdf = pdfquery.PDFQuery(i)
		pdf.load()

		# pdf.tree.write('samplepdf1.xml', pretty_print = True)  # find the data by first writing the PDF to an XML

		patient_data["Patient Number"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Patient Number")')\
				                                         .text()))
		patient_data["Patient Name"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Patient Name")')\
				                                         .text()))
		patient_data["DOB"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("DOB")')\
				                                         .text()))
		patient_data["Height"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Height")')\
				                                         .text()))
		patient_data["Weight"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Weight")')\
				                                         .text()))
		patient_data["Diagnosis"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Diagnosis")')\
				                                         .text()))
		patient_data["Treatment"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Treatment")')\
				                                         .text()))
		patient_data["Recommendation"].append(clean_text_data(pdf.pq('LTTextLineHorizontal:contains("Recommendation")')\
				                                         .text()))
		
	columns=["Patient Number","Patient Name","DOB",
	"Height","Weight", "Diagnosis","Treatment","Recommendation"]
	pdata = pd.DataFrame.from_dict(patient_data)
	pdata = pdata[columns]

	return pdata

def main():

	#to_parse = ['samplepdf1.pdf','samplepdf2.pdf','samplepdf3.pdf','samplepdf4.pdf']

	parser = argparse.ArgumentParser(description = 'Parsing PDF')
	parser.add_argument('--parse', nargs='+', required=True)

	args = parser.parse_args()

	if args.parse:
		to_parse = args.parse


	pdata = pdf_to_df(to_parse)
	write_to_excel(pdata)

# python pdfquery-extract.py --parse 'samplepdf1.pdf' 'samplepdf2.pdf' 'samplepdf3.pdf' 'samplepdf4.pdf'
if __name__ == '__main__':
	main()
