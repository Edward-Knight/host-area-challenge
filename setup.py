#!/usr/bin/env python3
from setuptools import find_packages, setup

import host_area

with open("requirements.txt") as f:
    requirements = f.read().split("\n")

setup(
    name="host_area",
    version=host_area.__version__,
    description=host_area.__doc__,
    author="Edward Knight",
    author_email="edw@rdknig.ht",
    url="https://github.com/Edward-Knight/host-area-challenge",

    python_requires=">=3",
    install_requires=requirements,
    packages=find_packages(exclude=["tests"]),
    test_suite="tests",
    entry_points={
        "console_scripts": ["host_area = host_area.__main__:main"]
    }
)
