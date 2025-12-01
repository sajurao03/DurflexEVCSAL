from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
import os

ext_modules = [
    Extension(
        "monotonic_align.core",
        ["core.pyx"],
        include_dirs=[np.get_include()],
    )
]

setup(
    name="monotonic_align",
    ext_modules=cythonize(
        ext_modules,
        compiler_directives={'language_level': "3"}
    ),
    packages=["monotonic_align"],
)
