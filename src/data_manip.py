import numpy as np
import os
import sys
sys.path.append('../ptbpyrecon/')
import PTBRecon.Functions.Motion.im_reg as reg


def normalise_image(im):
    return((im - np.min(im))/(np.max(im) - np.min(im)))


def reg_im(ima, imb, ptmp, reg_mask, reg_type='bspline', be=0, vol=0, jac=0, sparse=0, sp=2):
    PathTemp = ptmp + 'reg_3d_nonrigid/'
    MirtkPath = '/opt/mirtk/lib/tools/'
    MirtkType = reg_type
    MirtkBe = be
    MirtkSim = 'nmi'
    MirtkSp = sp
    MirtkSpt = 100
    MirtkJac = jac
    MirtkVol = vol
    MirtkSparse = sparse
    MirtkPar = []
    Mirtk4D = 0
    MirtkInitPrevMf = 0
    MirtkRegMulti = 0
    MirtkRegMultiWeight = []
    
    if not os.path.exists(PathTemp):
        os.mkdir(PathTemp)
    
    if os.path.isfile(MirtkPath + 'register'):
        (cmf, cimf, affMat, affPar) = reg.im_reg_mirtk(ima, imb, reg_mask, PathTemp, MirtkPath, MirtkSp, MirtkSpt, MirtkBe,
                                                    MirtkSim, MirtkJac, MirtkSparse, MirtkVol, MirtkPar, Mirtk4D,
                                                    MirtkInitPrevMf, 0, MirtkType, MirtkRegMulti, MirtkRegMultiWeight)
    else:
        cmf = None
    return cmf
    