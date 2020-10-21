from setuptools import setup, find_packages

setup(
    name='pyxmp',
    version='0.1.0',
    description='A Python XMP metadata injection tool based on py3exiv2.',
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