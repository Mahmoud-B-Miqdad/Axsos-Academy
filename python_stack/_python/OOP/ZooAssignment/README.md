<div align="center">

# 🦁 Python OOP: Zoo Inheritance
**Mastering Inheritance and Polymorphism**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Focus-Inheritance_&_Polymorphism-blueviolet?style=for-the-badge)

</div>

---

## 📝 Description
This project simulates a zoo management system. The core design uses **Inheritance** to share common attributes (name, age, health) from a base class `Animal`, while **Polymorphism** allows each specific animal (Lion, Monkey, Tiger) to override the `feed()` method, providing unique behaviors tailored to each species.



---

## 🎯 Key Concepts
* **Inheritance:** The base class `Animal` serves as a blueprint, and subclasses extend it to add specific attributes like `pride_size`, `intelligence`, or `stripe_count`.
* **Polymorphism:** The `feed()` method exists in all classes, but behaves differently depending on the object type, demonstrating how different objects can respond to the same message in their own way.
* **Super Method:** Using `super().__init__()` to properly initialize the base class attributes within the child classes.
* **Object Composition:** The `Zoo` class manages a collection of various `Animal` objects, illustrating how different subclasses can be treated as part of the same parent type within a list.

---

## 🛠️ Implementation Highlights
* **Base Class:** Defines common state (`health_level`, `happiness_level`) and shared functionality (`display_info`).
* **Subclasses:** Specialized versions of the base class that override or extend functionality.
* **Management System:** The `Zoo` class provides an interface to add animals and report the status of the entire collection efficiently.

---

## 🚀 How to Run
1. Ensure all files (`animal.py`, `lion.py`, `monkey.py`, `tiger.py`, `zoo.py`) are in the same directory.
2. Run the main execution script:

```bash
python main.py