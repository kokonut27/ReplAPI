from setuptools import setup
 
#reeee

with open("README.md", "r") as fh:
  long_description = fh.read()
setup(
  name = "REPLAPI",
  install_requires=[
        'bs4',
        'repltalk',
        # other requirements
  ],
  url = "https://github.com/JBYT27/REPLAPI",
  version = "0.0.6",
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