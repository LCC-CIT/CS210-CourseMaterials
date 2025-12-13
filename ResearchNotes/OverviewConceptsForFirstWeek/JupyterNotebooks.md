

<h1>Intro to Jupyter Notebooks</h1>

[TOC]

------

## What They Are

- **Open‑source web app** for creating and sharing documents that combine **live code**, **equations**, **visualizations**, and **narrative text**.
- Originated as the **IPython Notebook**, later expanded to support many languages — the name “Jupyter” nods to **Julia, Python, and R**.
- Supports 100+ kernels, so you’re not limited to Python.

------

## Why They’re Popular

- **Exploratory Data Analysis (EDA)**: Run code in small, testable chunks and see results instantly.
- **Reproducibility**: Code, output, and explanation live in one file (`.ipynb`).
- **Rich Media**: Embed plots, images, LaTeX math, and interactive widgets.
- **Teaching & Collaboration**: Great for tutorials, workshops, and sharing research.

------

## Getting Started

1. **Install** via `pip install notebook` or get it bundled with **Anaconda**.
2. **Launch** with `jupyter notebook` in your terminal — it opens in your browser.
   Doesn't work in Windows PowerShell, use: `python -m notebook`
   The -m option runs a python module as a script.
3. **Create a Notebook**: Add cells for code or Markdown, run them independently, and iterate quickly.

------

## Typical Use Cases

| Domain           | Example                               |
| ---------------- | ------------------------------------- |
| Data Science     | Cleaning datasets, visualizing trends |
| Machine Learning | Training models, tracking experiments |
| Education        | Interactive coding lessons            |
| Research         | Documenting computational workflows   |

------



Absolutely, Brian — let’s walk through a clean, reproducible “Hello, World” in a Jupyter Notebook. This will be minimal but structured, so it’s easy to build on later.

------

## 🧭 Step-by-Step: Hello World in Jupyter

### 1. ✅ Launch the Notebook

From your terminal (with your environment activated), run:

```bash
python -m notebook
```

This opens the Jupyter interface in your browser.

------

### 2. 📓 Create a New Notebook

- Click **New → Python 3** (or whatever kernel you want).
- You’ll see a blank notebook with one cell.

------

### 3. 🧪 Write Your First Cell

In the first cell, type:

```python
print("Hello, world!")
```

Then hit **Shift + Enter** to run the cell.

You should see:

```
Hello, world!
```

printed just below the cell.

------

### 4. 🖋️ Add Markdown (Optional)

Click on a new cell, change the cell type to **Markdown** (from the dropdown), and type:

```markdown
## My First Notebook
This notebook prints a simple greeting using Python.
```

Run it with **Shift + Enter** — now you’ve got a title and description.

------

### 5. 💾 Save Your Work

Click **File → Save and Checkpoint** or hit **Ctrl + S**. Your notebook is saved as a `.ipynb` file.

------

## 🧠 Bonus: Inline Math and Plots

Want to spice it up? Try:

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Simple Plot")
plt.show()
```

Or in Markdown:

```markdown
Euler's identity: $e^{i\pi} + 1 = 0$
```

------

In order to use matplotlib, I had to install (re-install, upgrade?) pip:
` python3 -m pip install --upgrade pip setuptools wheel`

Then install the matplotlib module:
`pip install matplotlib`

