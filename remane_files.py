"""
    I made this file to remane the image files
    I made it because I took the images from another dataset, so when I copied the files
    the files are named with numbers that are not in order and I want to be in order
    starting from zero, one, two and so on...
"""

import os


imageFiles = os.listdir("./images")
index = 0
for fileIndex, imageFile in enumerate(imageFiles):
    newFileName = "./images/" + str(fileIndex) + ".jpg"
    oldFileName = "./images/" + imageFile
    os.rename(oldFileName, newFileName)
    