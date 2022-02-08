# cek-transferan
Cek bukti transferan dari screenshot atau foto dan mutasi bank

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](#)

## Config
1. Put the bank statement file (currently only supports mandiri) into "input_pdf" directory
2. Put the screenshot or photo of bukti transfer grouped by month into "input" directory
3. Link the month directory and the name of bank statement with the following json format in config.py
```python
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
```

## Install
1. Create environment variables
```shell
$ python -m venv venv
$ source venv/bin/activate
```
2. Install dependencies
```shell
$ sudo apt-get update
$ sudo apt-get install tesseract-ocr
$ sudo apt-get install libtesseract-dev
$ pip install -U git+https://github.com/madmaze/pytesseract.git
$ pip install -r requirements.txt
```
3. Run
```shell
$ python main.py
```
4. Example output:
```
Month: sep
Filename: 2021_09_ENDORS [11 pages]
2,300,001 not found [input//sep/WhatsApp Image 2021-09-07 at 11.36.53 AM.jpeg]
1,600,051 checked
2,306,512 not found [input//sep/WhatsApp Image 2021-09-07 at 11.36.54 AM.jpeg]
1,206,502 not found [input//sep/WhatsApp Image 2021-09-07 at 11.36.55 AM (1).jpeg]
1,000,011 checked
1,000,008 checked
5,100,012 checked
1,000,011 checked
1,000,015 checked
1,000,015 checked
1,600,012 not found [input//sep/WhatsApp Image 2021-09-17 at 6.56.04 PM (2).jpeg]
1,000,019 not found [input//sep/WhatsApp Image 2021-09-17 at 6.56.04 PM.jpeg]
1,600,016 not found [input//sep/WhatsApp Image 2021-09-17 at 6.56.05 PM.jpeg]
2,300,034 not found [input//sep/WhatsApp Image 2021-09-28 at 11.15.18 AM (1).jpeg]
1,000,009 not found [input//sep/WhatsApp Image 2021-09-28 at 11.15.18 AM.jpeg]
1,000,007 checked
2,300,008 checked
3,500,007 checked
```