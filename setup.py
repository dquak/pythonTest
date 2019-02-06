from setuptools import find_packages
from distutils.core import setup

install_requires = [
    'requests',
    'xlwt',
    'flask',
    'numpy',
]

setup(name='Distutils',
      version='1.0',
      packages=find_packages(),
      description='psycho python package',
      author='Idan Magled',
      author_email='idanmagled@gmail.com',
      url='http://black-colt.net/psycho/',
      install_requires=install_requires,
      classifiers=["Programming Language :: Python"]
      )
