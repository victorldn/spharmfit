import numpy as np
import quadpy
from scipy.special import sph_harm

def make_harmonic(m=0, n=0, theta=0, phi=0):
    """Sample spherical harmonics at relevant points for numerical integration.

    parameters:
    -----------
    m: array_like
        Order of the harmonic (int); must have `|m| <= n`.
    n: array_like
        Degree of the harmonic (int); must have `n >= 0`. This is often denoted
        by `l` (lower case L) in descriptions of spherical harmonics.
    theta: array_like
        Azimuthal (longitudinal) coordinate; must be in `[0, 2*pi]`.
        The azimuth values are incremented by a factor of `pi` to agree with
        conventions used by `scipy.special.sph_harm` class.
    phi : array_like
        Polar (colatitudinal) coordinate; must be in `[0, pi]`.
    """
    theta = theta[:]
    return sph_harm(m,n,theta,phi)


def get_lebdev_grid():
    """Query positions and weights of Lebdev gridpoints.

    Coordinates are given in `(azimuth, elevation)` pairs (row-major)
    Lebdev grid coordinates are specified in `quadpy` in `(-pi, pi], [0, pi]`
    convention.

    """
    scheme = quadpy.sphere.lebedev_131()
    coordinates = scheme.azimuthal_polar
    weights = scheme.weights
    cartesian = scheme.points

    print("Quadpi bounds:")
    deg = np.rad2deg(coordinates)
    print(np.min(deg, axis=0))
    print(np.max(deg, axis=0))

    return coordinates, weights, cartesian

def leb2sk(obs):
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

   return obs

def main():
    grid = get_lebdev_grid()
    sph_harm_pts = make_harmonic(m=-4, n=4, theta=grid[0][:,0], phi=grid[0][:,1])
    print("norm: ", 4*np.pi*np.sum(grid[1] * np.absolute(sph_harm_pts)**2))
    #print(np.absolute(sph_harm_pts)**2)


if __name__ == "__main__":
    main()
