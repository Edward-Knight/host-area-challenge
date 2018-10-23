#!/usr/bin/env python3
from setuptools import find_packages, setup

import host_area

setup(
    name="host_area",
    version=host_area.__version__,
    description=host_area.__doc__,
    author="Edward Knight",
    author_email="edw@rdknig.ht",
    url="https://github.com/Edward-Knight/host-area-challenge",

    python_requires=">=3",
    packages=find_packages(exclude=["tests"]),
    test_suite="tests",
    entry_points={
        "console_scripts": ["host_area = host_area.__main__:main"]
    }
)
