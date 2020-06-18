from sknni import SkNNI
import numpy as np

class Interpolator(SkNNI):

    def __call__(self, obs):
        EPS = np.finfo(obs.dtype).eps
        RANGE = np.ptp(obs, axis=0)
        if RANGE[0] > RANGE[1]:
            print("exchanging indices")
            a = obs[:,0]
            b = obs[:,1]
            obs = np.vstack((b,a)).T

        if np.all(RANGE < (2*np.pi + EPS)):
            print("Coordinates in radians")
            np.rad2deg(obs, out=obs)
        else:
            print("Coordinates in degrees")

        MINIMA = np.min(obs, axis=0)
        if np.isclose(MINIMA[0], 0):
            obs[:,0] -= 90.0
        if np.isclose(MINIMA[1], 0):
            obs[:,1] -= 180.0
        print(np.min(obs, axis=0))
        print(np.max(obs, axis=0))
        interp_values = super().__call__(obs)
        return interp_values
