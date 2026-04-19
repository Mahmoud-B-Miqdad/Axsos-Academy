<div align="center">

# 🐍 Python Fundamentals: Modular Programming
**Understanding Modules, Imports, and Execution Contexts**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Modules](https://img.shields.io/badge/Focus-Modules_&_Execution-yellowgreen?style=for-the-badge)

</div>

---

## 📝 Description
This assignment explores how Python handles file execution and imports. It demonstrates the critical difference between running a script directly versus importing it into another file. By using the `if __name__ == "__main__":` block, I learned how to separate executable testing logic from reusable code components.



---

## 🎯 Key Concepts
* **`__name__` variable:** A special built-in variable that holds the name of the current module. When a file is run directly, it is set to `"__main__"`; when imported, it is set to the filename.
* **Modularization:** Organizing code into reusable units (modules) to promote clean and scalable architecture.
* **Direct vs. Imported Execution:** Controlling what logic runs when a file is executed independently versus when it acts as a dependency for other parts of the project.

---

## 🛠️ Key Logic
* **The Main Block:** The `if __name__ == "__main__":` guard prevents test/demo code from executing when the module is imported into another script, ensuring that importing a file remains a clean operation.
* **Namespace Management:** Understanding how variables and functions from `parent.py` become available in `child.py` upon import.

---

## 🚀 How to Run
1. Ensure both `parent.py` and `child.py` are in the same directory.
2. To see the "Imported" behavior, run the child file:

```bash
python child.py