
# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path
# Generates all package information
import info

setup(**info.info)