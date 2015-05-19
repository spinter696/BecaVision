# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04  2015

@author: Adrián de las Matas de la Fuente
"""
import Calculo_LBP as clbp
import readImages as rimg
import svm as svm
import numpy as np

    
"""
Concatenate two vectos in one

Input: vectorOne,vectorTwo
Output: finalVector
"""    

def concatenateVectors(vectorOne,vectorTwo):
    finalVector = np.concatenate([vectorOne,vectorTwo])
    return finalVector
    

# Number of Columns
cols = raw_input("Introduzca el numero de columnas:")
cols = int(cols)
# Numbers of Rows
rows = raw_input("Introduzca el numero de filas:")
rows= int(rows)

# Neighbours
neigh = raw_input("Introduzca el numero de vecinos:")
neigh= int (neigh)

# Radius
radius = raw_input("Introduzca el radio:")
radius = int(radius)

# Type LBP
lbpType='ror'
# Reading images non eroded

vectorNonEroded,vectorNamesNonEroded = rimg.readImages(
                                    "Datasets\Parches Intactas\\",".png")
#print 2len(vectorNoEroded)

# Reading images eroded
vectorEroded,vectorNamesEroded = rimg.readImages(
                                    "Datasets\Parches Chipped\\",".png")
                   
vectorErodedAux,vectorNamesErodedAux = rimg.readImages("Datasets\Parches Big broken\\"
                               ,".png")
vectorEroded = concatenateVectors(vectorEroded,vectorErodedAux)
vectorNamesEroded = concatenateVectors(vectorNamesEroded,vectorNamesErodedAux)

vectorErodedAux,vectorNamesErodedAux = rimg.readImages("Datasets\Parches Con desgaste brillante\\"
                               ,".png")                            
vectorEroded = concatenateVectors(vectorEroded,vectorErodedAux)
vectorNamesEroded = concatenateVectors(vectorNamesEroded,vectorNamesErodedAux)
                               
vectorErodedAux,vectorNamesErodedAux = rimg.readImages("Datasets\Parches Con desgaste oscuro\\"
                               ,".png")
vectorEroded = concatenateVectors(vectorEroded,vectorErodedAux)
vectorNamesEroded = concatenateVectors(vectorNamesEroded,vectorNamesErodedAux)

                              
vectorErodedAux,vectorNamesErodedAux = rimg.readImages("Datasets\Parches Chipped\\"
                               ,".png")
vectorEroded = concatenateVectors(vectorEroded,vectorErodedAux)
vectorNamesEroded = concatenateVectors(vectorNamesEroded,vectorNamesErodedAux)
                                                             
#print len(vectorEroded)

"""
#calculating regions of the image 
#regions = rg.computingRegions(vector[0],cols,rows)
#Calculating lbp values
lbp = clbp.computingLBP(vector[0],neigh,radius,lbpType)
# Plotting lbp
clbp.plotHistogram(lbp,neigh)
"""


# Compute train,test,tags,and name vector to Eroded Images
EtrainVector,EtestVector,EtagsVector,EnamesVector = svm.vectorsOfTraingTestTags(vectorEroded,
                                                            "Eroded piece",vectorNamesEroded)
Etestlength = len (EtestVector)
                                                            
# # Compute train,test,tags,and name vector to Non Eroded Images                                                            
NEtrainVector,NEtestVector,NEtagsVector,NEnamesVector = svm.vectorsOfTraingTestTags(vectorNonEroded,
                                                            "Non Eroded piece",vectorNamesNonEroded)
NEtestlength = len (NEtestVector)
                                                            
#print len(EtestVector),len(NEtestVector)

# Creating final vector                                                         
finalTrainVect = []
finalTrainVect = concatenateVectors(EtrainVector,NEtrainVector)

finalTestVect = []
finalTestVect = concatenateVectors(EtestVector,NEtestVector)

finalTagsVect = []
finalTagsVect = concatenateVectors(EtagsVector,NEtagsVector)

testVectorNames = []
testVectorNames = concatenateVectors(EnamesVector,NEnamesVector)

# Vector that contains the LBP values of the traning images
lbpFinalTrainVect = []
lbpFinalTrainVect = clbp.getDescriptorValues(finalTrainVect,neigh,radius,lbpType)

# Train a svm
clf = svm.computeSvm(lbpFinalTrainVect,finalTagsVect)

# Vector that contains the LBP values of the test images
lbpFinalTestVect=[]
lbpFinalTestVect=clbp.getDescriptorValues(finalTestVect,neigh,radius,lbpType)

# Predict all the test image with the svm trained
predictedValues = svm.classify(clf,lbpFinalTestVect)
total = 0
for i in range (0,len(predictedValues)):
    if (i <= Etestlength):
        if (predictedValues[i] == "Eroded piece" ):
            total = total + 1
    else:
        if (predictedValues[i]== "Non Eroded piece"):
            total = total + 1
    
    print predictedValues[i], testVectorNames[i] 

#print total,(Etestlength+NEtestlength)
print float(float(total*100)/float(Etestlength+NEtestlength))
