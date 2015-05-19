# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:55:38 2015

@author: Administrator
"""
import numpy as np
import ImageOperations as imgOperations
import setupFile as setup
import svm
import computingLBP as lbp

"""
Concatenate two vectos in one

Input: vectorOne,vectorTwo
Output: finalVector
"""    
def concatenateVectors(vectorOne,vectorTwo):
    finalVector = np.concatenate([vectorOne,vectorTwo])
    return finalVector
    
                    
def CreatingSVMModel():
    
    # Compute train,test,label,and name vector to worn Images
    wornVector,wornNames = imgOperations.readImages(setup.wornImages['wornPath'],
                                              setup.wornImages['extension'])
    
    wornTrainVector,wornTestVector,wornLabelsVector,wornTestNames = \
                                                svm.vectorsOfTraingTestTags(
                                                wornVector,
                                                'Worn Images',wornNames) 
                                                               
    # Compute train,test,label,and name vector to Non Eroded Images 
    withoutWornVector,withoutWornNames = imgOperations.readImages(
                                         setup.withoutWornImages[
                                         'withoutWornPath'],
                                         setup.withoutWornImages['extension'])

    withoutWornTrainVector,withoutWornTestVector,withoutWornLabelsVector,\
    withoutWornTestNamesVector = svm.vectorsOfTraingTestTags(
                                 withoutWornVector,
                                 'Without Worn Images',withoutWornNames)

    # Creating final vectors                                                     
    finalTrainVect = []
    finalTrainVect = concatenateVectors(wornTrainVector,withoutWornTrainVector)
    
    finalLabelsVect = []
    finalLabelsVect = concatenateVectors(wornLabelsVector,
                                         withoutWornLabelsVector)
                                         
    # Vector that contains the LBP values of the traning images
    lbpFinalTrainVect = []
    lbpFinalTrainVect = lbp.getDescriptorValues(finalTrainVect,
                                                 setup.LBPSettings['neigh'],
                                                 setup.LBPSettings['radius'],
                                                 setup.LBPSettings['lbpType'])
                                                 # Train a svm
    clf = svm.computeSvm(lbpFinalTrainVect,finalLabelsVect)
    
    return clf