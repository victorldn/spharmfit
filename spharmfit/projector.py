"""Unit sphere projector.

Project surface points onto unit sphere with original
radii stored as 'colors'

data fed in as col-major: [[x,x,x,...],
                           [y,y,y,...],
                           [z,z,z,...]]
"""
import numpy as np
import numpy.linalg as LA
import trimesh


def project(xyz):
    """Project spatial distribution about a point onto unit sphere.

    Given  a set of points about an origin, remove radial information leaving
    only angular information, thus casting a set of arbitrarily distributed
    points onto the surface of sphere.
    """
    print(xyz.shape)
    norms = LA.norm(xyz, axis=0)
    stdd = xyz/norms[None, :]

    return norms, stdd


def mk_obsrv(xyz, norms):
    """Convert Cartesian description of points into its spherica counterpart.

    Preprocess data for use with skNNI package, which requires data to be fed
    in in terms of longitude and latitude.
    """
    lat = np.rad2deg(np.arcsin(xyz[2, :]))
    lon = np.rad2deg(np.arctan2(xyz[1, :], xyz[0, :]))

    #obsrv_arr = np.vstack((lat, lon, norms)).T
    obsrv_arr = np.vstack((lat, lon, norms)).T

    return obsrv_arr

def sph2cart(coords, r=1.0):

    theta = coords[:,0].view()
    phi   = coords[:,1].view()

    x = r * np.sin(theta) * np.cos(phi),
    y = r * np.sin(theta) * np.sin(phi),
    z = r * np.cos(theta)

    return np.vstack((x,y,z)).T

def main():
    """Plot distances of points in mesh from center-of-mass (COM) on unit sphere.

    Given a triangular mesh, normalize the radial distance of vertices from
    COM and store distances in separate data structure.

    Plot unit sphere with radial distances represented by heatmap.
    """
    ROOT = 'tests/meshes/bowling_Pin/'
    FNAME = '10492_Bowling Pin_v1_max2011_iteration-2.obj'
    mesh = loadMesh(fname=ROOT+FNAME)
    xyz = mesh.vertices.T
    norms, stdd = project(xyz)
    N_MIN = np.min(norms)
    N_MAX = np.max(norms)

    obs = mk_obsrv(stdd, norms)

    norm = colors.Normalize(vmin=N_MIN, vmax=N_MAX)

    for vert_id, vertex in enumerate(mesh.vertices):
        c1 = np.array(cm.hot(norm(norms[vert_id])))*255
        c1 = c1.astype(np.uint8)
        mesh.visual.vertex_colors[vert_id] = c1
    mesh.show()


if __name__ == '__main__':
    from loader import loadMesh
    import matplotlib.cm as cm
    from matplotlib import colors

    main()
