'''
File: setup.py
Description: Bolt installation script
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 28/08/2017
'''
from setuptools import setup, find_packages
setup(
    name='bolt',
    version='0.0.1',
    packages=find_packages(exclude=['docs', 'tests', 'temp'])
)
