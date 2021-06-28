from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).resolve().parent

readme = (HERE / 'README.rst').read_text("utf-8")

setup(
    author="Brénainn Woodsend",
    author_email='bwoodsend@gmail.com',
    python_requires='>=3.6',
    description="A coding challenge for a Twig application.",
    install_requires=[],
    extras_require={
        "test": ['pytest>=3']
    },
    license="MIT license",
    long_description=readme,
    name='twig_challenge',
    packages=find_packages(include=['twig_challenge', 'twig_challenge.*']),
    url='https://github.com/bwoodsend/twig_challenge',
    version="0.1.0",
)
