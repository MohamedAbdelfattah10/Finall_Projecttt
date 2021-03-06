from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
directory="E:/Abdelfattah/First_Test_NER/Rename/"

def rename(directory):
        i=0
        os.chdir(directory) # Changing to the directory you specified.
        for name in os.listdir(directory):
            print(name)
            
            os.rename(name,str(i)+".pdf")
            i=i+1  

rename(directory)

    
def ocr(PDF_file):
#Converting PDF to images
    pages = convert_from_path(PDF_file, 500)
    # Counter to store images of each page of PDF to image
    image_counter = 1
    for page in pages:
    	filename = "page_"+str(image_counter)+".jpg"
    	page.save(filename, 'JPEG')
    	image_counter = image_counter + 1
    # Recognizing text from the images
    filelimit = image_counter-1
    # Creating a text file to write the output
    outfile = "out_text.txt"
    # Open the file in append mode so that
    f = open(outfile, "a",encoding="utf-8")
    s = open(outfile, "a",encoding="utf-8")
    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1):
    	filename = "page_"+str(i)+".jpg"
    	# Recognize the text as string in image using pytesserct
    	text = str(((pytesseract.image_to_string(Image.open(filename)))))
    	text = text.replace('-\n', '')	
    	# Finally, write the processed text to the file.
    	f.write(text)
    s.write("-----------")
    #print(text)
    # Close the file after writing all the text.
    f.close()
    return 0 

for i in range(212):
    pdf="E:/Abdelfattah/First_Test_NER/Rename/"+str(i)+".pdf"
    print(pdf)
    ocr(pdf)
      