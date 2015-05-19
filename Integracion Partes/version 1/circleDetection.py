# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 02:43:27 2015

@author: Adrián de las Matas de la Fuente
"""
import cv2
import numpy as np


"""
Function to detect circles inside an image

Input: image (image where to detect circles), name (name of the image),
path (where to save images), circles (where to store detected circles)
"""
def findCircles(image, name,Rmin=20,Rmax=40,cropping=None,circles=None):
   


    # Smoothing image applying a median filter with a kernel 5
    cimg = image.copy()
    cimg = cv2.cvtColor(cimg,cv2.COLOR_GRAY2RGB)
    image = cv2.GaussianBlur(image,(3,3),0)
    # Trying to detect circles
    try:
        # Storing all circles detected
        allCircles = cv2.HoughCircles(image,cv2.HOUGH_GRADIENT,1,20,
                                      param1=100,param2=30,minRadius=Rmin,
                                      maxRadius=Rmax)
        allCircles = np.uint16(np.around(allCircles))
    
    except AttributeError:
        allCircles = None

    # If circles are detected
    if(allCircles is not None):
        radioMax = 0
        pos = 0
        circle=0
        circles=[]
        for i in allCircles[0,:]:
            # Max radius obtained
            if(cropping==True):
                if(i[2] > radioMax):
                    radioMax = i[2]

            pos = i
            if(cropping==False):
                circles.append([pos[0],pos[1],pos[2]])
                circle = circle + 1
        # Drawing circle
            cv2.circle(cimg,(pos[0],pos[1]),pos[2],(0,255,0),3)
        # Drawing center of the circle
            cv2.circle(cimg,(pos[0],pos[1]),2,(0,0,255),3)
        # Mostramos la imagen con el circulo
        """if(cropping==False):
            cv2.imshow(name, cimg)
            cv2.waitKey(0)
        """
        # Vertical division that correspond to the center
        # position - radius
        nHorizontalDivision = round(pos[0]-pos[2])
    else:
        nHorizontalDivision = len(image)/2
    
    if(cropping==False):
        return circles
    else:
        return nHorizontalDivision

