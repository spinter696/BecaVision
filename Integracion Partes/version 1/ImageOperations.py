# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 2015

@author: Adrián de las Matas de la Fuente
"""
import os
import cv2

"""
Read the images, convert them to grayscale in the indicated path with a custom
extension and then saving them in a vector

Input: path (where to read images)
type (type of images read, .bmp, .jpg)
grayscale (0 as default auto convert images to gray scale if >0 then read a 
color image if <0 the loaded image as is (with alpha channel))

Output: vectorImages vectorNames
"""

def readImages(path,type,grayscale=0):
    vectorImages = []
    vectorNames = []
    for nameImg in os.listdir(path):
        if nameImg.endswith(type):
            completePath = path + str(nameImg)
            vectorNames.append(nameImg)
            vectorImages.append(cv2.imread(completePath,grayscale))
    return vectorImages,vectorNames
    
"""
Create directories where the different images are going to be stored

Input: pathHome (path where to create directories)
"""
def creatingDirectories(path):
     # Creating directories to store images
        if not os.path.exists(path+'\croppedBorder'):
            os.mkdir(path+'\croppedBorder')
        if not os.path.exists(path+'\inserts'):
            os.mkdir(path+'\inserts')  
        if not os.path.exists(path+'\patches'):
            os.mkdir(path+'\patches')


def saveImage(img,path,name):
    cv2.imwrite(path+name+'.bmp',img)
    
    