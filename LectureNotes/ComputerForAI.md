---
title: Computer for for AI Work
description: What are the system requirements for the computer you use to do AI work.
generator: Typora
author: Brian Bird
---

<h1>Computer Systems for AI Work</h1>

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

### Graphic Procesing Unit (GPU)

**Graphics Processing Units (GPUs)** are highly parallel processors originally designed for rendering graphics in video games. Their architecture makes them ideal for the massive computations required in deep learning, especially for training large neural networks.

### Why GPUs Matter in Deep Learning

GPUs have enabled deep learning to scale dramatically, bringing supercomputer-level performance to consumer hardware. Many breakthroughs in recent years owe their feasibility to GPU acceleration.

- **NVIDIA** leads the field, especially through its **CUDA** platform, which allows developers to harness GPU power for machine learning tasks.

### GPU vs. CPU

For the models and datasets in this book:

- We’ll use **CPU-only** versions of libraries (e.g. TensorFlow) to keep things simple and accessible.
- Training will be fast enough without GPU acceleration.
- **scikit-learn** runs entirely on the CPU.

### Optional GPU Use

If you have a **CUDA-capable GPU**, you’re welcome to use it:

- Install CUDA properly before setting up packages
- Use a **GPU-enabled version of TensorFlow**
- No need to buy a GPU—examples will run fine on CPU

## References

- *Practical Deep Learning: A Python-Based Introduction*, 2nd Edition, Ronald T. Kneusel, 2025, No Starch Press. 
  Chapter 0: Graphic Processing Units



---

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) AI Programming lecture notes by [Brian Bird](https://profbird.dev), written in <time>August 2025</time>, are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). 

MS Copilot GPT-4 was used to draft parts of these notes.

[^1]: 
[^2]: 