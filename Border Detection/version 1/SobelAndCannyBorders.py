# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 04:00:00 2015

@author: Adrián de las Matas
"""
import cv2
import numpy as np

def edgeDetection(cropImg,name,path):

    # Apply a Canny to the crop Img
    edges = cv2.Canny(cropImg,0,100)
    
    #cpy img
    canny =  edges.copy()
    # Kernel to apply dilation to canny
    kernel = np.ones((3,3),np.uint8)
    
    """
    (thresh, canny) = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY)
    """
       	 
    # Dilating image to see borders clearer
    cv2.fastNlMeansDenoising(canny, canny, 3, 7, 21)
    dilation = cv2.dilate(canny,kernel,iterations = 1)
    
    # Storing canny edges images
    cv2.imwrite(path+'\CannyEdges\CannyEdges'+name,dilation)

    # Parameters to use Sobel filter
    scale = 5
    delta = 0
    ddepth = cv2.CV_16S

    # X_Sobel
    grad_x = cv2.Sobel(cropImg,ddepth,1,0,ksize = 3, scale = scale,
                       delta = delta,borderType = cv2.BORDER_DEFAULT)
    edges = cv2.convertScaleAbs(grad_x)
    
    (thresh, sobel) = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    cv2.fastNlMeansDenoising(edges, edges, 3, 7, 21)
    # Dilating sobel
    dilation = cv2.dilate(sobel,kernel,iterations = 1)
    # Storing images
    cv2.imwrite(path+'\SobelEdges\SobelEdges'+name,dilation)
    

 