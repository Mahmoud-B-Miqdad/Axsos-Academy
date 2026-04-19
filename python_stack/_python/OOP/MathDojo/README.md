<div align="center">

# 🧮 Python OOP: MathDojo
**Advanced Method Chaining with Variable Arguments**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Focus-Fluent_API-blue?style=for-the-badge)

</div>

---

## 📝 Description
This assignment involves creating a `MathDojo` class that allows for fluent, chainable mathematical operations. By utilizing Python's `*args` syntax, the class can accept an arbitrary number of arguments for both addition and subtraction, keeping the internal `result` state consistent throughout the chain.



---

## 🎯 Key Features
* **Variable Arguments (`*nums`):** Allows the `add` and `subtract` methods to process a single number or a long list of numbers passed dynamically.
* **Method Chaining:** Returns `self` at the end of each operation to enable the fluent syntax `md.add().subtract().add()`.
* **State Persistence:** Maintains the `result` attribute across multiple chained method calls.

---

## 🛠️ Key Concepts
* **`*args` (Variable-Length Arguments):** A powerful Python feature that collects extra positional arguments into a tuple, enabling functions to be more flexible.
* **Fluent Interface:** Designing a class where method calls can be chained together to form a readable, sentence-like code structure.
* **Encapsulation of State:** Keeping the calculation logic and the result inside one class instance.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Navigate to the directory containing this script.
3. Run the following command in your terminal:

```bash
python math_dojo.py