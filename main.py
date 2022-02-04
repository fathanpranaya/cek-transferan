from os import walk
import cv2
import pytesseract
import re

__input_dir = 'input/'
__patterns = r'([0-9]{3}\.[0-9]{3})|([0-9]{3}\,[0-9]{3})'

# list all filenames inside __input_dir 
filenames = next(walk(__input_dir), (None, None, []))[2]  # [] if no file

# process all images inside __input_dir 
for f in filenames:
	# image2text processing
	img = cv2.imread(f"{__input_dir}/{f}")
	text = pytesseract.image_to_string(img)
	
	# pattern matching
	nominal = ''
	for e in text.split():
		if re.search(__patterns, e):
			nominal = e
	

	res = {
		'filename': f,
		'nominal': nominal
	}

	print(res)

