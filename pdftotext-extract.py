#author          : Agung Pambudi
#email           : mail@agungpambudi.com
#linkedin        : http://linkedin.com/in/agungpambudi
#version         : 0.5
#
#
# CONVERT PDF TO OCR pake notebook kita : PDF_OCR.ipynb (https://colab.research.google.com/drive/1WzkgBcWOQRgaep1J5xzWiA_8zE4Brv5w?usp=sharing)
#
#==============================================================================
#                                   _         _ _
# ___ ___ _ _ ___ ___ ___ ___ _____| |_ _ _ _| |_|  ___ ___ _____
#| .'| . | | |   | . | . | .'|     | . | | | . | |_|  _| . |     |
#|__,|_  |___|_|_|_  |  _|__,|_|_|_|___|___|___|_|_|___|___|_|_|_|
#    |___|       |___|_|


import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import pandas as pd

filePath = 'sample_pdf.pdf'
doc = convert_from_path(
    filePath,
    500,
    poppler_path=
    r'D:\Upwork\PDFScraping\poppler-22.01.0-0\poppler-22.01.0\Library\bin')
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)


page_counter = 1

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
for page_number, page_data in enumerate(doc):

    if (page_counter % 2) == 0:
        print("{0} is Even".format(page_counter))
    else:
        filename = "page_" + str(page_counter) + ".jpg"
        page_data.save(filename, 'JPEG')

    
    page_counter = page_counter + 1

    # txt = pytesseract.image_to_string(page_data).encode("utf-8")
    # print("Page # {} — {}".format(str(page_number), txt), end='\n\n')
    # DEBUG
    # file = open('output_sample_pdf.txt','a', encoding='utf-8') #write to a file
    # file.write("Page # {} — {}".format(str(page_number), txt))
    # file.close()

# Variable to get count of total number of pages
filelimit = page_counter - 1
  
# Creating a text file to write the output
outfile = "out_text.txt"
  
# Open the file in append mode so that 
# All contents of all images are added to the same file
f = open(outfile, "a")
  
# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
  
    if (filelimit % 2) == 0:
        # print("{0} is Even".format(filelimit))
        pass
        # print("{0} is Even".format(filelimit))
    else:
        print("{0} is Odd".format(filelimit))
        # Set filename to recognize text from
        # Again, these files will be:
        # page_1.jpg
        # page_2.jpg
        # ....
        # page_n.jpg

        # filename = "page_" + str(i) + ".jpg"
            
        # Recognize the text as string in image using pytesserct

        # text = str(((pytesseract.image_to_string(Image.open(filename)).encode("utf-8"))))
    

        # The recognized text is stored in variable text
        # Any string processing may be applied on text
        # Here, basic formatting has been done:
        # In many PDFs, at line ending, if a word can't
        # be written fully, a 'hyphen' is added.
        # The rest of the word is written in the next line
        # Eg: This is a sample text this word here GeeksF-
        # orGeeks is half on first line, remaining on next.
        # To remove this, we replace every '-\n' to ''.
        
        # text = text.replace('\n\n', ',')    
    
        # Finally, write the processed text to the file.
        
        # f.write(text)
  
# Close the file after writing all the text.

# f.close()


def clean_text_data(text):
    return text.split(':')[1]


