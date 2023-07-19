# app.py
import os
import pyfiglet

def create_ascii_art(text, font='standard'):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(ascii_art)

name = os.getenv('USERNAME')
if name:
    create_ascii_art(name, , font="slant")
else:
    print("No name provided. Please set the USERNAME environment variable.")
