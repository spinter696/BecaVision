# -*- coding: utf-8 -*-
import readImages as rdimgs
import houghLines as hl
import circleDetection as cd
import croppingImages as cropImg
import SobelAndCannyBorders as SobelCannyBord

"""
@author: Adrián de las Matas de la Fuente
"""

def main():
    
    # parth where to load images
    pathHome = "C:\Documents and Settings\Administrator\Desktop\InsertsFromHeadTools\\"
    # creating images where to save images    
    rdimgs.creatingDirectories(pathHome)
        
    # Variables to stores images an images names
    images = []
    imagesNames = []
    # reading images and names
    images,imagesNames=rdimgs.readImages(pathHome,'.bmp')
    
    # total number of images
    numImages = len(images)
    
    # arry to store circles detected 3 values to each image, pixel x and y
    # of detected center circle and the radius
    circles = [ [ 0 for i in range(3) ] for j in range(numImages*2) ]
    
    if(numImages != 0):    
        for i in range(numImages):
        
            image=images[i]
            name=imagesNames[i]
            # converting to uint8
            
            circles,nVerticalDivision = cd.findCircles(image,name,
                                          pathHome,circles)

            cropImage = cropImg.cut(200,nVerticalDivision,image,
                                  name,pathHome)
            """
            Detecting lines by Hough
            """
            #img_adapteq=exposure.equalize_adapthist(cropImg)
            hl.detectLines(cropImage,name,pathHome)
            
            #SobelCannyBord.edgeDetection(cropImage,
            #                             name,pathHome)

if __name__ == "__main__":
    main()    
