#!/usr/bin/env python
#  -*- coding: utf8 -*-

from setuptools import setup

setup(
    name='qwasm',
    version='1.0.1',
    packages=['qwasm'],
    keywords=['wasm', 'disassembler', 'decoder'],
    license='MIT',
    url="https://github.com/CQCL/qwasm",
    author='Melf Johannsen',
    author_email='melf.johannsen@quantinuum.com',
    description='WebAssembly decoder & disassembler',
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'wasmdump = wasm.__main__:dump'
        ]
    }
)
