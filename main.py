from os import walk
import cv2
import pytesseract
import re
import PyPDF2
import tabula
import numpy as np

_img_dir = 'input/'
_pdf_dir = 'input_pdf/'

def read_img(_path=''):
	_patterns = r'([0-9]{3}\.[0-9]{3})|([0-9]{3}\,[0-9]{3})'

	# list all filenames inside _path 
	filenames = next(walk(_path), (None, None, []))[2]  # [] if no file

	# process all images inside _path 
	for f in filenames:
		# image2text processing
		img = cv2.imread(f"{_path}/{f}")
		text = pytesseract.image_to_string(img)
		
		# pattern matching
		nominal = ''
		for e in text.split():
			if re.search(_patterns, e):
				nominal = e
		

		res = {
			'filename': f,
			'nominal': nominal
		}

		print(res)

def read_pdf(_path=''):
	_patterns = r'([0-9]{3}\.[0-9]{3})|([0-9]{3}\,[0-9]{3})'
	res = []

	# list all filenames inside _path 
	filenames = next(walk(_path), (None, None, []))[2]  # [] if no file
	
	# process all pdf inside _path 
	for f in filenames:
		df = tabula.read_pdf(f"{_path}/{f}", pages="all", )
		print(f"Filename: {f} [{len(df)} pages]")
		
		for i, page in enumerate(df):
			for colName, colData in page.iteritems():
				for e in colData.values:
					if re.search(_patterns, str(e)):
						# print(int(''.join(filter(str.isdigit, str(e)[:-3]))))
						res.append(int(''.join(filter(str.isdigit, str(e)[:-3]))))
		
	print(res)


if __name__ == '__main__':
	# print('read_img')
	# read_img(_img_dir)

	print('read_pdf')
	read_pdf(_pdf_dir)