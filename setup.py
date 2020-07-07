#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

from setuptools import setup, find_packages

requires = ['itsdangerous', 'Jinja2', 'misaka>=2.0,<3.0', 'html5lib',
            'werkzeug>=1.0', 'bleach', 'flask-caching']

if sys.version_info < (3, ):
    raise SystemExit("Python 2 is not supported.")
elif (3, 0) <= sys.version_info < (3, 4):
    raise SystemExit("Python 3 versions < 3.4 are not supported.")

setup(
    name='nikas',
    version='1.0.0',
    author='Arash Hatami',
    author_email='hatamiarash7@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/Nikas-Project/Nikas-Server',
    license='MIT',
    description='The first persian comment system ',
    classifiers=[
        "Development Status :: Beta",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=requires,
    setup_requires=["cffi>=1.3.0"],
    entry_points={
        'console_scripts':
            ['nikas = nikas:main'],
    }
)