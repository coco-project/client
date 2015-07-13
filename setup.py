from setuptools import setup, find_packages

setup(
    name="ipynbsrv-client",
    description="Client package to communicate with an ipynbsrv setup.",
    version="0.0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['ipynbsrv'],
    install_requires=[],
)
