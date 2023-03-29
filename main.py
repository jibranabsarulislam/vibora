# if you are on windows, download Poppler and add it to PATH
# refer to https://github.com/oschwartz10612/poppler-windows/releases/ to get the latest version

from pdf2image import convert_from_path, convert_from_bytes
import os
import time
import sys
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
    PDFPopplerTimeoutError
)

def pdf_to_png(pdf_path):
  # example: images = convert_from_path(r'C:/path/to/file.pdf')
  images = convert_from_path(pdf_path)
  for i in range(len(images)):
    # this is the name of converted file. change that later, too weird a file always called page[number]
    images[i].save('page' + str(i) + '.png')

if __name__ == '__main__':
  # case we type python main.py
  if len(sys.argv) == 1:
    print("Unknown command, see `python main.py help` for reference on how to use it!")
  # case we type python main.py help
  elif sys.argv[1].lower() == 'help':
    print('\nWelcome to vibora :) A PDF tool that lets you convert a PDF to PNG, PDF to text, plus some more awesome things!\n\nPDF TO PNG:\nto convert a .PDF to .PNG, use: python main.py pdf2png file.pdf')
    exit()
  # case we actually pass a valid argument
  else:
    command = sys.argv[1].lower()
    # e.g. python main.py pdf2png | note that it also expects a file! -> python main.py pdf2png file.pdf
    if command == 'pdf2png':
      pdf_path = sys.argv[2]
      print("converting")
      pdf_to_png(pdf_path)
      time.sleep(2)
      print('file converted!')