# SPHARMFIT - Spherical Harmonic Fitting of crystal voids
----------------------

Python package for deriving shape descriptors of voids in organic crystal structures.

The algorithm relies on spherical nearest neighbour interpolation and numerical integration on the surface of the sphere.

It is reliant on the following Python packages:
    * [`trimesh`](https://pypi.org/project/trimesh/) - Ppure Python library for loading and using triangular meshes
    * [`pyglet`](https://pypi.org/project/pyglet/) - Cross-platform windowing and multimedia library
    * [`quadpy`](https://pypi.org/project/quadpy/) - Numerical integration, quadrature for various domains
    * [`sknni`](https://pypi.org/project/sknni/) - spherical k-nearest neighbors interpolation and is a geospatial interpolator
