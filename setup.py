
import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.4'
PACKAGE_NAME = 'significant_figures'
AUTHOR = 'Luis García Nnomo'
AUTHOR_EMAIL = 'luisnnomo@hotmail.com'
URL = 'https://github.com/luisgn98'

LICENSE = 'MIT'
DESCRIPTION = 'Library for rounding a number to a quantity of significant figures'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


#Packages required to run the library
#INSTALL_REQUIRES = [
#
#      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    #install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)