"""Cython compiles a .pyx module."""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os

module = os.environ['MODULE']
name = os.path.splitext(module)[0]
ext_modules = [Extension(name, [module])]

setup(
  name = 'Euler Problem',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
