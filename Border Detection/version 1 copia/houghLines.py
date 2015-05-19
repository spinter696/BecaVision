# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:31:17 2015

@author: Adrián de las Matas de la Fuente
"""

import cv2
import numpy as np

"""
Detect lines of an image and draw the weightest one

Input: img (image), name (name of the image), path (path
where to save images with lines drawed)
"""
def detectLines(img,name,path):
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img,30,45)
    

    #edges = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=1)  
    lines = cv2.HoughLines(edges,1,np.pi/180,50)
    
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)  

    #print lines
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
    
        cv2.line(cimg,(x1,y1),(x2,y2),(0,0,255),3)
        
    """
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(255),3)
    """        

    
    cv2.imwrite(path+'\HoughLines\HoughLines'+name,cimg)

    """cv2.imshow('houghlines3.jpg',img)
    cv2.waitKey(0)"""