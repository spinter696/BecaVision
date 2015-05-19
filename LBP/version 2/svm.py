# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 02:55:14 2015

@author: Adrián de las Matas de la Fuente
"""

from sklearn import svm

"""
Train an specific svm with an specific kernel, by default is linear
Input: train vector, tags vector, kerneltype
Output: clf svm object
"""
def computeSvm(train,tags,kernelType='linear'):
    clf = svm.SVC(kernel=kernelType)
    clf.fit(train,tags)
    return clf
    
"""
classify a test vector into tags with a specific svm
Input: svm object, test vector
Output: prediction vector
"""
def classify(clf,test):
    #for element in enumerate(test):
    prediction = clf.predict(test)
    return prediction
#return vectorImages
    
"""
Compute the vector of traning, test and the tags of the training one from a 
specific dataset. Also it computes the names of the test vector to identify 
them when the classification is gonna be done.
In this specific case the set of training is the 70% of the main dataset and
the set of test is the difference between them

Input: vector of image,a tag and a vector of names.
Output: vector of traning and test images, a vector of tags, and a vector
of names for the test one
"""
def vectorsOfTraingTestTags(vector,tag,names):
    
    # The size of the traning set
    trainSize = len(vector)*0.7
    trainVector = []
    testVector = []
    tagsVector = []
    testNames = []
    
    # Creating the traning ,test, tags and names vectors
    for i in range(0,len(vector)):
        # less than size of traning, the image is append to the traning vector
        if (i <= trainSize):
            trainVector.append(vector[i])
            # the desired tag is appended in a vector of them
            tagsVector.append(tag)
        else:
            # create the test vecot and the names one
            testVector.append(vector[i])
            testNames.append(names[i])
    
    return trainVector,testVector,tagsVector,testNames