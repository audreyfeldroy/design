#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import design

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = design.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst', 'rt').read()
history = open('HISTORY.rst', 'rt').read()

setup(
    name='design',
    version=version,
    description='Generates various common web design elements. Borders, \
        patterns, textures, gradients, etc.',
    long_description=readme + '\n\n' + history,
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    url='https://github.com/audreyr/design',
    packages=[
        'design',
    ],
    include_package_data=True,
    install_requires=[
        'Pillow',
        'colors.py',
        'cairocffi',
    ],
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='design graphics generator border pattern texture gradient \
        PIL Pillow PyCairo png webdesign',
    test_suite='tests',
)
