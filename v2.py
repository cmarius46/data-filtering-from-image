from PIL import Image
from pytesseract import pytesseract
from os import listdir

#Define path to tessaract.exe

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Define path to image
path_to_image = 'test2.png'


text = pytesseract.image_to_string(img)
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME)

currentRow = []
text_by_rows = []

for i in range(len(data)):
	if str(data['text'][i]) == 'nan':
		if len(currentRow) != 0:
			text_by_rows.append(currentRow)
		currentRow = []
	else:
		currentRow.append(str(data['text'][i]).lower())


for row in text_by_rows:	
	print(row)
	print('=====')

