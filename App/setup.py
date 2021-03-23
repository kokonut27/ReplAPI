from setuptools import setup
 
#reeee

with open("README.md", "r") as fh:
  long_description = fh.read()
setup(
  name = "REPLAPI",
  version = "0.0.3",
  description = "REPLAPI Module",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = "darkdarcool30",
  author_email = "darkdarcool@gmail.com",#email
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "MIT",
  packages=['REPLAPI'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)