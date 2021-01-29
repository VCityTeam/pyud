#!/usr/bin/env python

import codecs
import os

from setuptools import find_packages
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

version = None
exec(open('ud/version.py').read())

long_description = ''
with codecs.open('./README.md', encoding='utf-8') as readme_md:
    long_description = readme_md.read()

setup(
    name="ud",
    version=version,
    description="A set of treatments of Urban Data.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/VCityTeam/docker-helper-py',
    project_urls={
        'Source': 'https://github.com/VCityTeam/pyud',
        'Tracker': 'https://github.com/VCityTeam/pyud/issues',
    },
    packages=find_packages(exclude=["tests.*", "tests"]),
    dependency_links=['https://github.com/VCityTeam/docker-helper-py'],
    python_requires='>=3.7',
    zip_safe=False,
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    maintainer='vcity_devel',
    maintainer_email='vcity@liris.cnrs.fr',
)
