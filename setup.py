import os
from setuptools import setup, find_packages
import config

here = os.path.abspath(os.path.dirname(__file__))
CLASSIFIERS = [
    'Intended Audience :: Ubuntu Users',
    'Natural Language :: English',
    'Operating System :: Ubuntu',
    'Topic :: System :: Authentication',
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

setup(
    name=config.name,
    version=config.__version__,
    license=config.license,
    url=config.url,
    description="A face Authentication system for Ubuntu Linux.",
    classifiers=CLASSIFIERS,
    author="Rushabh Vasani",
    author_email="vasanirushabh24@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
)

