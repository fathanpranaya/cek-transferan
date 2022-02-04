# cek-transferan
Cek bukti transferan dari screenshot atau foto dan mutasi bank

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](#)

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