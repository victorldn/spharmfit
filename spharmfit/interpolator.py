from numpy import rad2deg
import numpy as np
from loader import loadMesh
from projector import project, mk_obsrv, sph2cart
from lebdev_grid import get_lebdev_grid, make_harmonic, leb2sk
from sknni import SkNNI
from superclass import Interpolator
from functools import reduce
import matplotlib.pyplot as plt

from shfit import SHFit

def main():
    ROOT = 'tests/meshes/bowling_Pin/'
    FNAME = '10492_Bowling Pin_v1_max2011_iteration-2.obj'
    mesh = loadMesh(fname=ROOT+FNAME)
    mesh_xyz = mesh.vertices.T

    norms, stdd = project(mesh_xyz)
    obs = mk_obsrv(stdd,  norms)

    coords, weights, xyz = get_lebdev_grid()

    #coords = leb2sk(coords)

    interpolator = Interpolator(obs, r=1.0)
    interpolated = interpolator(coords)

    theta = coords[:, 0] + np.pi
    phi   = coords[:, 1]

    SHFit.theta = theta.copy()
    SHFit.phi = phi.copy()
    SHFit.xyz = xyz.copy()

    coefficients = []

    for n in range(4):
        for l in range(-n, n+1):
            sph_harm_pts = make_harmonic(m=l, n=n,
                                         theta=SHFit.theta, phi=SHFit.phi)

            integral = 4*np.pi*np.sum(weights*np.real(sph_harm_pts)*interpolated[:,2])
            fit = SHFit(l, n, integral)
            print(fit)
            coefficients.append(fit)

    fig, ax = plt.subplots(nrows=1, ncols=3, sharey=False)

    cs = ax[0].scatter(obs[:, 1], obs[:, 0], c=obs[:, 2])
    cbar = fig.colorbar(cs)
    ax[1].scatter(interpolated[:, 1], interpolated[:, 0], c=interpolated[:, 2])
    ax[2].scatter(coords[:, 0], coords[:, 1], c=sph_harm_pts[:])
    plt.show()

    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #new_pts = xyz * (np.real(sph_harm_pts)**2)[:,None]
    #new_pts = norms * stdd

    new_pts = np.zeros(SHFit.xyz.shape, dtype=SHFit.xyz.dtype)
    for c in coefficients:
       new_pts += c.reconstructed
    #print(new_pts)


    ax.scatter(*new_pts.T)
    #ax.scatter(*mesh_xyz, alpha=0.2)
    plt.show()


if __name__ == '__main__':

    main()
