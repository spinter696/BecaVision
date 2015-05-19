# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 10:28:37 2015

@author: Adrian de las Matas de la Fuente
"""

headToolImagesSettings = dict (
    # Path where to read imgs
    readPath = 'C:\Documents and Settings\Administrator\Desktop\images\\',
    # Images extension
    extension = '.bmp'
)

directoriesToSaveImgs = dict (

     # Path where to save inserts
     insertsPath = 'C:\Documents and Settings\Administrator\Desktop\inserts\\',
     # Path where to save border imgs
     leftBorderPath = 'C:\Documents and Settings\Administrator\Desktop\croppedBorder\\',
     # Path where to save crop imgs
     patchesPath = 'C:\Documents and Settings\Administrator\Desktop\patches\\'
     
)

insertImagesSettings = dict ( 
    # size for vertical Insert
    sizeVerticalInsert = 100,
    
    # size for horizontal Insert
    sizeHorizontalInsert = 100,
    
    # min radius to detect screws in inserts
    minRadius = 20,
    
    # max radius to detect screws in inserts
    maxRadius = 40
)

borderDetectionSettings = dict (
    # min radius to detect screws in one inserts
    minRadius = 20,
    
    # max radius to detect screws in one inserts
    maxRadius = 40
)

houghLinesSettings = dict(
    # canny thresholds
    cannyThresholdOne = 30 ,
    cannyThresholdTwo = 45 ,
    
    # HoughLines function's threshold
    houghThreshold = 50 ,
)

regionSettings = dict(

    # Number of Columns
    cols = 2,
    
    # Numbers of Rows
    rows= 4,
)

LBPSettings = dict (
    # Neighbours
    neigh= 8,
    # Radius
    radius = 1,
    # Type LBP
    lbpType='uniform',
)

SVMSettings = dict(
    trainingSize = 1,
    classes = 2,
    kernelType = 'linear',
    probability = True
)

wornImages = dict(
    # Path where to read images
    wornPath = 'C:\Documents and Settings\Administrator\Desktop\WornWithouWornDataset\WornPatches\\',
    # Images extension
    extension = '.png'
)

withoutWornImages = dict (
    # Path where to read images
    withoutWornPath = 'C:\Documents and Settings\Administrator\Desktop\WornWithouWornDataset\WithouWornPatches\\',
    
    # images extension
    extension = '.png'
)