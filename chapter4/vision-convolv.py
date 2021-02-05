# -*- coding: utf-8 -*-
"""
@author: MahZaky
<<< SirMahZaky >>>
"""

import numpy as np
import matplotlib.pyplot as plt

def mean_mask(n, m):
    ma = np.zeros((n, m), dtype=np.float)
    ma = ma + 1 / (m * n)
    return ma

def convolv(im, ma=mean_mask(3, 3)):
    ret = np.zeros_like(im,dtype = np.float)
    r, c = im.shape
    mr, mc = [x // 2 for x in ma.shape]

    for i in range(mr, r - mr):
        for j in range(mc, c - mc):
            ret[i, j] = (np.sum(im[i - mr:i + mr + 1
                                   , j - mc: j + mc + 1]*ma))
    return ret

def med(im):
    ma = np.ones((3, 3))
    ret = np.zeros_like(im);
    r, c = im.shape
    mr, mc = [x // 2 for x in ma.shape]

    for i in range(mr, r - mr):
        for j in range(mc, c - mc):
            ret[i, j] = np.median(im[i - mr:i + mr + 1,
                                     j - mc: j + mc + 1]*ma);
    return ret

def guass(n, m, sig=1):
    def G(n, m):
        return (1 / (2 * np.pi * sig ** 2)) * np.e ** (-(n ** 2 + m ** 2) / 2 * sig ** 2)

    ma = np.zeros((n, m));
    ns, ms = n // 2, m // 2
    for i in range(n):
        for j in range(m):
            ma[i, j] = G(i - ns, j - ms);
        return ma


def unshapping_filer(im):
    return im + (im - convolv(im, guass(3, 3)))


def smoth(I):
    return convolv(I, guass(5, 5, 2))


def unity(im):
    return im


# mask = np.ones( (7,7) ) * 1/49 ;
mask = guass(3, 3)

im = plt.imread('cameraman.png')
im = np.asarray(im, dtype=np.float) / im.max()
funcs = [unity, convolv, med, smoth, unshapping_filer]
for i, func in enumerate(funcs):
    plt.subplot(1, len(funcs), i + 1)
    plt.imshow(func(im), cmap='gray')
