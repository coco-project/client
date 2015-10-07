from setuptools import setup, find_packages

setup(
    name="coco-client",
    description="Client package to communicate with the coco core API.",
    version="0.0.1",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['coco'],
    install_requires=[
        'bunch==1.0.1',
        'simplejson==3.8.0',
        'slumber==0.7.1'
    ],
)
