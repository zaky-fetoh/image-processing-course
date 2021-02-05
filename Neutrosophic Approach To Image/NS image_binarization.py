# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:50:42 2021
@author: MahZaky
<<< SirMahZaky >>>
"""
import scipy.signal.signaltools as sig
import skimage.filters as filters
import matplotlib.pyplot as plt
import scipy.ndimage as ndim 
import numpy as np 

Windo = (3,3)

def im2gray(im):
    if len(im.shape) != 3 :
        return im
    return np.dot(im, [0.2989, 0.5870, 0.1140] ) 

def normalize( im ) :
    min, max = im.max(), im.min()
    return (im - min ) / (max - min) 

def get_image_gradiant(im):
    dx = ndim.sobel(im, axis = 0 ) 
    dy = ndim.sobel(im, axis = 1)
    return np.hypot(dx, dy) # the secondNorme distance

def NS_transform( im ) :
    T = normalize( im ) 
    F = 1 - T 
    I = 1 - normalize( np.abs( get_image_gradiant( im )) )
    return T, I, F 
    
def entropy(im):
    flatten = im.flatten()
    value, count = np.unique(flatten,return_counts=True) 
    acc = np.sum( count ) 
    return - np.sum([ x / acc * np.log( x / acc ) for x in count ] )
    
def mean_filter( im ):
    kernel = np.ones(Windo)/9 
    return ndim.convolve(im, kernel ) 

def NS_alpha_mean(T, I, F, alpha = .8 ):
    T_bar = mean_filter(T) 
    mask = I < alpha 
    T_bar[mask] = 0 
    addt = T.copy() ; addt[~mask] = 0 
    T_bar = T_bar + addt
    return NS_transform(T_bar) 
    
    

def Proposed_method(im):
    gry_im = im2gray(im )/255 
    filtered_im = sig.wiener( gry_im, Windo )
    T, I, F = NS_transform(filtered_im) 
    alpha = .001 ; pre_entr = entropy( I ) 
    while True :
        T, I, F = NS_alpha_mean(T, I, F)
        entr = entropy( I ) 
        print( entr ) 
        if (entr - pre_entr ) / pre_entr < alpha :
            break 
        pre_entr = entr 
    return filters.median((T  > filters.threshold_sauvola(T) )) 
    

im = plt.imread('page1.jpg') 
for i, func in enumerate([lambda x:x , Proposed_method]) :
    plt.subplot(1,2,i+1); plt.imshow(func(im) ,cmap='gray')
        
        
        
        
        
        
        
        
        
        
        
        
    