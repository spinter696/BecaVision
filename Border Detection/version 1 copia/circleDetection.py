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

Output: circles ( circles found in the image), nVerticalDivision (Division to crop
image)
"""
def findCircles(image, name, path, circles):
   
    # Max and min radius to detect circles
    Rmin = 10
    Rmax = 40

    # Smoothing image applying a median filter with a kernel 5
    image = cv2.medianBlur(image, 5)
    cimg = image.copy()
    
    # Trying to detect circles
    try:
        # Storing all circles detected
        allCircles = cv2.HoughCircles(image,cv2.HOUGH_GRADIENT,1,10,
                                      param1=100,param2=30,minRadius=Rmin,
                                      maxRadius=Rmax)
        allCircles = np.uint16(np.around(allCircles))
    
    except AttributeError:
        allCircles = None

    # If circles are detected
    if(allCircles is not None):
        radioMax = 0
        pos = 0
        j = 1
        for i in allCircles[0,:]:
            # Max radius obtained
            if(i[2] > radioMax):
                radioMax = i[2]
                pos = i

                if(circles[0][0] == 0):
                    j = 0
                else:
                    while(circles[j][0] != 0):
                        j = j + 1
                        circles[j][0] = pos[0]
                        circles[j][1] = pos[1]
                        circles[j][2] = pos[2]
        """
        # Drawing circle
        cimg = cv2.cvtColor(cimg,cv2.COLOR_GRAY2RGB)
        cv2.circle(cimg,(pos[0],pos[1]),pos[2],(0,255,0),3)
        # Drawing center of the circle
        cv2.circle(cimg,(pos[0],pos[1]),2,(0,0,255),3)
        # Mostramos la imagen con el circulo
        #cv2.imshow("detected circles", cimg)
        #cv2.waitKey(0)
        """
        
        # Vertical division that correspond to the center
        # position - radius
        nVerticalDivision = round(pos[0]-pos[2])
    else:
        nVerticalDivision = len(image)/2
    return circles, nVerticalDivision

