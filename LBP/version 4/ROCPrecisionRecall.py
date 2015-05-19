# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 03:58:07 2015

@author: Adrián de las Matas de la Fuente
"""

from sklearn import metrics as mt
import matplotlib.pyplot as plt

"""
Computing false positive rate, true positive rate and thresholds for a ROC
curve.

Input: realLabelBinary (real label for the test set to be predicted),
probPredictedValue(probability of belonging to each class)

Output: fpr,tpr,thresholds
"""
def rocCurveValues(realLabelsBinary,probPredictedValue):
    fpr,tpr,thresholds=mt.roc_curve(realLabelsBinary,probPredictedValue)
    return fpr,tpr,thresholds

"""
Computing the area under the ROC curve

Input: fpr(false positive rate), tpr(true positive rate)
Output: roc_auc
"""
def areaUnderCurves(fpr,tpr):
    roc_auc = mt.auc(fpr,tpr)
    return roc_auc
    
"""
Plotting ROC curve

Input: fpr,tpr,roc_auc
"""
def plotROCCurve(fpr,tpr,roc_auc):
    # Plot ROC curve
    plt.clf()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1.1], [0, 1.1], 'k--')
    plt.xlim([0.0, 1.1])
    plt.ylim([0.0, 1.1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()
    
"""
Computing precision and recall values

Input: precision (to store precision value), recall (to store recall value),
realLabelsBinary(real label for the test set to be predicted),
probPredictedValues(probability of belonging to each class)

Output: precision, recall
"""    
def precisionRecallValues(precision,recall,realLabelsBinary,
                          probPredictedValues):
    precision,recall,_ = mt.precision_recall_curve(realLabelsBinary,
                         probPredictedValues)
    return precision,recall
    
"""
Computing the area under the precision-recall curve

Input:average_prec (to store the area),
realLabelsBinary (real label for the test set to be predicted),
probPredictedValues(probability of belonging to each class)
"""    
def areaUnderPrecisionRecallCurve(average_prec,realLabelsBinary,
                                  probPredictedValues):
    average_prec = mt.average_precision_score(realLabelsBinary,
                                probPredictedValues)
    return average_prec

"""
Plotting precision-recall curves

Input:index,recall,precision,average_precision
"""
def plotPrecisionRecallCurve(index,recall,precision,average_precision):
        plt.plot(recall, precision,
             label='Precision-recall curve of class {0} (area = {1:0.2f})'
                   ''.format(index, average_precision))
                   
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title('Precision-Recall curve')
        plt.legend(loc="lower right")
        plt.show()
                                              
    
