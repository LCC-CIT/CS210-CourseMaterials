<h1>Decision Trees</h1>

[toc]

Implementing a basic decision tree in Python is **quite easy**, especially when using the popular and well-optimized machine learning library **scikit-learn** (`sklearn`). You don't have to code the complex tree-building algorithms yourself; you just need to prepare the data and call a few functions.

------



## Example Application: Iris Flower Classification 🌸



A classic, simple application for a decision tree is classifying the species of an Iris flower based on its physical measurements.

- **Goal:** Predict the flower species (`setosa`, `versicolor`, or `virginica`).
- **Features (Input Data):** Sepal length, sepal width, petal length, and petal width.
- **Output:** The classification model itself, which can be visualized as a tree of simple if-then-else rules.

------



## Python Solution (using scikit-learn)



The following code demonstrates how to implement, train, and visualize a decision tree classifier.

Python

```
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# 1. Load the Data
# The Iris dataset is a classic and simple built-in dataset in sklearn.
iris = load_iris()
X = iris.data    # Features (measurements)
y = iris.target  # Labels (species)
feature_names = iris.feature_names
target_names = iris.target_names

# 2. Split Data (Training and Testing)
# Split the data into 80% for training and 20% for testing.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Implement and Train the Decision Tree
# Initialize the classifier and train it on the training data.
# random_state ensures reproducibility.
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluate the Model (Optional but Recommended)
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy on Test Data: {accuracy:.2f}")
# In this simple example, accuracy should be 1.00 (100%)

# 5. Visualize the Decision Tree (The Core Output)
plt.figure(figsize=(15, 10))
plot_tree(
    model,
    feature_names=feature_names,
    class_names=target_names,
    filled=True,      # Color the nodes to indicate the majority class
    rounded=True,     # Round the box corners
    proportion=False, # Show counts instead of proportions
    fontsize=10
)
plt.title("Iris Species Decision Tree Classifier")
plt.show()

# 6. Make a Prediction
# Example: A flower with (Sepal L, Sepal W, Petal L, Petal W)
new_flower = [[5.0, 3.4, 1.5, 0.2]]
prediction_index = model.predict(new_flower)[0]
predicted_species = target_names[prediction_index]
print(f"\nNew flower measurements: {new_flower[0]}")
print(f"Predicted Species: {predicted_species}")
```



### Explanation of the Output Tree



When the code runs, it displays a visualization of the decision process. Each node represents a condition (an "IF" statement), and the path down the tree represents the final classification:

| Component           | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Split Condition** | e.g., `petal length (cm) <= 2.45`. This is the rule the model learned to partition the data. |
| **Gini**            | A measure of **impurity** (how mixed the classes are in that node). A Gini of 0.0 means the node is **pure** (contains only one class). |
| **Samples**         | The number of data points that reached this node.            |
| **Value**           | The count of samples for each class in the node (e.g., `[0, 50, 0]` means 0 Setosa, 50 Versicolor, and 0 Virginica). |
| **Class**           | The majority class in that node; this is the prediction if the branch terminates here. |

The decision tree is inherently a form of symbolic AI because every decision is based on an **explicit, human-readable rule** (like *If petal length is less than or equal to 2.45 cm, go left*), which is simpler and more transparent than complex search or statistical weighting.

That's a great request! Implementing a decision tree from scratch without libraries like scikit-learn is possible for simple applications. It primarily requires using **dictionaries** and **lists** to represent the tree and writing a recursive function for the prediction process.

The most complex part of a real-world decision tree is the training (the math to calculate **Gini impurity** or **Entropy** for optimal splits), which is what scikit-learn automates. However, for a simple, **pre-built** tree, the prediction logic is straightforward.



## Simple Application: T-Shirt Ordering Logic 👕



Let's use a basic pre-defined tree to determine the recommended T-shirt size based on a person's height and weight.



### 1. Representing the Decision Tree



We can represent the decision tree structure using nested Python dictionaries. Each dictionary node contains:

- **`feature`**: The feature to check (e.g., 'height').
- **`split`**: The value at which to split the data (e.g., 175).
- **`left`** and **`right`**: Pointers to the next node (or the final prediction).
- **`prediction`**: The final result if the node is a leaf (a string, like 'M').

Python

```
# The pre-built, hardcoded decision tree
TSHIRT_TREE = {
    'feature': 'height', 'split': 175,
    'left': {
        'feature': 'weight', 'split': 70,
        'left': {'prediction': 'S'},   # height <= 175 AND weight <= 70
        'right': {'prediction': 'M'}  # height <= 175 AND weight > 70
    },
    'right': {
        'feature': 'weight', 'split': 85,
        'left': {'prediction': 'L'},   # height > 175 AND weight <= 85
        'right': {'prediction': 'XL'}  # height > 175 AND weight > 85
    }
}
```

------



## 2. Python Prediction Function (Recursive)



The function below implements the core of the decision tree: recursive traversal. It takes the input data (a dictionary of features) and the current node of the tree, and it navigates down until it hits a leaf node with a prediction.

Python

