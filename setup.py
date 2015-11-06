#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name                = 'djehouty',
    version             = version,
    description         = "labeled TSV logger",
    long_description    = """""",
    classifiers         = ["Programming Language :: Python",],
    keywords            = '',
    author              = 'Cedric DUMAY',
    author_email        = 'cedric.dumay@gmail.com',
    url                 = 'https://github.com/cdumay/djehouty',
    license             = 'Proprietary',
    packages            = find_packages('src'),
    package_dir         = {'': 'src'},
    include_package_data= True,
    zip_safe            = True,
    install_requires    = (
        'distribute',
    ),
    entry_points        = """
""",
)
