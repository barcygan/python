#!/usr/bin/env python
# coding: utf-8

# connecting to tinyjpg API

import tinify
tinify.key = "594lphSHLsCFvsqBSQBG29sX0yTjRNmL"


from pathlib import Path
#print("File      Path:", Path(__file__).absolute())
#print("Directory Path:", Path().absolute())  


# getting current files path 
# creating list of files elements in forlder
import os
files = os.listdir(Path().absolute())
JPG_files = [_ for _ in files if _[-4:] == ".JPG"]


# compressing files and save as 'compressed' + filename
for element in JPG_files:

    source = tinify.from_file(element)
    source.to_file('compressed'+element)

