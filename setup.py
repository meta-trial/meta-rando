# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages
from os.path import join, dirname, abspath, normpath

with open(join(dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(join(dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

tests_require = []
with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    for line in f:
        tests_require.append(line.strip())

# allow setup.py to be run from any path
os.chdir(normpath(join(abspath(__file__), os.pardir)))

setup(
    name='meta-rando',
    version=VERSION,
    author=u'Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/meta-trial/meta-rando',
    license='GPL license, see LICENSE',
    description='Randomization class and models for meta/edc',
    long_description=README,
    zip_safe=False,
    keywords='django meta edc randomization',
    install_requires=[
        #         'meta-sites',
        'django-crypto-fields',
        'django-collect-offline',
        'django-collect-offline-files',
        'edc-model-admin',
        'edc-registration',
        'tqdm',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires=">=3.7",
    tests_require=tests_require,
    test_suite='runtests.main',
)
