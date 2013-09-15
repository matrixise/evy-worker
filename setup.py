# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

from evy_worker import release

HERE = os.path.dirname(__file__)

with open(os.path.join(HERE, 'requirements.txt')) as fp:
    requirements = fp.readlines()

setup(
    author=release.author,
    author_email=release.version,
    description='Worker for Evy',
    include_package_data=True,
    install_requires=requirements,
    name=release.name,
    packages=find_packages(),
    version=release.version,
    zip_safe=False,
    entry_points = """
    [console_scripts]
    evy-worker = evy_worker.app:main
    """

)
