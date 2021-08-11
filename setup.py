from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'PySafePass',
    version = '1.0.3',
    license='MIT License',
    description = 'SafePass is an Open Source Password Manager. SafePass is released as PySafePass on PyPi.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['pyqt5',
                         'pyperclip', 
                         'cryptography'],
)