"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='convert_and_download',
    version='0.0.2',
    description='Convert and Download Jupyter Notebooks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bryanwweber/convert_and_download',
    author='Bryan W. Weber',
    author_email='bryan.w.weber@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    # keywords='sample setuptools development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['thermohw'],
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
    # package_data={
    #     'convert_and_download': ['static/main.js'],
    # },
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
    # project_urls={
    #     'Bug Reports': 'https://github.com/bryanwweber/convert_and_download/issues',
    #     'Source': 'https://github.com/bryanwweber/convert_and_download/',
    # },
)
