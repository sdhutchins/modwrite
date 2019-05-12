# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='modwrite',
    version='0.1',
    packages=find_packages(),
    author='Shaurita Hutchins',
    author_email='sdhutchins@outlook.com',
    description='A CLI to easily create template TCL or lua based module files.',
    license='MIT',
    keywords="modules lmod tcl template",
    url='https://github.com/sdhutchins/modwrite',
    project_urls={
        "Bug Tracker": "https://github.com/sdhutchins/modwrite/issues",
        "Documentation": "",
        "Source Code": "https://github.com/sdhutchins/modwrite",
    },
    install_requires=['click>=7.0'],
    entry_points={
        'console_scripts': [
            'modwrite = modwrite.cli:main'
        ]
    }
)
