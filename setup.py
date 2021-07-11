from setuptools import setup, find_packages

import ez_sphinx

setup(
    name='ez_sphinx',
    version=ez_sphinx.version,
    description='Easy sphinx',
    author='Yawei Li',
    author_email='yawei.li@tum.de',
    python_requires='>=3.6',
    packages=find_packages(),
)
