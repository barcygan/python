#!/usr/bin/env python
# coding: utf-8


#Python Script that uses tinyjpg.com compression via API. Put the script in folder with .jpg files and run script inside in Python environment.


import tinify
import os
from pathlib import Path

# connecting to tinyjpg API
tinify.key = "594lphSHLsCFvsqBSQBG29sX0yTjRNmL"


#print("File      Path:", Path(__file__).absolute())
#print("Directory Path:", Path().absolute())  




# getting current files path 
files = os.listdir(Path().absolute())

# creating list of files elements in forlder
JPG_files = [_ for _ in files if _[-4:] == ".JPG"]



# compressing files and save as 'compressed' + filename
for element in JPG_files:

    source = tinify.from_file(element)
    source.to_file('compressed'+element)

