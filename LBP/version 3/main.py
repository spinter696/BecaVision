# -*- coding: utf-8 -*-
"""
Created on Wed Feb 04  2015

@author: Adrián de las Matas de la Fuente
"""
import Calculo_LBP as clbp
import svm as svm
import numpy as np
import configFile as cfg
from sklearn import metrics
import ROCPrecisionRecall as curves
"""
Concatenate two vectos in one

Input: vectorOne,vectorTwo
Output: finalVector
"""    

def concatenateVectors(vectorOne,vectorTwo):
    finalVector = np.concatenate([vectorOne,vectorTwo])
    return finalVector
    
                                                             
"""
#calculating regions of the image 
#regions = rg.computingRegions(vector[0],cols,rows)
#Calculating lbp values
lbp = clbp.computingLBP(vector[0],neigh,radius,lbpType)
# Plotting lbp
clbp.plotHistogram(lbp,neigh)
"""

#Classes of our dataset
n_classes = cfg.vectorsConfig['classes']
# Compute train,test,label,and name vector to worn Images
WornTrainVector,WornTestVector,WornLabelsVector,WornNamesVector = svm.vectorsOfTraingTestTags(
                                                            cfg.vectorsConfig['vectorWorn'],
                                                            "Worn piece",
                                                            cfg.vectorsConfig['vectorNamesWorn'])
WornTestlength = len (WornTestVector)
                                                            
# # Compute train,test,label,and name vector to Non Eroded Images                                                            
NWornTrainVector,NWornTestVector,NWornLabelsVector,NWornNamesVector = svm.vectorsOfTraingTestTags(
                                                            cfg.vectorsConfig['vectorWithoutWorn'],
                                                            "Without Worn piece",
                                                            cfg.vectorsConfig['vectorNamesWithoutWorn'])
NWornTestlength = len (NWornTestVector)
                                                            
#print len(EtestVector),len(NEtestVector)

# Creating final vector                                                         
finalTrainVect = []
finalTrainVect = concatenateVectors(WornTrainVector,NWornTrainVector)

finalTestVect = []
finalTestVect = concatenateVectors(WornTestVector,NWornTestVector)

finalTagsVect = []
finalTagsVect = concatenateVectors(WornLabelsVector,NWornLabelsVector)

testVectorNames = []
testVectorNames = concatenateVectors(WornNamesVector,NWornNamesVector)

# Vector that contains the LBP values of the traning images
lbpFinalTrainVect = []
lbpFinalTrainVect = clbp.getDescriptorValues(finalTrainVect,cfg.lbpConfig['neigh'],
                                             cfg.lbpConfig['radius'],
                                             cfg.lbpConfig['lbpType'])

# Train a svm
clf = svm.computeSvm(lbpFinalTrainVect,finalTagsVect)

# Vector that contains the LBP values of the test images
lbpFinalTestVect=[]
lbpFinalTestVect=clbp.getDescriptorValues(finalTestVect,cfg.lbpConfig['neigh'],
                                             cfg.lbpConfig['radius'],
                                             cfg.lbpConfig['lbpType'])
                                             
                                             
# Predict all the test image with the svm trained
predictedValues = svm.classify(clf,lbpFinalTestVect)
probaPredictedValues = svm.predictProba(clf,lbpFinalTestVect)
predictedValuesBinary = []

# Translate predicted values in string to binary
for i in range (0,len(predictedValues)):
    if (predictedValues[i] == "Worn piece"):
        predictedValuesBinary.append(0)
    else:
        predictedValuesBinary.append(1)

# Real values of predicted sets
realLabelsBinary = []
realLabelsString = []

for i in range (0,len(predictedValues)):
    if (i <= WornTestlength):
        realLabelsString.append("Worn piece")
        realLabelsBinary.append(0)
    else:
        realLabelsString.append("Without Worn piece")
        realLabelsBinary.append(1)


# Precision,recall and average_precision
precision = dict()
recall = dict()
average_precision = dict()

# For all classes we have in sets
for i in range (0,n_classes):
    
    #Obtain the precision and recall values
    precision[i],recall[i]= curves.precisionRecallValues(precision,
                                recall,realLabelsBinary,
                                probaPredictedValues[:,i])
                                
    #Obtain the average precision values
    average_precision[i] = curves.areaUnderPrecisionRecallCurve(average_precision,  
                                                  realLabelsBinary,
                                                  probaPredictedValues[:,i])

# Plot the precision recall curves for each class
for i in range(n_classes):
    curves.plotPrecisionRecallCurve(i,recall[i], precision[i],
                                    average_precision[i])

# Computing the false positive rate and true positive rate to make ROC curve
fpr,tpr,thresholds=curves.rocCurveValues(realLabelsBinary,
                                         probaPredictedValues[:,0])
# The area under the curve ROC                                         
roc_auc = curves.areaUnderCurves(fpr,tpr)
print "Area under the ROC curve : %f" % roc_auc
# Plotting the curve
curves.plotROCCurve(fpr,tpr,roc_auc)

# Computing the false positive rate and true positive rate to make ROC curve
fpr,tpr,thresholds=curves.rocCurveValues(realLabelsBinary,
                                         probaPredictedValues[:,1])
# The area under the curve ROC                                         
roc_auc = curves.areaUnderCurves(fpr,tpr)
print "Area under the ROC curve : %f" % roc_auc
# Plotting the curve
curves.plotROCCurve(fpr,tpr,roc_auc)

# Printing values of precision recall and fscore for each class
print metrics.precision_recall_fscore_support(realLabelsBinary,
                                              predictedValuesBinary)


# Printing values of precision recall and fscore globally
print metrics.precision_recall_fscore_support(realLabelsBinary,
                                              predictedValuesBinary
                                              ,average='micro')

#print "metrics media",metrics.accuracy_score(predictedValues,realLabelsString)


