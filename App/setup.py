from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "Main",
  version = "1.0.0",
  description = "REPLAPI Module",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "",
  author = "JBYT27",
  author_email = "Your email",
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "GNU General Public License v3 (GPLv3)",
  packages=['REPLAPI'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)