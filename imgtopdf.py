import img2pdf
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

foldername = "Hattara Yarachau!? Ero SealWith One Sheet Selfish High Schoolers Become Enslaved To Cock~ Ch.1-3 [English]"
img_group = "2183344"
number_of_page = 84

if not os.path.exists(foldername+"/pdf"):
	os.makedirs(foldername+"/pdf")
for x in range(1,number_of_page):
	pdf_bytes = img2pdf.convert([foldername+"/"+img_group+"_"+str(x)+".jpg"])
	file = open(foldername+"/pdf/"+img_group+"_"+str(x)+".pdf","wb")
	file.write(pdf_bytes)

print("Done convert : "+str(number_of_page)+" pages of "+foldername+" to pdf")
print("EachPDF location : "+foldername+"/pdf/")

# Creating a routine that appends files to the output file
def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

# Creating an object where pdf pages are appended to
output = PdfFileWriter()

# Appending two pdf-pages from two different files
for x in range(1,number_of_page):
	append_pdf(PdfFileReader(open(foldername+"/pdf/"+img_group+"_"+str(x)+".pdf","rb")),output)

# Writing all the collected pages to a file
output.write(open(foldername+"/"+foldername+".pdf","wb"))

print("Done merge : "+foldername+" pdfs")
print("PDF location : "+foldername+"/")