```
def predict_tshirt_size(person_data, tree):
    """
    Predicts a result by recursively traversing the decision tree.

    Args:
        person_data (dict): Dictionary of features (e.g., {'height': 180, 'weight': 80}).
        tree (dict): The current node/subtree in the decision tree.

    Returns:
        str: The final prediction (e.g., 'L').
    """
    # Base Case: If the current node is a leaf, return the prediction
    if 'prediction' in tree:
        return tree['prediction']

    # Recursive Step: Get feature and split value
    feature = tree['feature']
    split_value = tree['split']
    
    # Get the value of the feature for the person
    input_value = person_data.get(feature)

    # Make the decision and move to the appropriate child node
    if input_value is not None:
        if input_value <= split_value:
            # Go left (TRUE branch)
            return predict_tshirt_size(person_data, tree['left'])
        else:
            # Go right (FALSE branch)
            return predict_tshirt_size(person_data, tree['right'])
    else:
        # Handle cases where input data is missing for the feature
        return "Error: Missing feature data."
```

------



## 3. Example Usage



Python

```
# Test Case 1: Short and light
person_a = {'height': 165, 'weight': 65}
size_a = predict_tshirt_size(person_a, TSHIRT_TREE)
print(f"Person A ({person_a['height']}cm, {person_a['weight']}kg) -> Size: {size_a}")

# Test Case 2: Tall and medium weight
person_b = {'height': 185, 'weight': 75}
size_b = predict_tshirt_size(person_b, TSHIRT_TREE)
print(f"Person B ({person_b['height']}cm, {person_b['weight']}kg) -> Size: {size_b}")

# Test Case 3: Short and heavy
person_c = {'height': 170, 'weight': 80}
size_c = predict_tshirt_size(person_c, TSHIRT_TREE)
print(f"Person C ({person_c['height']}cm, {person_c['weight']}kg) -> Size: {size_c}")
```

**Output:**

```
Person A (165cm, 65kg) -> Size: S
Person B (185cm, 75kg) -> Size: L
Person C (170cm, 80kg) -> Size: M
```

This solution demonstrates the conceptual simplicity of a decision tree prediction. It's essentially a **structured series of `if/else` statements** that are recursively executed, which is the definition of a symbolic, rule-following algorithm.



A solution for traversing the T-shirt decision tree without recursion is achieved using an **iterative** approach, typically a `while` loop, which directly implements the sequential decision process.

This method avoids function call overhead and stack depth limits, making it a conceptually simple, non-recursive, symbolic AI implementation.



## Iterative T-Shirt Sizing Logic 👕



The logic remains the same, but the traversal is done by repeatedly updating the `current_node` variable within a loop until a leaf node is reached.



### 1. Representing the Decision Tree



The tree structure is identical to the recursive example:

Python

```
TSHIRT_TREE = {
    'feature': 'height', 'split': 175,
    'left': {
        'feature': 'weight', 'split': 70,
        'left': {'prediction': 'S'},   # height <= 175 AND weight <= 70
        'right': {'prediction': 'M'}  # height <= 175 AND weight > 70
    },
    'right': {
        'feature': 'weight', 'split': 85,
        'left': {'prediction': 'L'},   # height > 175 AND weight <= 85
        'right': {'prediction': 'XL'}  # height > 175 AND weight > 85
    }
}
```

------



## 2. Python Prediction Function (Iterative)



The function below implements the core traversal using a `while` loop. It stops when the current node contains a `'prediction'` key, signaling a leaf node.

Python

```
def predict_tshirt_size_iterative(person_data, tree):
    """
    Predicts a result by iteratively traversing the decision tree using a while loop.

    Args:
        person_data (dict): Dictionary of features (e.g., {'height': 180, 'weight': 80}).
        tree (dict): The root of the decision tree.

    Returns:
        str: The final prediction (e.g., 'L').
    """
    current_node = tree
    
    # Loop until a leaf node (a node with a 'prediction' key) is reached
    while 'prediction' not in current_node:
        
        # 1. Extract feature and split value from the current internal node
        feature = current_node['feature']
        split_value = current_node['split']
        
        # 2. Get the input value for the feature being tested
        input_value = person_data.get(feature)

        if input_value is None:
            return "Error: Missing feature data for decision."

        # 3. Make the decision and move to the next node (update current_node)
        if input_value <= split_value:
            # Move to the 'left' (TRUE) branch
            current_node = current_node['left']
        else:
            # Move to the 'right' (FALSE) branch
            current_node = current_node['right']

    # Once the loop terminates, return the prediction from the leaf node
    return current_node['prediction']
```

------



## 3. Example Usage



Python

```
# Test Case 1: Short and light
person_a = {'height': 165, 'weight': 65}
size_a = predict_tshirt_size_iterative(person_a, TSHIRT_TREE)
print(f"Person A ({person_a['height']}cm, {person_a['weight']}kg) -> Size: {size_a}")

# Test Case 2: Tall and heavy
person_d = {'height': 190, 'weight': 95}
size_d = predict_tshirt_size_iterative(person_d, TSHIRT_TREE)
print(f"Person D ({person_d['height']}cm, {person_d['weight']}kg) -> Size: {size_d}")
```

**Output:**

```
Person A (165cm, 65kg) -> Size: S
Person D (190cm, 95kg) -> Size: XL
```

This iterative approach perfectly executes the **direct, non-search-based inference** characteristic of a simple symbolic decision tree. It starts at the top (root) and follows the explicit rules until it hits a conclusion (leaf), without needing to explore alternatives or manage a search space.