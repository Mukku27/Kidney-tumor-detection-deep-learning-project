import setuptools

with open("README.md","r",encoding='utf-8') as f:
    long_description=f.read()

__version__='0.0.0'

REPO_NAME='Kidney-tumor-detection-deep-learning-project'

AUTHOR_USER_NAME='VemulapalliMukesh27'
SRC_REPO='cnnClassifier'
AUTHOR_EMAIL='vemulapallimukesh@gmail.com'

setuptools.setup(
   name=SRC_REPO
   version=__version__
   author=AUTHOR_USER_NAME
   description='A PYTHON PACKAGE FOR CNN'
   long_description=long_description
   


)