# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 06:20:48 2015

@author: Administrator
"""

import readImages as rimg
import numpy as np

"""
Concatenate two vectos in one

Input: vectorOne,vectorTwo
Output: finalVector
"""    

def concatenateVectors(vectorOne,vectorTwo):
    finalVector = np.concatenate([vectorOne,vectorTwo])
    return finalVector
    
# Dictionary with the configurations used in regions
regionsConfig = dict(
    # Number of Columns
    cols = 2,
    # Numbers of Rows
    rows= 4,
)

# Dictionary with the configurations used in LBP
lbpConfig = dict(
    # Neighbours
    neigh= 8,
    # Radius
    radius = 1,
    # Type LBP
    lbpType='uniform',
)
# Reading images without worn
vectorWithoutWorn,vectorNamesWithoutWorn = rimg.readImages(
                                    "Datasets\Parches Intactas\\",".png")
#print 2len(vectorNoEroded)

# Reading images with worn from path
vectorWorn,vectorNamesWorn = rimg.readImages(
                                    "Datasets\Parches Chipped\\",".png")
                   
vectorWornAux,vectorNamesWornAux = rimg.readImages("Datasets\Parches Big broken\\"
                               ,".png")
vectorWorn = concatenateVectors(vectorWorn,vectorWornAux)
vectorNamesWorn = concatenateVectors(vectorNamesWorn,vectorNamesWornAux)

vectorWornAux,vectorNamesWornAux  = rimg.readImages("Datasets\Parches Con desgaste brillante\\"
                               ,".png")                            
vectorWorn = concatenateVectors(vectorWorn,vectorWornAux)
vectorNamesWorn = concatenateVectors(vectorNamesWorn,vectorNamesWornAux)
                               
vectorWornAux,vectorNamesWornAux  = rimg.readImages("Datasets\Parches Con desgaste oscuro\\"
                               ,".png")
vectorWorn = concatenateVectors(vectorWorn,vectorWornAux)
vectorNamesWorn = concatenateVectors(vectorNamesWorn,vectorNamesWornAux)

                              
vectorWornAux,vectorNamesWornAux  = rimg.readImages("Datasets\Parches Chipped\\"
                               ,".png")
vectorWorn = concatenateVectors(vectorWorn,vectorWornAux)
vectorNamesWorn = concatenateVectors(vectorNamesWorn,vectorNamesWornAux)

# Dictionary with the configurations of vectos used as dataset
vectorsConfig = dict(
    vectorWithoutWorn=vectorWithoutWorn,
    vectorNamesWithoutWorn=vectorNamesWithoutWorn,
    vectorWorn=vectorWorn,
    vectorNamesWorn=vectorNamesWorn,
    classes = 2,
)
