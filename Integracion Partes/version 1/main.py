# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 03:52:56 2015

@author: Adrián de las Matas de la Fuente
"""

import circleDetection as circleD
import croppingImages as cropImg
import ImageOperations as imgOperations
import setupFile as setup
import SVMModel as svmModel
import croppingLeftBorder as clb
import computingLBP as clbp
import patches as cpatches
import svm

def main():
    
    path ='C:\Documents and Settings\Administrator\Desktop\\'
    imgOperations.creatingDirectories(path);
    
    """
    Parte de creación del clasificador
    """

    model = svmModel.CreatingSVMModel()    
    """
    Parte de obtención de inserts
    """
    images,imagesNames = imgOperations.readImages(
                setup.headToolImagesSettings['readPath']
                ,setup.headToolImagesSettings['extension'])
    circles = [ ]    
    predictedValuesBinary = []

    for i, image in enumerate (images):
        imageName = 'Image'+imagesNames[i]
        circles = circleD.findCircles(images[i],imageName,
                                          setup.insertImagesSettings[
                                          'minRadius'],
                                          setup.insertImagesSettings[
                                          'maxRadius'],
                                          False,circles)
        
        for j, circle in enumerate (circles):
            circle = circles[j]
            imageNameSave= str(j)+imageName
            print imageNameSave
            insert = cropImg.cut(circle[0],circle[1],image,
                                 imageNameSave,True,
                                 setup.insertImagesSettings[
                                 'sizeHorizontalInsert'],
                                 setup.insertImagesSettings[
                                 'sizeVerticalInsert'])
            imgOperations.saveImage(insert,setup.directoriesToSaveImgs[
                              'insertsPath']
                              ,imageNameSave)
            try:
                leftBorderPatch = clb.obtaningLeftBorderImage(insert,imageName,
                                                          inserts=False)
                imgOperations.saveImage(leftBorderPatch,setup.directoriesToSaveImgs[
                              'leftBorderPath'],imageNameSave)
    
                patches = cpatches.computingRegions(leftBorderPatch,
                                                  setup.regionSettings['cols'],
                                                  setup.regionSettings['rows'])
    
                for p in range (0,len(patches)):
                    patchesNameSave = imageNameSave + str(p)
                    patch = patches[p]
                    imgOperations.saveImage(patch,setup.directoriesToSaveImgs[
                                      'patchesPath'],patchesNameSave)
                                      
                    """
                    TO-DO crear nombre con el que los diferentes patches son guard
                    ados
                    """
                                     
                #Calculating lbp values
                try:
                    lbpTestPatches = clbp.getDescriptorValues(patches,
                                                   setup.LBPSettings['neigh'],
                                                   setup.LBPSettings['radius'],
                                                   setup.LBPSettings['lbpType'])
    
                    predictedValues = svm.classify(model,lbpTestPatches)
                except AttributeError:
                    print "not valid patches where to compute LBP values"
                    
    
    
                # Translate predicted values in string to binary
                for i in range (0,len(predictedValues)):
                    if (predictedValues[i] == "Worn piece"):
                        predictedValuesBinary.append(0)
                    else:
                        predictedValuesBinary.append(1)
                        
                #print predictedValuesBinary
                predictedValues = []
                predictedValuesBinary = []
            except:
                print "not a valid Image to crop"

if __name__ == "__main__":
    main() 