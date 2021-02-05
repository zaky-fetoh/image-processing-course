"""
mahmoud Zaky AttaALLAH, B.Sc.
matlab Image Processing
Task6

this script include two methods to calculate the gray scale image from the rgb chunneled image
method one is simle it culculate the gray scale with simple eequation
in method two i used PCA as concedering the rgb image as a set of ordered vector in rgb space
pca calcute the optimal vector that achive the maximum amount of variance when projecting the
3D space to 1D space suitable for gray scale
"""


import numpy as np
import sklearn.decomposition as deco
import matplotlib.pyplot as plt

def simple_rgb2gray(im):
    return .29* im[:,:,0] + .58*im[:,:,1] + .11*im[:,:,2]

def pca_gray( im ):
    df = np.zeros((im[:, :, 0].size, 3))

    for i in range(3):
        df[:, i] = im[:, :, i].flatten()

    pca = deco.PCA(1)
    d1 = pca.fit_transform(df)
    return d1.reshape(im[:,:,0].shape)

im  = plt.imread('onion.png')

plt.subplot(1,3,1)
plt.imshow(im)
plt.subplot(1,3,2)
plt.imshow(simple_rgb2gray(im),cmap = 'gray')
plt.subplot(1,3,3)
plt.imshow(pca_gray(im),cmap = 'gray')

