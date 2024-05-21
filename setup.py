import setuptools

# Readme file
with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

# Requirements file
with open("requirements.txt", "r", encoding='utf-8') as f:
    requirements = f.read().splitlines()

# Metadata
__version__ = '0.0.0'
REPO_NAME = 'Kidney-tumor-detection-deep-learning-project'
AUTHOR_USER_NAME = 'VemulapalliMukesh27'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'vemulapallimukesh@gmail.com'

# Setup config
setuptools.setup(
    name=SRC_REPO,  # Package name
    version=__version__,  # Version
    author=AUTHOR_USER_NAME,  # Author name
    author_email=AUTHOR_EMAIL,  # Author email
    description='A PYTHON PACKAGE FOR CNN',  # Short description
    long_description=long_description,  # Long description
    long_description_content_type="text/markdown",  # Description type
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Project URL
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # Issues URL
    },
    package_dir={"": "src"},  # Package dir
    packages=setuptools.find_packages(where="src"),  # Find packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Classifiers
    python_requires='>=3.6',  # Python version
    install_requires=requirements,  # Dependencies
    license='MIT',  # License
)
