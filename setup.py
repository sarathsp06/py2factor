#!/usr/bin/env python

PROJECT = 'py2factor'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,
    description='2Factor authention app',
    long_description=long_description,
    author='Sarath Sadasivan Pillai',
    author_email='sarathsp06@gmail.com',
    url='https://github.com/sarathsp06/py2factor',
    download_url='https://github.com/sarathsp06/py2factor/tarball/master',
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],
    platforms=['linux'],
    scripts=[],
    provides=[],
    install_requires=['cliff'],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'py2factor = py2factor.main:main'
        ],
        'py2factor.commands': [
            'profiles = py2factor.profiles:Profiles',
            'add = py2factor.add:Add'
        ],
    },
    zip_safe=False,
)