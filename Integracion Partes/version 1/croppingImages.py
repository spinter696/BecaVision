# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 03:35:14 2015

@author: Adrián de las Matas de la Fuente
"""

def cut(x, y, img, name,inserts=True,
        verticalPatch=None,horizontalPatch=None):
    #200,dim,img,0,name,path
    # Recortamos la imagen desde 0 a 200 ya que es el tamaño en vertical de
    # la imagen y de 0 a nLineaVertical

    try:
        if inserts==True:
            horizontalLeftBorder= y - horizontalPatch
            horizontalRigthBorder= y + horizontalPatch
            verticalTopBorder= x - verticalPatch
            verticalBotBorder= x + verticalPatch
            cropImg = img[horizontalLeftBorder:horizontalRigthBorder,
                          verticalTopBorder:verticalBotBorder]
        else:
            cropImg = img[0:x,0:y] # Crop [y1:y2, x1:x2]
            
        
        #cv2.imshow("copped img", cropImg)
        #cv2.waitKey(0)
    except AttributeError:
        print "not a valid image to crop"
        
    return cropImg