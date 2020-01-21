#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from glob import glob

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'python-aalib',
    'toml',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='dcgot',
    version='0.0.0',
    description="Typos made fun.",
    long_description=readme,
    author="Frederikke Byron",
    author_email='frederikkebyron@gmail.com',
    url='',
    packages=[
        'dcgot',
        'dcgot.memes',
    ],
    package_dir={'dcgot':
                 'dcgot'},
    package_data={'dcgot': ['memes/*.*']},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='dcgot',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
    ],
    tests_require=test_requirements,
    scripts=[x for x in glob('scripts/*.py') if x != 'scripts/__init__.py']
)
