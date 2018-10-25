#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

from setuptools import setup


setup(
    name='django-robokassa-receipt',
    version='1.4',
    author='Kirill Marchenko',
    author_email='kirill@nekidaem.ru',

    packages=['robokassa', 'robokassa.migrations'],

    url='https://github.com/NeKidaem/django-robokassa',
    license='MIT License',
    description='Приложение для интеграции платежной системы ROBOKASSA в проекты на Django.',
    #long_description=open('README.rst').read() + "\n\n" + open('CHANGES.rst').read(),

    install_requires=[
        # 'Django==1.6',
        'six',
    ],

    classifiers=(
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
