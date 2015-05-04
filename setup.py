import os
from setuptools import setup, find_packages

setup(
    name="ipynbsrv-skeleton",
    description="Project skeleton for ipynbsrv Python packages.",
    version="0.0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['ipynbsrv'],
    install_requires=[],
)
