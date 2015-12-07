from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='gam',
    version=version,
    description='Gam Works',
    author='GAM LTD',
    author_email='info@gam.gr',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
