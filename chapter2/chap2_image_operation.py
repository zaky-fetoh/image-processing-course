import matplotlib.pyplot as plot
import numpy as np

"""
Mahmoud Zaky AttaALLAH, B.Sc.
matlab Image processing 
Chapter3 Tasks 

"""
def imadd(im1, im2):
    assert  im1.shape == im2.shape
    return im1 + im2

def imsubtr(im1, im2 ):
    return imadd( im1, im2 * -1 )

def imtimes(im1, scaler):
    assert type(scaler)  == int
    return im * scaler

def imdiv(im,scaler):
    assert type(scaler) == int
    return im / scaler

def im_inver(im) :
    if im.max() <= 1 :
        return 1- im
    else :
        return 255 - im

def imand(im1, musk) :
    assert im1.shape == musk.shape
    assert im1.dtype == np.uint8
    assert musk.dtype == np.bool
    return np.bitwise_and(im1,musk)

def imandscaler(im, scaler) :
    assert im.dtype == np.uint8
    assert type(scaler) == int
    return np.bitwise_and(im,scaler)


def imor(im1, musk):
    assert im1.shape == musk.shape
    assert im1.dtype == np.uint8
    assert musk.dtype == np.bool
    return np.bitwise_or(im1, musk)


def imorscaler(im, scaler):
    assert im.dtype == np.uint8
    assert type(scaler) == int
    return np.bitwise_or(im, scaler)




