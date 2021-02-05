import matplotlib.pyplot as plt
import numpy as np
from skimage import io, exposure



def log_trans(im, sig = 3):
    if im.max() <= 1:
        im = im*255
    C = 255 / np.log10(1+im.max() )
    return C * np.log(1+(np.e ** sig -1 ) * im )

def expo_trans(im, alpha = .4, c = 1) :
    return c * ((1+alpha)** im -1 )

def gamma_trans(im, gamma= 1.5, c= 2):
    return c*(im)**gamma

def contrast_stretching(im, a = 150 ,b= 200):
    return (im - im.min()) * ((b-a)/(im.max() - im.min())) + a

def histo_equaliz(im):
    return exposure.equalize_hist(im)


def get_histo(im) :
    return np.histogram(im, 255)[0]

def imhistplt(im) :
    plt.plot(get_histo(im) )

im = plt.imread('cameraman.png')

plt.subplot(1,7,1)
plt.imshow(im, cmap= 'gray')
for i,func in enumerate([log_trans,expo_trans,gamma_trans,contrast_stretching,histo_equaliz ]):
    out = func(im)
    plt.subplot(1, 7, i+2)
    plt.imshow( out, cmap= 'gray')

plt.subplot(1, 7, 7)
imhistplt(im)