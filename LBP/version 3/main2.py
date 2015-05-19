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
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
import ROCPrecisionRecall as curves
"""
Concatenate two vectos in one

Input: vectorOne,vectorTwo
Output: finalVector
"""    

def concatenateVectors(vectorOne,vectorTwo):
    finalVector = np.concatenate([vectorOne,vectorTwo])
    return finalVector
    
                                                             
#print len(vectorEroded)

"""
#calculating regions of the image 
#regions = rg.computingRegions(vector[0],cols,rows)
#Calculating lbp values
lbp = clbp.computingLBP(vector[0],neigh,radius,lbpType)
# Plotting lbp
clbp.plotHistogram(lbp,neigh)
"""

n_classes = cfg.vectorsConfig['classes']
                                                    
#print len(EtestVector),len(NEtestVector)
finalVector = concatenateVectors(cfg.vectorsConfig['vectorWorn'],
                                 cfg.vectorsConfig['vectorWithoutWorn'])
finalTags = []
for i in range (0,len(finalVector)):
    if i < len(cfg.vectorsConfig['vectorWorn']):
        finalTags.append(0)
    else:
        finalTags.append(1)
        
# Split and shuffle the dataset
X_train, X_test, y_train, y_test = train_test_split(finalVector, finalTags,
                                                    test_size=.5)

# Vector that contains the LBP values of the traning images
lbpFinalTrainVect = []
lbpFinalTrainVect = clbp.getDescriptorValues(X_train,cfg.lbpConfig['neigh'],
                                             cfg.lbpConfig['radius'],
                                             cfg.lbpConfig['lbpType'])
lbpFinalTestVect = clbp.getDescriptorValues(X_test,cfg.lbpConfig['neigh'],
                                             cfg.lbpConfig['radius'],
                                             cfg.lbpConfig['lbpType'])
# Train a svm
clf = svm.computeSvm(lbpFinalTrainVect,y_train)

# Classifying with a decision function
y_score = clf.decision_function(lbpFinalTestVect)

precision = dict()
recall = dict()
average_precision = dict()

# computing precision and recall
precision[0],recall[0],_= metrics.precision_recall_curve(y_test,y_score)
# computing area under curve
average_precision[0]= metrics.average_precision_score(y_test,y_score)
# plotting precision-recall curve
plt.clf()
plt.plot(recall[0], precision[0], label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('Precision-Recall example: AUC={0:0.2f}'.format(average_precision[0]))
plt.legend(loc="lower left")
plt.show()

# computing rates to ROC curve
fpr,tpr,thresholds=curves.rocCurveValues(y_test,y_score)
# computing area under curve
roc_auc = curves.areaUnderCurves(fpr,tpr)
# plotting the ROC curve
print "Area under the ROC curve : %f" % roc_auc
curves.plotROCCurve(fpr,tpr,roc_auc)



