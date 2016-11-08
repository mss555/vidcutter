#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import sys
from codecs import open
from os import path, remove
from re import match

from setuptools import setup


here = path.abspath(path.dirname(__file__))

def get_version(filename='__init__.py'):
    with open(path.join(here, filename), encoding='utf-8') as initfile:
        for line in initfile.readlines():
            m = match('__version__ *= *[\'](.*)[\']', line)
            if m:
                return m.group(1)


def get_description(filename='README.md'):
    with open(path.join(here, filename), encoding='utf-8') as f:
        return f.read()

def get_package_data():
    if sys.platform == 'win32':
        if path.exists('bin/ffmpeg.zip'):
            remove('bin/ffmpeg.zip')
        arch = sys.argv[3]
        if arch == 'win32':
            shutil.copy(path.join(here, 'bin', 'x86', 'ffmpeg.zip'), path.join(here, 'bin'))
        elif arch == 'win-amd64':
            shutil.copy(path.join(here, 'bin', 'x64', 'ffmpeg.zip'), path.join(here, 'bin'))
        return ['vidcutter.ico', 'bin/ffmpeg.zip']
    else:
        return []


setup(
    name='vidcutter',
    version=get_version(),
    author='Pete Alexandrou',
    author_email='pete@ozmartians.com',
    description='FFmpeg based video cutter & joiner with a modern PyQt5 GUI',
    long_description=get_description(),
    url='https://github.com/ozmartian/vidcutter',
    license='GPLv3+',

    packages=['vidcutter'],

    package_dir={'vidcutter': '.'},

    setup_requires=['setuptools >= 28.1.0'],

    install_requires=['PyQt5 >= 5.5'],

    package_data={ 'vidcutter': get_package_data() },

    entry_points={ 'gui_scripts': [ 'vidcutter = vidcutter.vidcutter:main' ] },

    keywords='vidcutter audiovideoediting audiovideo videoeditor video videoedit pyqt Qt5 multimedia',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Communications :: File Sharing',
        'Programming Language :: Python :: 3.5'
    ]
)
