---
title: Unit 1 Overview
description: What's AI
keywords: Classical AI, Symbolic AI, GOFAI
generator: Typora
author: Brian Bird
---

**CS 210, Intro to AI Programming**

<h1>Overview of AI</h1>



| Topics                                   |                           |
| ---------------------------------------- | ------------------------- |
| 1. What is AI, Python                    | 6. ANN: Image recognition |
| 2.  <mark>Symbolic AI</mark>             | 7. Generative AI          |
| 3. Classical Machine Learning: Training  | 8. Custom chatbot         |
| 3. Classical Machine Learning: Inference | 9. LLM fine-tuning        |
| 5. Midterm                               | 10. Ethics                |
|                                          | 11. Final                 |



<h2>Contents</h2>

[TOC]

## Review

- John McCarthy, a mathematics professor at Dartmouth College coined the term *Artificial Intelligence* in 1956.
- Categories of AI
  (There are other categories, but these are some of the major ones.)

  - Symbolic (GOFAI)
    - Rule-based, expert systems
    - Search-based


  - Machine Learning
    - Statistical
    - ANN (Artificial Neural Networks)


## Symbolic AI

- Last time, we briefly discussed expert systems as an example of rule-based systems. You wrote a "toy" version of an expert system.
- This time we will explore search-based systems and you will write a problem solving "AI" system using this approach.

### Search

Many problems can be thought of as search problems. We normally think of searching as a way to solve problems like finding a web site, finding a book in a library, or finding a product in an online store. But search can also be used to find the shortest route on a road map or the best sequence of moves to win a game.

- **Breadth-First Search (BFS)**: This algorithm is one way of solving this problem without trying all the combinations of legal transitions. It explores all possible states level by level. It starts from the initial state and explores all possible moves, then moves to the next level of states. BFS guarantees finding the shortest path (minimum number of river crossings) to the goal state because it explores all nodes at the present depth level before moving on to nodes at the next depth level.

Note: Parts of this document were drafted with assistance from Gemini 2.5 Flash


---



[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/) Intro to AI Course Materials by [Brian Bird](https://profbird.dev), written in <time>2025</time>, are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). 

[^1]: [Dartmouth workshop](https://en.wikipedia.org/wiki/Dartmouth_workshop)&mdash;Wikipedia
[^2]: 
