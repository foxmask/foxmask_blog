Title: How to Publish an Open-Source Python Package to PyPI – Real Python - realpython
Date: 2022-05-27 21:51:56.829253+00:00
Author: FoxMaSk 

tags: python

Status: published





# How to Publish an Open-Source Python Package to PyPI – Real Python - realpython

[How to Publish an Open-Source Python Package to PyPI – Real Python - realpython](https://realpython.com/pypi-publish-python-package/)

# How to Publish an Open-Source Python Package to PyPIReal Python 

par Real Python, 

le lundi 23 mai 2022 16:00Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: How to Publish Your Own Python Package to PyPI 

Python is famous for coming with batteries included, and many sophisticated capabilities are available in the standard library. However, to unlock the full potential of the language, you should also take advantage of the community contributions at PyPI: the Python Packaging Index. 

PyPI, typically pronounced pie-pee-eye, is a repository containing several hundred thousand packages. These range from trivial Hello, World implementations to advanced deep learning libraries. In this tutorial, you’ll learn how to upload your own package to PyPI. Publishing your project is easier than it used to be. Yet, there are still a few steps involved. 

In this tutorial, you’ll learn how to: 

• Prepare your Python package for publication

• Handle versioning of your package

• Build your package and upload it to PyPI

• Understand and use different build systems 

Throughout this tutorial, you’ll work with an example project: a reader package that can be used to read Real Python tutorials in your console. You’ll get a quick introduction to the project before going in depth about how to publish this package. Click the link below to access the GitHub repository containing the full source code of reader: 

Get Source Code: Click here to get access to the source code for the Real Python Feed Reader that you’ll work with in this tutorial. 

Get to Know Python Packaging 

Packaging in Python can seem complicated and confusing for both newcomers and seasoned veterans. You’ll find conflicting advice across the Internet, and what was once considered good practice may now be frowned upon. 

The main reason for this situation is that Python is a fairly old programming language. Indeed, the first version of Python was released in 1991, before the World Wide Web became available to the general public. Naturally, a modern, web-based system for distribution of packages wasn’t included or even planned for in the earliest versions of Python. 

Instead, Python’s packaging ecosystem has evolved organically over the decades as user needs became clear and technology offered new possibilities. The first packaging support came in the fall of 2000, with the distutils library being included in Python 1.6 and 2.0. The Python Packaging Index (PyPI) came online in 2003, originally as a pure index of existing packages, without any hosting capabilities. 

Note: PyPI is often referred to as the Python Cheese Shop in reference to Monty Python’s famous Cheese Shop sketch. To this day, cheeseshop.python.org redirects to PyPI. 

Over the last decade, many initiatives have improved the packaging landscape, bringing it from the Wild West and into a fairly modern and capable system. This is mainly done through Python Enhancement Proposals (PEPs) that are reviewed and implemented by the Python Packaging Authority (PyPA) working group. 

The most important documents that define how Python packaging works are the following PEPs: 

• PEP 427 describes how wheels should be packaged.

• PEP 440 describes how version numbers should be parsed.

• PEP 508 describes how dependencies should be specified.

• PEP 517 describes how a build backend should work.

• PEP 518 describes how a build system should be specified.

• PEP 621 describes how project metadata should be written.

• PEP 660 describes how editable installs should be performed. 

You don’t need to study these technical documents. In this tutorial, you’ll learn how all these specifications come together in practice as you go through the process of publishing your own package. 

For a nice overview of the history of Python packaging, check out Thomas Kluyver’s presentation at PyCon UK 2019: Python packaging: How did we get here, and where are we going? You can also find more presentations at the PyPA website. 

Create a Small Python Package 

In this section, you’ll get to know a small Python package that you can use as an example that can be published to PyPI. If you already have your own package that you’re looking to publish, then feel free to skim this section and join up again at the next section. 

The package that you’ll see here is called reader. It can be used both as a library for downloading Real Python tutorials in your own code and as an application for reading tutorials in your console. 

Note: The source code as shown and explained in this section is a simplified—but fully functional—version of the Real Python feed reader. Compared to the version currently published on PyPI, this version lacks some error handling and extra options. 

First, have a look at the directory structure of reader. The package lives completely inside a directory that can be named anything. In this case, it’s named realpython-reader/. The source code is wrapped inside an src/ directory. This isn’t strictly necessary, but it’s usually a good idea. 

Note: The use of an extra src/ directory when structuring packages has been a point of discussion in the Python community for years. In general, a flat directory structure is slightly easier to get started with, but the src/-structure provides several advantages as your project grows. 

The inner src/reader/ directory contains all your source code: 
```
realpython-reader/
│
├── src/
│   └── reader/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.toml
│       ├── feed.py
│       └── viewer.py
│
├── tests/
│   ├── test_feed.py
│   └── test_viewer.py
│
├── LICENSE
├── MANIFEST.in
├── README.md
└── pyproject.toml
```
The source code of the package is in an src/ subdirectory together with a configuration file