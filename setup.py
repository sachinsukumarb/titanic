from setuptools import find_packages,setup

setup(
    name='titanic',
    author='sachin',
    version='1.0',
    install_requires=['pandas','numpy','seaborn'],
    packages=find_packages()
    
)