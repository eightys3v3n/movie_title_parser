""" This file is the source for all the packages metadata.
    The 'info' variable should contain all relavent information
    about the project.
"""

import os
from setuptools import find_packages


info = {}

info['name']        = 'movie_title_parser'
info['version']     = '1.0'
info['description'] = 'A small library for parsing movie titles from file names'

# Read long description from README.rst
if os.path.exists('README.rst'):
    with open('README.rst', 'r') as f:
        info['long_description'] = f.read()

# The project's homepage.
#info['url'] = ''

# Author details
info['author']       = 'Terrence Plunkett'
info['author_email'] = 'eightys3v3n@gmail.com'

# License (should match license classifier)
info['license'] = 'MIT'

# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
info['classifiers'] = [
    # Project language
    'Natural Language :: English',

    # Project maturity
    #'Development Status :: 1 - Planning',

    # Intended audience
    #'Intended Audience :: Education',

    # Package category
    #'Topic :: Software Development :: Build Tools',

    # License (should match "license" above)
    #'License :: OSI Approved :: MIT License',

    # Python versions supported
    'Programming Language :: Python :: 3',

    # Operating systems supported
    #'Operating System :: POSIX :: Linux',
    #'Operating System :: Microsoft :: Windows',
],

# What does your project relate to?
info['keywords'] = ''

# You can just specify the packages manually here if your project is
# simple. Or you can use find_packages().
info['packages'] = find_packages(exclude=['contrib', 'docs', 'tests'])

# Alternatively, if you want to distribute just a my_module.py, uncomment
# this:
#   py_modules=["my_module"],

# List run-time dependencies here.  These will be installed by pip when
# your project is installed. For an analysis of "install_requires" vs pip's
# requirements files see:
# https://packaging.python.org/en/latest/requirements.html
#install_requires=[''],

# Specify the python version(s) that are required to run this package.
# >=, !=, <
#info['python_requires'] = '>=3'

# List additional groups of dependencies here (e.g. development
# dependencies). You can install these using the following syntax,
# for example:
# $ pip install -e .[dev,test]
#extras_require={
#    'dev': [''],
#    'test': [''],
#},

# If there are data files included in your packages that need to be
# installed, specify them here.  If using Python 2.6 or less, then these
# have to be included in MANIFEST.in as well.
#package_data={
#    'sample': ['package_data.dat'],
#},

# Although 'package_data' is the preferred approach, in some case you may
# need to place data files outside of your packages. See:
# http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
# In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
#data_files=[('my_data', ['data/data_file'])],

# To provide executable scripts, use entry points in preference to the
# "scripts" keyword. Entry points provide cross-platform support and allow
# pip to create the appropriate form of executable for the target platform.
#entry_points={
#    'console_scripts': [
#        'sample=sample:main',
#    ],
#}