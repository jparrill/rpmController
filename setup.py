#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='rpmController',
    version='0.1.0',
    url='https://pdihub.hi.inet/troitino/rpmControler',
    license='GPLv2',
    description='more control about your machine rpms',
    authors='Francisco Garcia Troitiño, Juan Manuel Parrilla',
    author_emails='troitino@tid.es, padajuan@gmail.com',
    keywords='rpm yum rpmController',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().split('\n'),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: DevOps',
        'Operating System :: Redhat/CentOS',
        'Programming Language :: Python',
    ]
)
