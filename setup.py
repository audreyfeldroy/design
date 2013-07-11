#!/usr/bin/env python

import os
import sys

import design

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst', 'rt').read()
history = open('HISTORY.rst', 'rt').read()
license = open('LICENSE', 'rt').read()

setup(
    name='design',
    version=design.__version__,
    description='Generates various common web design elements. Borders, \
        patterns, textures, gradients, etc.',
    long_description=readme + '\n\n' + history,
    author='Audrey Roy',
    author_email='audreyr@gmail.com',
    url='https://github.com/audreyr/border',
    packages=[
        'design',
    ],
    entry_points={
        'console_scripts': [
            'design = design.design:command_line_runner',
        ]
    },
    include_package_data=True,
    install_requires=[
        'Pillow',
        # 'pycairo',  # Must be installed manually :(
    ],
    license=license,
    zip_safe=False,
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        "Environment :: Console",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
    keywords='design graphics generator border pattern texture gradient \
        PIL Pillow PyCairo png',
)
