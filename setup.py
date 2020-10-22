from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyxmp',
    version='0.1.1',
    description='A Python XMP metadata injection tool based on py3exiv2.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/numbersprotocol/pyxmp',
    author='Numbersprotocol',
    author_email='hi@numbersprotocol.io',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'py3exiv2',
    ],
    tests_require = [
        'Pillow',
    ],
)
