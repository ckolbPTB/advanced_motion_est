import numpy as np

def normalise_image(im):
    return((im - np.min(im))/(np.max(im) - np.min(im)))