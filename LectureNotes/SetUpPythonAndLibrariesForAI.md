---
title: Installing scikit-learn and tensor flow
description: How to set up a computer to use Python to work with the scikit-learn and tensorflow AI libraries.
keywords: ML, numpy, scikit-learn, tensroflow, python
generator: Typora
author: Brian Bird
---

<h1>Set Up Python Packages for AI</h1>

**CS 210, Intro to AI Programming**

| Topics                               |                                   |
| ------------------------------------ | --------------------------------- |
| <mark>Overview, History of AI</mark> | Generative AI                     |
| Machine Learning: Symbolic           | Using LLMs in custom applications |
| Machine Learning: Statistical        | Custom chatbot creation           |
| Neural networks                      | LLM fine-tuning                   |
| Image recognition                    | Social and ethical issues of AI   |



<h2>Contents</h2>

[TOC]

## Python Packages We Will Use

### NumPy
NumPy is a scientific computing library for efficient array processing, offering fast, flexible multi-dimensional arrays that outperform native Python lists. It adds additional array features that used by many scientific and machine learning libraries.

### scikit-learn
Scikit-learn is a library for traditional machine learning in Python, built on NumPy arrays. It offers a consistent interface to a wide range of models and tools, many beyond the scope of this course. As you deepen your understanding, the [official documentation](https://scikit-learn.org/stable/documentation.html) is an essential resource.

### TensorFlow with Keras
TensorFlow is a widely adopted, open-source framework and toolkit developed by Google. It provides deep learning neural network functionality and includes Keras, a user-friendly Python API (programming interface). 



## Setup Instructions for Ubuntu Linux

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo apt-get install build-essential python3-dev
$ pip3 install numpy
$ pip3 install scipy
$ pip3 install matplotlib
$ pip3 install scikit-learn
$ pip3 install tensorflow-cpu==2.10.0
$ pip3 install pillow
```



## Setup Instructions for MacOS

### Install Python

Tensorflow for MacOS currently (8/26/2025) requires python 3.9 or 3.10, it won't work with newer versions. Check your Python version (if it is installed)

```bash
python --version
```

If it's older than 3.9 or newer than 3.10.x (where x is any number) then install 3.10 using Homebrew, a MacOS package managaer[^1].

```bash
brew update
brew install python@3.10
```

This will install Python 3.10 on your computer at a location like: `/usr/local/bin/python3.10`

### Install Libraries

```bash
xcode-select --install
pip3 install --upgrade pip
pip3 install numpy
pip3 install scipy
pip3 install matplotlib
pip3 install scikit-learn
pip3 install tensorflow-macos==2.12.0
pip3 install tensorflow-metal==1.0.0
pip3 install pillow
```

- For TensorFlow, specify version 2 to ensure that the proper version of the Keras library is included.
- Metal is Apple’s low-level, high-performance graphics and compute API that provides direct access to the GPU.
- The Pillow library is an image-processing library
- Matplotlib is for plotting.

### Set Up a Virtual Environment

**1. Create a Virtual Environment**

Navigate to your project directory or create one:

```bash
mkdir Projects/pdl
cd Projects/pdl
```

Then create the *virtual environment*[^2]:

```bash
/usr/local/bin/python3.10 -m venv
```

This creates a folder named `venv` containing the isolated Python environment.

**2. Activate the Environment**

```bash
source venv/bin/activate
```

Your terminal prompt will change to show you're inside the virtual environment. Now any `pip3 install` commands will apply only to this project.

**4. Install Your Packages**

Install the dependencies for this project:

```bash
pip3 install --upgrade pip
pip3 install numpy
pip3 install scipy
pip3 install matplotlib
pip3 install scikit-learn
pip3 install tensorflow-macos==2.12.0
pip3 install tensorflow-metal==1.0.0
pip3 install pillow
```

**5. Deactivate When Done**

To exit the virtual environment:

```bash
deactivate
```

## References

- *Practical Deep Learning: A Python-Based Introduction*, 2nd Edition, Ronald T. Kneusel, 2025, No Starch Press. 
  Chapter 0: The operating Environment, Installing the Toolkits

- [Install scikit-Learn](https://scikit-learn.org/stable/install.html)&mdash;scikit-learn.org

- [Install Tensorflow 2](https://www.tensorflow.org/install)&mdash;tensorflow.org
- [Getting Started with Tensorflow Metal](https://developer.apple.com/metal/tensorflow-plugin/)&mdash;Apple Developer

---

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) AI Programming lecture notes by [Brian Bird](https://profbird.dev), written in <time>August 2025</time>, are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). 

MS Copilot GPT-4 was used to draft parts of these notes.

[^1]: Another popular package manager for MacOS is [MacPorts](https://www.macports.org/). 
[^2]: A Python virtual environment is like a sandbox for your Python projects—it isolates dependencies so that each project can have its own specific versions of packages, without interfering with others or your system-wide Python setup. It creates a folder (venv) containing: a) A copy of the Python interpreter. b) A local pip installer. c) A clean site-packages directory for your project’s dependencies. When you activate it, your shell temporarily switches to using that isolated Python and pip. 