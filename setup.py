#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-make',
    version='0.0.3',
    description='Django development environment `$ make` middleware',
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/django-make',
    requires=['Django (>=1.3.0)'],
    packages=['django_make',],
    package_dir = {'django_make': 'lib'},
    license='MIT License',
    zip_safe=True)