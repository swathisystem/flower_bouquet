from setuptools import setup,find_packages

setup(
    name='pycart',
    version='0.1.0',
    package_dir={'': 'Example'},
    packages=find_packages('Example'),
    # scripts=['bin/script1','bin/script2'],
    description='Order management package in python'
)
