# Matteo Delfavero jan.2019
# honfoglalo.hu

from time import gmtime, strftime
from bs4 import BeautifulSoup
from pynput import mouse
from pathlib import Path
from PIL import Image
import pytesseract
import pyautogui
import requests
import time
import os

# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
clear = lambda: os.system('cls')
debug = 1

def log(question, answer, filename):
    string = filename + "\nQuestion:\n\n\"" + question + "\"\n\n\nAnswer: \n\n\"" + answer + "\"\n--------------------------------------------------------------\n\n"
    if debug:
        with open('log/log.txt', 'a', encoding='utf-8') as file:
            file.writelines(string)
    print(string)

def OCRimage():
    pos = (raw_pos.pressed[0], raw_pos.pressed[1], raw_pos.released[0] - raw_pos.pressed[0], raw_pos.released[1] - raw_pos.pressed[1])
    filename = "honfoglalo " + strftime("%Y-%m-%d %H_%M_%S", gmtime()) + ".jpg"
    return pytesseract.image_to_string(pyautogui.screenshot(imageFilename="log/" + filename, region=(pos)), lang='hun'), filename

def main(args):
    keyword = args[0]
    filename = args[1]
    google_search = "https://www.google.co.in/search?q=" + keyword
    url = BeautifulSoup(requests.get(google_search).text, "html.parser").findAll('span', {"class":"st"})

    for u in url:
        log(keyword, u.text, filename)
        break

class raw_pos():
    pressed = [0, 1]
    released = [3, 4]

def on_click(x, y, button, pressed):
    if button == button.middle:
        if pressed:
            raw_pos.pressed[0] = x
            raw_pos.pressed[1] = y
        else:
            raw_pos.released[0] = x
            raw_pos.released[1] = y
            print("Area selected: ", raw_pos.pressed[0], raw_pos.pressed[1], raw_pos.released[0] - raw_pos.pressed[0], raw_pos.released[1] - raw_pos.pressed[1])


    if button == button.right:
        if pressed:
            pass
        else:
            clear()
            pos = (raw_pos.pressed[0], raw_pos.pressed[1], raw_pos.released[0] - raw_pos.pressed[0], raw_pos.released[1] - raw_pos.pressed[1])
            main(OCRimage())

if __name__ == '__main__':
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    #main(OCRimage())
