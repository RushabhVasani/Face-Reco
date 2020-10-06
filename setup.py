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
    name='facerec',
    version=config.__version__,
    license='BSD',
    url='http://github.com/rushabh-v/linux_face_unlock',
    description="A face Authentication system for Ubuntu Linux.",
    classifiers=CLASSIFIERS,
    author="Rushabh Vasani",
    author_email="vasanirushabh24@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
)

