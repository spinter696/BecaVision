# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:34:30 2015

@author: Administrator
"""
import circleDetection as cd
import croppingImages as cropImg

def obtaningLeftBorderImage(image,name,horizontalPatch=None,verticalPatch=None
                            ,inserts=None):
    nHorizontalDivision = cd.findCircles(image,name,cropping=True)

    cropLeftBorderImage = cropImg.cut(200,nHorizontalDivision,image,
                                  name,inserts=inserts)
    return cropLeftBorderImage