#author          : Agung Pambudi
#email           : mail@agungpambudi.com
#linkedin        : http://linkedin.com/in/agungpambudi
#version         : 0.5
#
#
# atau (sumber : https://www.analyticsvidhya.com/blog/2021/06/data-extraction-from-unstructured-pdfs/)
#
#==============================================================================
#                                   _         _ _
# ___ ___ _ _ ___ ___ ___ ___ _____| |_ _ _ _| |_|  ___ ___ _____
#| .'| . | | |   | . | . | .'|     | . | | | . | |_|  _| . |     |
#|__,|_  |___|_|_|_  |  _|__,|_|_|_|___|___|___|_|_|___|___|_|_|_|
#    |___|       |___|_|


# VSC Extension 
# autoDocstring - Python Docstring Generator

import sys, fitz
fname = sys.argv[1]  # get document filename
doc = fitz.open(fname)  # open document
out = open(fname + ".txt", "wb")  # open text output
for page in doc:  # iterate the document pages
    text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    out.write(text)  # write text of page
    out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
out.close()




import pandas as pd 

doc = fitz.open('File-Mansfield--70-21009048 - ConvertToExcel.pdf')
page1 = doc[0]
words = page1.get_text("words")

# extract the coordinates of the first object
first_annots = []
rec = page1.first_annot.rect
rec

# information of words in first object is stored in mywords
mywords = [w for w in words if fitz.Rect(w[:4]) in rec]
ann = make_text(mywords)
first_annots.append(ann)

# this function selects the words contained in the box, sort the words and return in form of a string
def make_text(words):
    line_dict = {} 
    words.sort(key = lambda w: w[0])

    for w in words:  
        y1 = round(w[3], 1)  
        word = w[4] 
        line = line_dict.get(y1, [])  
        line.append(word)  
        line_dict[y1] = line  

    lines = list(line_dict.items())
    lines.sort()  

    return "n".join([" ".join(line[1]) for line in lines])

# extracting each page of the document and all the annots/rectanges
for pageno in range(0,len(doc)-1):
    page = doc[pageno]
    words = page.get_text("words")

    for annot in page.annots():
        if annot != None:
            rec=annot.rect
            mywords = [w for w in words if fitz.Rect(w[:4]) in rec]
            ann = make_text(mywords)
            all_annots.append(ann)


# splitting to form column name and its values
cont = []

for i in range(0, len(all_annots)):
    cont.append(all_annots[i].split('n', 1))


# removing unnecessary symbols *,#,:
liss = []

for i in range(0,len(cont)):
    lis = []

    for j in cont[i]:
        j = j.replace('*','')
        j = j.replace('#','')
        j = j.replace(':','')
        j = j.strip()

        # print(j)
        lis.append(j)

    liss.append(lis)


# spliting into keys and values and removing spaces in the values which only contain digits
keys = []
values = []

for i in liss:
    keys.append(i[0])
    values.append(i[1])

for i in range(0, len(values)):
    for j in range(0, len(values[i])):
        if values[i][j] >= 'A' and values[i][j] <= 'Z':
            break            

    if j == len(values[i])-1:
       values[i] = values[i].replace(' ','')


# converting to dictionary
report = dict(zip(keys, values))
report['VEHICLE IDENTIFICATION'] = report['VEHICLE IDENTIFICATION'].replace(' ','')
dic = [report['LOCALITY'], report['MANNER OF CRASH COLLISION/IMPACT'], report['CRASH SEVERITY']]

l = 0
val_after = []

for local in dic:
    li = []
    lii = []
    k = ''
    extract = ''
    l = 0

    for i in range(0, len(local) - 1):
        if local[i + 1] >= '0' and local[i+1] <= '9':
            li.append(local[l:i + 1])
            l = i + 1
    li.append(local[l:])

    print(li)


    for i in li:
        if i[0] in lii:
            k = i[0]
            break
        lii.append(i[0])


    for i in li:
        if i[0] == k:
            extract = i
            val_after.append(extract)
            break


report['LOCALITY'] = val_after[0]
report['MANNER OF CRASH COLLISION/IMPACT'] = val_after[1]
report['CRASH SEVERITY'] = val_after[2]


# converting to DataFrame and exporting to CSV: 
data = pd.DataFrame.from_dict(report)
data.to_csv('final.csv', index = False)

