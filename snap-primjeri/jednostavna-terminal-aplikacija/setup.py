import os
from setuptools import setup

setup(
    name = 'testapp', # Name of the package
    version = '0.1', # Version of the package
    description = 'Python test package', # Short description of the package
    license='GPL v3', # License under which the package is distributed
    author = 'Juraj Benić', # Author of the package
    packages = ['src'], # List of packages to include in the distribution
    install_requires=['future'], # List of dependencies required by the package
    entry_points = {
        'console_scripts': [
            'app=src.app:main'] # Entry point for the console script, maps 'app' command to src.app:main function
            },
    classifiers = [
            'Programming Language :: Python :: 3.13', # Supported Python version
            'Operating System :: POSIX', # Supported operating systems
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)' # License classifier
        ],
)