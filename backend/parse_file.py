#!/usr/bin/env python

""" Module reads and parses pages in a pdf file """

import sys
import fitz
import json


def readPdfFile(filePath):
    """ reads and returns all lines in a pdf file """
    try:
        with open(filePath, "rb") as file:
            pdfFile = fitz.open(file)

            allLines = []
            for page in pdfFile:
                text = page.get_text("text")
                lines = text.splitlines()
                allLines.extend(lines)

            return allLines

    except FileNotFoundError:
        return [f"Error: {filePath} not found"]


def listToString(list):
    """convert a python list to a string """
    newString=""

    # loop over the list
    for item in list:
        newString += '{} '.format(item)

    return newString

def writeToJson(FilePath, content):
    """ write parsed pdf file to a json file format """
    with open(FilePath, "w") as jsonFile:
        jsonFile.write(content)


def parser():
    """ output point """
    
    # path to file to read
    pdfFilePath = "centers.pdf"
    # jsonFilePath = "parsed.json"

    # call read function
    lines = readPdfFile(pdfFilePath)
    
    # itterate and print each line
    for line in lines:
        allLines = list(line)
        allLines.insert(len(allLines) - len(allLines) + 7, ", ")
        joinedLines = "".join(allLines)
        print(joinedLines)

        """ None of these worked yet for saving to json """
        # convert lines to JSON format
        # jsonData = []
        # charArray = list(joinedLines)
        # jsonData.append({charArray})
        
        # write the JSON data to a file
        # jsonContents = json.dumps(jsonData, indent=2)
        # writeToJson(jsonFilePath, jsonContents)

        """ use command line redirection to save print output to a csv file"""
        # e.g: python parse_file.py > parsed.csv

        """ or call Redirectfile function """
        # e.g: Redirectfile(filePath)
        
    # print number of lines
    print(f"Total Number of Lines in {pdfFilePath} is: {len(lines)}")

def Redirectfile(file):
    sys.stdout = file

if __name__ == '__main__':
    # call main function
    parser()
