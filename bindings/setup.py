#!/usr/bin/env python2

from setuptools import setup, find_packages

setup(
    name='pulp-bindings',
    version='2.9.0b1',
    license='GPLv2+',
    packages=find_packages(exclude=['test']),
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    install_requires=['m2crypto', 'oauth2>=1.5.170']
)
