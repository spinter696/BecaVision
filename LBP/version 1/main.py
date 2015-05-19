# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04  2015

@author: Adrián de las Matas de la Fuente
"""
import cv2
import regiones as rg
import calculo_LBP as Clbp

# Number of Columns
n = 2

# Numbers of Rows
m = 4

# Neighbours
p=8

# Radius
r=1

# Type LBP
lbpType='ror'

# Reading image
img = cv2.imread('0007c.bmp',0)

# calculating regions of the image 
regions = rg.computingRegions(img,n,m)

# Calculating lbp values
lbp = Clbp.computingLBP(regions[0],p,r,lbpType)

# Plotting lbp
Clbp.plotHistogram(lbp,p)

print regions