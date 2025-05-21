from PyPDF2 import PdfReader, PdfWriter
from zipfile import ZipFile
import argparse
import os


def arguments_parser():
    """
        Use the library argparse to parse the arguments
        There are 4 possible arguments:
        -r / --read <<< THIS ONE IS MANDATORY
        -w / --write
        -n / --pages_interval
        --create-zip-file
    """
    parser = argparse.ArgumentParser(description='PDF Splitter')
    parser.add_argument('-r', '--read', metavar="<file_path>", type=str, help='PDF file to be read. e.g., sample.pdf', required=True)
    parser.add_argument('-w', '--write', metavar="<folder_name>", type=str, help='Folder destination to store the PDF files. e.g., pdf_files', default="pdf_files")
    parser.add_argument('-n', '--pages_interval', metavar="<number_of_pages_interval>", type=int, help="Number of pages to store in each PDF file")
    parser.add_argument('--create-zip-file', '-z', action='store_true', help='Create a ZIP file with the PDF files', default=True)
    try:
        return parser.parse_args()
    except Exception as e:
        print(e)
        exit()


def open_pdf_file(pdf_file):
    """
        Use the library PyPDF2 to read PDF files
        The function returns a variable named reader with the PDF content
    """
    try:
        reader = PdfReader(pdf_file)
    except Exception as error_read_file:
        print(f'Failure while opening the PDF file. Error: {error_read_file}')
        exit()
    return reader


def walk_pdf_file(reader, num_pages):
    """
        Walk throught every page in the PDF file to split the pages according to the user's demand
        For a split for 2 pages, it will create files as:
        File #1: Pages 1, 2
        File #2: Pages 3, 4
        File #3: Pages 5, 6
        etc
    """
    os.makedirs(output_folder, exist_ok=True)
    for page in range(0, len(reader.pages), num_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[page])

        if page + 1 < len(reader.pages):
            writer.add_page(reader.pages[page + 1])
        
        file_path = os.path.join(output_folder, f"file_{page}.pdf")

        with open(file_path, "wb") as file_writer:
            writer.write(file_writer)
        
        files_list.append(file_path)


def create_zip_file():
    """
        This function will only be called if user uses the flag --create-zip-file / -z
        It will create a ZIP file named pdf_files.zip with the splitted PDF files
    """
    with ZipFile("pdf_files.zip", "w") as zip_creator:
        for file_path in files_list:
            zip_creator.write(file_path, os.path.basename(file_path))



if __name__ == '__main__':
    # List used to stored the splitted PDF files
    files_list = []
    
    # Store the arguments into vars
    args = arguments_parser()
    input_pdf_file = args.read
    output_folder = args.write
    num_pages = args.pages_interval
    
    reader = open_pdf_file(input_pdf_file)
    walk_pdf_file(reader, num_pages)
    if args.create_zip_file:
        create_zip_file()
