# A:\ML projects\setup.py
from __future__ import annotations
from typing import List
from setuptools import setup, find_packages, setup

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements.txt and return a list of packages,
    ignoring blank lines and comments. Remove '-e .' if present.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Aman",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
