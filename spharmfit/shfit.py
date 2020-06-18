from scipy.special import sph_harm
from quadpy import sphere
import numpy as np

class SHFit(object):
    integration_scheme = sphere.lebedev_131()
    theta = None
    phi = None
    xyz = None

    def __init__(self, l, n, coeff):
        self.l = l
        self.n = n
        self.coeff = coeff

    def __repr__(self):
        return f"<l={self.l:>2}, n={self.n:>3}, coefficient={self.coeff:>7.3f}>"

    @property
    def __Y_mn(self):
        #a = sph_harm(self.l, self.n, self.theta, self.phi)
        return sph_harm(self.l, self.n, SHFit.theta, SHFit.phi)

    @property
    def reconstructed(self):
        a =  self.coeff * (self.xyz * np.real(self.__Y_mn[:,None]))
        return(a)
