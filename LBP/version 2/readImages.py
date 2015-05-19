# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 2015

@author: Adrián de las Matas de la Fuente
"""
from os import listdir
import cv2

"""
Read the images in the indicated path with a custom extension and
then saving them in a vector
"""

def readImages(path,type):
    vectorImages = []
    vectorNames = []
    for nameImg in listdir(path):
        if nameImg.endswith(type):
            completePath = path + str(nameImg)
            vectorNames.append(nameImg)
            vectorImages.append(cv2.imread(completePath,0))
    return vectorImages,vectorNames

