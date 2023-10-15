#!/usr/bin/env python

""" Module reads and parses pages in a pdf file """

import fitz


def read_pdf_file(file_path):
    """ reads and returns all lines in a pdf file """
    try:
        with open(file_path, "rb") as file:
            pdf_file = fitz.open(file)

            all_lines = []
            for page in pdf_file:
                text = page.get_text("text")
                split_lines = text.splitlines()
                all_lines.extend(split_lines)

            return all_lines

    except FileNotFoundError:
        return [f"Error: {file_path} not found"]


# path to file to read
pdf_file_path = "pdf_file.pdf"

# call read function
lines = read_pdf_file(pdf_file_path)

# itterate and print each line
for line in lines:
    print(line)

#print number of lines
print (f"total_lines: {len(lines)}")
