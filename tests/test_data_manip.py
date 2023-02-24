import numpy as np
import sys

sys.path.append('./src')
import data_manip

def test_normalise_image():
    im = np.random.randn(20,20)
    im_norm = data_manip.normalise_image(im)
    assert np.min(im_norm) == 0
    assert np.max(im_norm) == 1
    
def test_reg_im():
    ima = np.random.randn(20,20,1)
    imb = np.random.randn(20,20,1)
    reg_mask = np.ones((20,20,1))
    data_manip.reg_im(ima, imb, './', reg_mask)