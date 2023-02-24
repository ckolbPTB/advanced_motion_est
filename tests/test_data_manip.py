import numpy as np
import os
import sys

sys.path.append('./src')
import data_manip

def test_normalise_image():
    im = np.random.randn(20,20)
    im_norm = data_manip.normalise_image(im)
    assert np.min(im_norm) == 0
    assert np.max(im_norm) == 1
    
    
def test_reg_im():
    ima = np.random.randn(20,20,1,1)
    imb = np.random.randn(20,20,1,1)
    reg_mask = np.ones((20,20,1,1))
    reg_path = os.getcwd()
    data_manip.reg_im(ima, imb, reg_path, reg_mask)