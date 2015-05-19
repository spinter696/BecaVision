# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 03:35:14 2015

@author: Administrator
"""
import cv2


"""
Cut the image to create a new one with the left side of the insert

Input: x , y (coordinates to make the crop image), img (original image)
name ( name of the image ), path (path to the image)

Output: cropImg (cropped image)
"""
def cut(x, y, img, name, path):
    #200,dim,img,0,name,path
    # Recortamos la imagen desde 0 a 200 ya que es el tamaño en vertical de
    # la imagen y de 0 a nLineaVertical
    cropImg = img[0:x,0:y] # Crop [y1:y2, x1:x2]

    cv2.imwrite(path+'\Cropped\cropped'+name,cropImg)

    return cropImg