from PIL import Image
import pytesseract

import argparse
import sys
import os

def run_ocr(file_name):
    return pytesseract.image_to_string(Image.open(file_name))
def write_file(file_name, text):
    with open(file_name, 'w') as f:
        f.write(text)
def is_image(file_name):
    accepted_files = ["jpg","png"]
    extension = file_name.split(".")[0]
    is_accepted = [_ for _ in accepted_files if _.lower() == extension.lower()]

    return len(is_accepted) == 0
if __name__ == "__main__":
    if sys.argv[1]:
        file_name = sys.argv[1]
        if is_image(file_name):
            text = run_ocr(sys.argv[1])
            text_file_name = file_name.split(".")[0] + ".txt"
            write_file(text_file_name, text)
    else:
        print("No filename was provided. It should be the first argument in the script")
