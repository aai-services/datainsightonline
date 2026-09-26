---
title: "Packaging and Publishing a Python Program"
author: "Abdi Tolesa"
date: 2021-10-13
description: "This article aims to explain how a Python program can be packaged and published so that other users and developers could access and use it. It will show you how to install the tools required to..."
categories: ["Python"]
image: images/9b2dd8_14cbff15cf0b4a9e8394ec0ed6f1b20e.webp
wix-url: https://www.datainsightonline.com/post/packaging-and-publishing-a-python-program
---
This article aims to explain how a Python program can be packaged and published so that other users and developers could access and use it. It will show you how to install the tools required to package a python project, what the files structure should look like, how to build the package and publish it to the Python Package Index, PyPI which is the official third-party software repository for Python.

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name X.Y designates a submodule named Y in a package named X.

First lets install the Package Installer of Python, pip with the following commands.

```python
# UNIX/Mac
python3 -m pip install --upgrade pip

# Windows
py -m pip install --upgrade pip
```

That installs/upgrades your pip to the latest version.

Once we have the tool required in place, lets look at how the file structure must be for our 'example_package' package to be considered a package by python.

```python
packaging_tutorial/
└── src/
    └── example_package/
        ├── __init__.py
        └── example.py
```

__init__.py is essential for the folder to be recognized by Python as a package. An empty __init__.py file makes all functions from the above modules available when this package is imported. Note that you can optionally define functions from individual modules to be made available by importing them in the file.

Now, lets add files that are important for publishing our package to the project's directory.

```python
packaging_tutorial/
├── LICENSE
├── README.md
├── setup.py
├── src/
   └── example_package/
       ├── __init__.py
       └── example.py
```

Every package published need to have a metadata that describes it.

There are two types of metadata: static and dynamic.

- Static metadata (setup.cfg): guaranteed to be the same every time. This is simpler, easier to read, and avoids many common errors, like encoding errors.
- Dynamic metadata (setup.py): possibly non-deterministic. Any items that are dynamic or determined at install-time, as well as extension modules or extensions to setuptools, need to go into setup.py.

Lets now walk through each new file introduced to the project's directory

setup.py : setup.py is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include. The content of this file typically looks like this:

```python
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
```

README.md : This file acts as the long_description of our package — which we set up in the setup.py file.

LICENSE : It’s important for every package uploaded to the Python Package Index to include a license. This tells users who install your package the terms under which they can use your package

Now, it is time to generate a distribution package and publish it. A distribution package is the one that could be published to PyPI and can be installed with pip.

Run the following command to build the package.

```python
# Unix/Mac
python3 -m build
# Windows
py -m build
```

The following new directory and files will be created after that.

```python
dist/
  example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
Next, lets build the package.
```

Finally, it is time to upload our package to PyPI.

The first thing you’ll need to do is register an account on TestPyPI, which is a separate instance of the package index intended for testing and experimentation.

The last tool we need here is twine that can be installed as follows.

```python
#Unix/Mac
python3 -m pip install --upgrade twine
# Windows
py -m pip install --upgrade twine
```

Once twine is installed, lets upload our package to the test pypi! You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.

```python
# Unix/Mac
python3 -m twine upload --repository testpypi dist/*
# Windows
py -m twine upload --repository testpypi dist/*
```

That's pretty much it! We have successfully uploaded our package and it can be installed by pip.
