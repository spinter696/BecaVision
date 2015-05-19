# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23  2015
@author: Adrián de las Matas de la Fuente

This script compute the different regions of an image given the image,
a number of comlums n and a number of rows m.

Input: img = image , n = colums, m=rows
Output: regions= vector with the diferrent regions of the image given before
"""
from matplotlib import pyplot as plt

def computingRegions(img,n,m):

    # Dimensions of the image
    sizeX = img.shape[0]
    sizeY = img.shape[1]
    #print sizeX,sizeY
    # Tam of Y region
    regionY=sizeY/n
    #print regionY
    # Tam of X region 
    regionX = sizeX/m
    #print regionX
    # Tam of Y region
    regionY = sizeY/n

    # Total of regions
    totalRegions = n* m
    
    # Array with regions
    regions = []

    # Compute the diferent regions of the image
    for v in range (0,totalRegions):
        if v != totalRegions-1:
        
            """
            print "principio Region",0+(regionX*(v%mCols))
            print "principio region y", 0+ regionY*(v%nRows)
            print "finalRegion",regionX + (regionX*(v%mCols))
            print "final REgion y", regionY +regionY*(v%nRows)
            """
            
            regions.append(img[0+(regionX*(v%m)) : regionX + (regionX*(v%m)) ,
                                0+ regionY*(v/m) : regionY +regionY*(v/m)])
                                
            """
            cv2.imshow('parte',img[0+(regionX*(v%mCols)) : regionX + (regionX*(v%mCols)) ,
                                0+ regionY*(v/mCols) : regionY +regionY*(v/mCols)])
            cv2.waitKey(0)
            """
            
        else:
            regions.append(img[0+(regionX*(v%m)) : sizeX ,
                                0+ (regionY*(v/m)) : sizeY])
                                
            """
            cv2.imshow('parte',img[0+(regionX*(v%mCols)) : regionX + (regionX*(v%mCols)) ,
                                0+ regionY*(v/mCols) : regionY +regionY*(v/mCols)])
            cv2.waitKey(0)
            """



    return regions
    
def plotRegiones(regiones):
        # Plotting all regions
    plt.subplot(4,2,1),plt.imshow(regiones[0],cmap='gray',interpolation='bicubic')
    plt.subplot(4,2,3),plt.imshow(regiones[1],cmap='gray',interpolation='bicubic')
    plt.subplot(4,2,5),plt.imshow(regiones[2],cmap='gray',interpolation='bicubic')
    plt.subplot(4,2,7),plt.imshow(regiones[3],cmap='gray',interpolation='bicubic')
    plt.subplot(4,2,2),plt.imshow(regiones[4],cmap='gray',interpolation='bicubic')
    plt.subplot(4,2,4),plt.imshow(regiones[5],cmap='gray',interpolation='bicubic')
    plt.subplot(4,2,6),plt.imshow(regiones[6],cmap='gray',interpolation='bicubic')
    plt.subplot(4,2,8),plt.imshow(regiones[7],cmap='gray',interpolation='bicubic')
    plt.show()