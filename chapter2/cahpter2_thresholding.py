import skimage.filters as filter
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np


"""
Mahmoud Zaky AttaALLAH, B.Sc.
matlab Image processing 
Chapter3 Tasks 

"""

def simple_thresholding( im,T = 128):
    if im.max() <= 1 :
        im = im*255
    return im > T

def simple_adaptive_threshold(im, N= 15, C= 20 ) :
    #t is selected as t = mean + 20  with neighbourhood 15
    if im.max() <= 1 :
        im = np.asarray(im*255)
    smoothed = ndi.gaussian_filter(im, N)
    smoothed += C
    return ( im - smoothed ) > 0

def otsu_threshold(im):
    T = filter.threshold_otsu(im)
    return im > T

im = plt.imread('cameraman.png')
plt.subplot(1,4,1)
plt.imshow(im)

for i, func in enumerate([simple_thresholding,simple_adaptive_threshold,otsu_threshold ]):
    plt.subplot(1,4,i+2); plt.imshow(func(im))

