from distutils.command.clean import clean
from os import walk
import cv2
import pytesseract
import re
import PyPDF2
import tabula
import numpy as np

_img_dir = 'input/'
_pdf_dir = 'input_pdf/'
_patterns = r'([0-9]{3}\.[0-9]{3})|([0-9]{3}\,[0-9]{3})'

_month_list = [
	{
		'img': 'sep',
		'pdf': '2021_09_ENDORS',	
	},{
		'img': 'oct',
		'pdf': '2021_10_ENDORS',	
	},{
		'img': 'nov',
		'pdf': '2021_11_ENDORS',	
	},{
		'img': 'dec',
		'pdf': '2021_12_ENDORS',	
	},{
		'img': 'jan',
		'pdf': '2022_01_ENDORS',	
	}
]

# _month_list = [
# 	{
# 		'img': 'sep',
# 		'pdf': '2021_10_ENDORS',	
# 	},{
# 		'img': 'oct',
# 		'pdf': '2021_11_ENDORS',	
# 	},{
# 		'img': 'nov',
# 		'pdf': '2021_12_ENDORS',	
# 	},{
# 		'img': 'dec',
# 		'pdf': '2022_01_ENDORS',	
# 	},
# ]

def clean_text(text=''):
	res = 0
	if text != '':
		res = text
		# remove .00 at the end
		if text[-3:] in ['.00', ',00'] :
			res = text[:-3]
		# get digit only
		res = filter(str.isdigit, str(res))
		# cast to int
		res = int(''.join(res))
	return res


def img2text(filename=''):
	# image2text processing
	img = cv2.imread(filename)
	text = pytesseract.image_to_string(img)
	
	# pattern matching
	nominal = ''
	for e in text.split():
		if re.search(_patterns, e):
			nominal = e
	
	res={
		'nominal': nominal,
		'value': clean_text(nominal),
		'filename': filename,
		'text': text
	}

	return res

def read_img(_path=''):
	res_list = []
	# list all filenames inside _path 
	filenames = next(walk(_path), (None, None, []))[2]  # [] if no file

	# process all images inside _path 
	for f in filenames:
		res = img2text(f"{_path}/{f}")
		res_list.append(res)
		# dump the filename and raw text of image if cannot be read
		# if res.get('value') == 0:
		# 	print(f"ERR: {f}")
		# 	print('===========')
		# 	print(res.get('text'))
		# 	print('===========')
		# else:
		# 	print(f"{res.get('value'):,}")
		

	return res_list


def read_pdf(_path='', filename=''):
	res = []
	df = tabula.read_pdf(f"{_path}/{filename}.pdf", pages="all")
	print(f"Filename: {filename} [{len(df)} pages]")
	
	for i, page in enumerate(df):
		for colName, colData in page.iteritems():
			for e in colData.values:
				if re.search(_patterns, str(e)):
					# print(int(''.join(filter(str.isdigit, str(e)[:-3]))))
					res.append(clean_text(str(e)))
		
	return res


if __name__ == '__main__':
	for month in _month_list:
		print(f"Month: {month.get('img')}")

		# load pdf
		res_pdf = read_pdf(_pdf_dir, month.get('pdf'))
		print(res_pdf)

		# load img
		res_img = read_img(f"{_img_dir}/{month.get('img')}")
		for e in res_img:
			if not e.get('value') in res_pdf:
				print(f"{e.get('value'):,} not found [{e.get('filename')}]")
			else:
				print(f"{e.get('value'):,} checked")

		
		
		
		print('\n\n')


	# TODO: match with bank statement records
	# print('read_pdf')
	# read_pdf(_pdf_dir, month.get('pdf'))
	
	# ==== test single month ====
	# month = _month_list[0]
	# print('read_img')
	# read_img(f"{_img_dir}/{month.get('img')}")

	# ==== test single image ====
	# res = img2text(f"{_img_dir}sep/WhatsApp Image 2021-09-17 at 6.56.03 PM (2).jpeg")
	# print(res)
	