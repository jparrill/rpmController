#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='rpmController',
    version='0.1.0',
    url='https://pdihub.hi.inet/troitino/rpmControler',
    license='MIT',
    description='more control about your machine rpms',
    author='Francisco Garcia Troitiño, Juan Manuel Parrilla',
    author_email='troitino@tid.es, padajuan@gmail.com',
    keywords='rpm yum rpmController',
    install_requires=open('requirements.txt').read().split('\n'),
    data_files=[('/usr/bin', ['bin/rpmcontroller']),
                ('config', ['conf/rpmController.ini'])],
    packages=['rpmcontroller'],
    package_dir={'rpmcontroller': 'lib/rpmcontroller'},
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Console',
        'Intended Audience :: DevOps',
        'Operating System :: Redhat/CentOS/Fedora',
        'Programming Language :: Python',
    ]
)
