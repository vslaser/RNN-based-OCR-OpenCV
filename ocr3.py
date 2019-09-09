from PIL import Image
import pytesseract
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help = "path to input image to be OCR'd")
ap.add_argument("-p",  "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
args = vars(ap.parse_args())

image = cv2.imread(args["images"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
 
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
#print(text)

#import datetime
#name = "Path" + str(datetime.datetime.now().minute) + str(datetime.datetime.now().second) + ".docx"

'''from docx import Document
from docx.shared import Inches
document = Document("Document.docx")
document.add_paragraph(text)
document.save("Path\\Document.docx")
#document.save(name)'''

with open("Path\\Document.docx", "a" as file:
	file.write(text)

