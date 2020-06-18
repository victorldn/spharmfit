"""Mesh File Loader
extract xyz coordinates from supported mesh files.

For a full list of supported file formats, visit:

`https://pypi.org/project/trimesh/`

Loads mesh and returns np.float64 array of Cartesian coords
"""

import numpy as np
import trimesh
import os

def loadMesh(fname=None):
    assert os.path.isfile(fname)
    mesh = trimesh.load(fname)
    mesh.vertices -= mesh.center_mass
    colors = trimesh.visual.color.ColorVisuals(mesh=mesh)
    mesh.visual = colors
    return mesh

def main():
    FNAME='tests/meshes/bowling_Pin/10492_Bowling Pin_v1_max2011_iteration-2.obj'
    mesh = loadMesh(fname=FNAME)
    xyz  = mesh.vertices.T
    print(mesh.faces)
    print(xyz.shape)

if __name__ == '__main__':
    main()
