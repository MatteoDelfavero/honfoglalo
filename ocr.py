# Matteo Delfavero jan.2019
# honfoglalo.hu

from time import gmtime, strftime
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image
import pytesseract
import pyautogui
import requests
import os

# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

debug = 1

def log(question, answer, filename):
    print(filename)
    string = filename + "\nQuestion:\n\n\"" + question + "\"\n\nAnswer: \n\n\"" + answer + "\"\n\n\n"
    if debug:
        print("debugmode")
        with open('log/log.txt', 'a', encoding='utf-8') as file:
            file.writelines(string)

    print(string)

def OCRimage():
    #         (x,   y,  width,  height)
    pos = (185, 720, 955, 200)
    filename = "honfoglalo " + strftime("%Y-%m-%d %H_%M_%S", gmtime()) + ".jpg"
    return pytesseract.image_to_string(pyautogui.screenshot(imageFilename="log/" + filename, region=(pos))), filename

def main(args):
    keyword = args[0]
    filename = args[1]
    google_search = "https://www.google.co.in/search?client=ubuntu&channel=fs&biw=748&bih=875&source=hp&ei=Ugc4XOStLc7CwQK4jbmACg&q=" + keyword
    url = BeautifulSoup(requests.get(google_search).text, "html.parser").findAll('span', {"class":"st"})

    for u in url:
        log(keyword, u.text, filename)
        break

if __name__ == '__main__':
    main(OCRimage())
