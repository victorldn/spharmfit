from setuptools import setup

setup(name='spharmfit',
      version='0.1',
      description='Spherical harmonics surface fitter',
      url='https://github.com/cha10vd/spharmfit',
      author='Victor Do Nascimento',
      author_email='contact@victordn.me',
      license='MIT',
      packages=['spharmfit'],
      install_requires=['trimesh', 'pyglet', 'quadpy', 'sknni']
      scripts=['bin/norms']
      zip_safe=False)

