#!/bin/env python
# -*- coding: utf-8 -*-

'django-cms plugin providing special offers functionality.'

import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='cms-special-offers',
    version='0.1.0.1',
    packages=['cms_special_offers'],
    include_package_data=True,
    description=locals()['__doc__'],
    url='https://github.com/ITrex/cms-special-offers/',
    author='Renat Galimov',
    author_email='renat2017@gmail.com',

    zip_safe=False,

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],

    install_requires=(
        'django-cms',
        'Django',
        'django-filer',
        'django-hvad',
        'south'
    ),

)
