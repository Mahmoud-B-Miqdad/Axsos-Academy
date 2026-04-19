<div align="center">

# 🛠️ Python Utility Library: Underscore Implementation
**Building Custom Functional Programming Utilities**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Functional Programming](https://img.shields.io/badge/Focus-Functional_Programming-orange?style=for-the-badge)

</div>

---

## 📝 Description
This assignment involves creating a custom Python class, `Underscore`, that provides functional utility methods. These methods (`map`, `find`, `filter`, and `reject`) allow for more elegant and readable data manipulation by applying callback functions to iterables.



---

## 🎯 Methods Implemented
1. **Map:** Creates a new list by applying the callback function to every element in the iterable.
2. **Find:** Returns the first element in the iterable that satisfies the condition in the callback function.
3. **Filter:** Returns a new list containing all elements that satisfy the callback condition.
4. **Reject:** Returns a new list containing all elements that do *not* satisfy the callback condition (the inverse of filter).

---

## 🛠️ Key Concepts
* **Higher-Order Functions:** Functions that accept other functions (callbacks) as arguments.
* **Callback Functions:** Passing logic (in this case, using `lambda` functions) as parameters to make our methods highly reusable.
* **Lambda Expressions:** Using anonymous functions for quick, concise logic within method calls.
* **Encapsulation:** Grouping related utility methods inside a single class (`Underscore`) for better organization.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Navigate to the directory containing this script.
3. Run the following command in your terminal:

```bash
python underscore_lib.py