# -*- coding: utf-8 -*-
"""
Created on Feb 04  2015

@author: Adrián de las Matas de la Fuente

This script compute an LBP and plot their computed image and the histogram of
values

"""

from skimage.feature import local_binary_pattern 
import matplotlib.pyplot as plt
import numpy as np

"""
Compute the values by LBP of a given image

Input: img: image, P: neighbours to calculate LBP, R: radius, typeLBP: type
of LBP used to calculate the values, by default is 'uniform' but could be:

    'default': original lbp wich is gray scale but not rotation invariant (ri).
    'ror': extension of default, gray scale but with ri.
    'uniform': improved ror with uniform patterns.
    'nri_uniform': non rotation-invariant with uniform patterns.
    'var': ri variance measures of the contrast of local, with ri but not
    grayscale.
    
"""
def computingLBP(img,P,R,typeLBP='default'):
    
    return local_binary_pattern(img,P,R,typeLBP)
    
    
"""
Plot an LBP image and its histogram calculated.

Input: imgH values calculated by the descriptor, P number of neightbours used
to calculate the LBP.

"""
def plotHistogram(imgH,P):
    fig, ((ax1), (ax2)) = plt.subplots(nrows=2, ncols=1,figsize=(9, 6))
    plt.gray()

    ax1.imshow(imgH)
    ax1.axis('off')
    ax2.hist(imgH.ravel(), normed=True, bins=P+2, range=(0,P+2))
    ax2.set_ylabel('Percentage')
    
"""
Return the LBP histogram value per feature

Input: imgH values calculated by the descriptor, P number of neighbours used to
calculate the LBP
Output: values of the histogram as an array
"""
    
def gettingHistValue(imgH,P):
    histo = np.histogram(imgH.ravel(), normed=True, bins=P+2, range=(0,P+2))
    return histo[0]
    
"""
Obtaning the values of the LBP for every image.

Input: vector of images,neighbours,radius,LBP type
Output: vector of LBP values of every image
"""
def getDescriptorValues(vector,neigh,radius,lbpType):
    vectorHistValues=[]
    for i in range(0,len(vector)):
        lbpValues = computingLBP(vector[i],neigh,radius,lbpType)
        histValues= gettingHistValue(lbpValues,neigh)
        vectorHistValues.append(histValues)
    return vectorHistValues
    

"""
Concatenate two vectos in one

Input: vectorOne,vectorTwo
Output: finalVector
"""    
def concatenateVectors(vectorOne,vectorTwo):
    finalVector = np.concatenate([vectorOne,vectorTwo])
    return finalVector
    
