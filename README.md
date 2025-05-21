# PDF Splitter

A very basic tool for those who wants to split a big PDF file

## Getting started
Install the requirements:
```
pip install -r requirements.txt
```

Split a PDF file:
```
python3 pdf_splitter.py -r pdf_file.pdf 
```


## Arguments
There are 4 possible arguments:

- -r / --read

It receives a PDF file as input

- -w / --write

It receives a folder name as input to where the PDF files will be stored

- -n / --pages interval

It receives a number as input for splitting the file

- --create-zip-file

It does not receive any input. Use it if you want to create a ZIP file with the PDF files. The file name is **pdf_files.zip**

## Usage Examples

1.
```
python3 pdf_splitter.py -r sample.pdf -w my_folder -n 5
```
It will read a PDF file named `sample.pdf`, create a folder named `my_folder` and write the PDF files into it.
The interval 5 means:
- File #1: Pages 1, 2, 3, 4, 5
- File #2: Pages 6, 7, 8, 9, 10
- File #3: Pages 11, 12, 13, 14, 15

2. 
```
python3 pdf_splitter.py -r sample.pdf -n 2 --create-zip-file
```
It will read a PDF file name `sample.pdf`, create a folder named `pdf_files` (default when -w/--write is not used) and crate a ZIP file named `pdf_files.zip` with the PDF files into it.