def buildingpdf_to_df(pdf_list):

    building_info = {
        "Project ID": [],
        "Project Name": [],
        "City": [],
        "Address": [],
        "Neigbourhood": [],
        "Total Units": [],
        "Developer": [],
        "Storeys": [],
        "Other Uses": [],
        "Site Area": [],
        "FSR FAR": [],
        "Sales Start Date": [],
        "Current Mktg Status": [],
        "Incentives": [],
        "Walk Score": [],
        "Realtor Commission": [],
        "Total Deposit": [],
        "1st Dep": [],
        "2nd Dep": [],
        "3rd Dep": [],
        "Web URL": [],
        "Launch Status": [],
        "Current Status": [],
        "1st Occupancy": [],
        "Standing Inv": [],
        "Amenities": [],
        "Strata Condo Fee psf": [],
        "Kitchen Flooring": [],
        "Entry Flooring": [],
        "Living Flooring ": [],
        "Main Bath Flooring": [],
        "Bedrooms Flooring": [],
        "Kitchen Counters": [],
        "Main Bath Counters": [],
        "Ensuite Counters": [],
        "Cabinets Finish": [],
        "Appliances Finish": [],
        "Appliances Fridge": [],
        "Appliances Stove": [],
        "Appliances Microwave": [],
        "Appliances Brands": [],
        "Ceiling Height": [],
        "Parking Stall": [],
        "Storage Locker": [],
        "Storage Locker": [],
        "Heat Source": [],
        "AC": []
    }

    # floorplan_data = {
    #     "Project ID": [],
    #     "Project Name": [],
    #     "Plan Type": [],
    #     "Baths": [],
    #     "Stalls": [],
    #     "Rlsd": [],
    #     "Sold": [],
    #     "Unsold": [],
    #     "Min SF": [],
    #     "Max SF": [],
    #     "Min dollar": [],
    #     "Max dollar": [],
    #     "Min dollar psf": [],
    #     "Max dollar psf": []
    # }

    for i in pdf_list:
        pdf = pdfquery.PDFQuery(i)
        pdf.load()

        # patient_data["Patient Number"].append(
        #     clean_text_data(
        #         pdf.pq('LTText\
        # LineHorizontal:contains("Patient Number")').text()))

        building_info["Project ID"].append()
        building_info["Project Name"].append()
        building_info["City"].append()
        building_info["Address"].append()
        building_info["Neigbourhood"].append()
        building_info["Total Units"].append()
        building_info["Developer"].append()
        building_info["Storeys"].append()
        building_info["Other Uses"].append()
        building_info["Site Area"].append()
        building_info["FSR FAR"].append()
        building_info["Sales Start Date"].append()
        building_info["Current Mktg Status"].append()
        building_info["Incentives"].append()
        building_info["Walk Score"].append()
        building_info["Realtor Commission"].append()
        building_info["Total Deposit"].append()
        building_info["1st Dep"].append()
        building_info["2nd Dep"].append()
        building_info["3rd Dep"].append()
        building_info["Web URL"].append()
        building_info["Launch Status"].append()
        building_info["Current Status"].append()
        building_info["1st Occupancy"].append()
        building_info["Standing Inv"].append()
        building_info["Amenities"].append()
        building_info["Strata Condo Fee psf"].append()
        building_info["Kitchen Flooring"].append()
        building_info["Entry Flooring"].append()
        building_info["Living Flooring "].append()
        building_info["Main Bath Flooring"].append()
        building_info["Bedrooms Flooring"].append()
        building_info["Kitchen Counters"].append()
        building_info["Main Bath Counters"].append()
        building_info["Ensuite Counters"].append()
        building_info["Cabinets Finish"].append()
        building_info["Appliances Finish"].append()
        building_info["Appliances Fridge"].append()
        building_info["Appliances Stove"].append()
        building_info["Appliances Microwave"].append()
        building_info["Appliances Brands"].append()
        building_info["Ceiling Height"].append()
        building_info["Parking Stall"].append()
        building_info["Storage Locker"].append()
        building_info["Storage Locker"].append()
        building_info["Heat Source"].append()
        building_info["AC"].append()


    columns = [
        "Project ID", "Project Name", "City", "Address", "Neigbourhood",
        "Total Units", "Developer", "Storeys", "Other Uses", "Site Area",
        "FSR/FAR", "Sales Start Date", "Current Mktg Status", "Incentives",
        "Walk Score", "Realtor Commission", "Total Deposit", "1st Dep",
        "2nd Dep", "3rd Dep", "Web URL", "Launch Status", "Current Status",
        "1st Occupancy", "Standing Inv", "Amenities", "Strata/Condo Fee (psf)",
        "Kitchen Flooring", "Entry Flooring", "Living Flooring ",
        "Main Bath Flooring", "Bedrooms Flooring", "Kitchen Counters",
        "Main Bath Counters", "Ensuite Counters", "Cabinets Finish",
        "Appliances Finish", "Appliances Fridge", "Appliances Stove",
        "Appliances Microwave", "Appliances Brands", "Ceiling Height",
        "Parking Stall $", "Storage Locker", "Storage Locker $", "Heat Source",
        "AC"
    ]  # reorder the columns

    building_info_data = pd.DataFrame.from_dict(building_info)
    building_info_data = building_info_data[columns]

    return building_info_data


def floorplanpdf_to_df(pdf_list):

    floorplan_data = {
        "Project ID": [],
        "Project Name": [],
        "Plan Type": [],
        "Baths": [],
        "Stalls": [],
        "Rlsd": [],
        "Sold": [],
        "Unsold": [],
        "Min SF": [],
        "Max SF": [],
        "Min dollar": [],
        "Max dollar": [],
        "Min dollar psf": [],
        "Max dollar psf": []
    }

    for i in pdf_list:
        pdf = pdfquery.PDFQuery(i)
        pdf.load()

        # floorplan_data["Patient Number"].append(
        #     clean_text_data(
        #         pdf.pq('LTText\
        # LineHorizontal:contains("Patient Number")').text()))


        floorplan_data["Project ID"].append()
        floorplan_data["Project Name"].append()
        floorplan_data["Plan Type"].append()
        floorplan_data["Baths"].append()
        floorplan_data["Stalls"].append()
        floorplan_data["Rlsd"].append()
        floorplan_data["Sold"].append()
        floorplan_data["Unsold"].append()
        floorplan_data["Min SF"].append()
        floorplan_data["Max SF"].append()
        floorplan_data["Min dollar"].append()
        floorplan_data["Max dollar"].append()
        floorplan_data["Min dollar psf"].append()
        floorplan_data["Max dollar psf"].append()



    columns = [
        "Project ID", "Project Name", "Plan Type", "Baths", "# Stalls", "Rlsd",
        "Sold", "Unsold", "Min SF", "Max SF", "Min $", "Max $", "Min $ psf",
        "Max $ psf"
    ]  # reorder the columns

    floorplandf_data = pd.DataFrame.from_dict(floorplan_data)
    floorplandf_data = floorplandf_data[columns]

    return floorplandf_data


def write_to_excel(df):
    writer = pd.ExcelWriter('example_building_info_data.xlsx')
    df.to_excel(writer, 'Main', index=False)
    writer.save()


def main():

    building_infodata = buildingpdf_to_df("file_pdf")
    write_to_excel(building_infodata)

    # floorplan = floorplanpdf_to_df("file_pdf")
    # write_to_excel(floorplan)


# if __name__ == '__main__':
# 	main()
