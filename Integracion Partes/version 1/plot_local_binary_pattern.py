
"""
Created on Fri Jan 30  2015

@author: Adrián de las Matas de la Fuente

Create an histogram of the values calculated by a descriptor, in this case
LBP.

Input: imgH values calculated by the descriptor, P number of neightbours used
to calculate the LBP


"""
import matplotlib.pyplot as plt

# plot histograms of LBP of textures
def plotHistogram(imgH,P):
    fig, ((ax1), (ax2)) = plt.subplots(nrows=2, ncols=1,figsize=(9, 6))
    plt.gray()

    ax1.imshow(imgH)
    ax1.axis('off')
    ax2.hist(imgH.ravel(), normed=True, bins=P+2, range=(0,P+2))
    ax2.set_ylabel('Percentage')

