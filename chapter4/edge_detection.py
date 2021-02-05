import matplotlib.pyplot as plt
import skimage.filters as filt
import numpy as np



im = plt.imread('cameraman.png')
edge_det = [lambda x: x, filt.roberts, filt.sobel, filt.prewitt, filt.laplace]
for i, func in enumerate(edge_det):
    plt.subplot(1,len(edge_det), i+1 )
    plt.imshow(func(im), cmap= 'gray')
