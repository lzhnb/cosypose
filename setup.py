import os
from setuptools import setup, find_packages
# from torch.utils.cpp_extension import BuildExtension, CppExtension
from pybind11.setup_helpers import Pybind11Extension, build_ext
from os import path

here = path.abspath(path.dirname(__file__))

# Use correct conda compiler used to build pytorch
os.environ['CXX'] = os.environ.get('GXX', '')

setup(
    name='cosypose',
    version='1.0.0',
    description='CosyPose',
    packages=find_packages(),
    ext_modules=[
        # CppExtension(
        Pybind11Extension(
            name='cosypose_cext',
            sources=[
                'cosypose/csrc/cosypose_cext.cpp'
            ],
            extra_compile_args=['-O3'],
            verbose=True
        )
    ],
    cmdclass={
        "build_ext": build_ext
        # 'build_ext': BuildExtension
    }
)
