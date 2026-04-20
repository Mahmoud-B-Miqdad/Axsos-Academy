<div align="center">

# ⛓️ Python Data Structures: Singly Linked List
**Building Linked Lists from Scratch**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Data Structures](https://img.shields.io/badge/Focus-Linked_Lists-red?style=for-the-badge)

</div>

---

## 📝 Description
This project demonstrates the implementation of a **Singly Linked List**. Unlike standard Python lists, a Linked List consists of individual `SLNode` objects where each node points to the next, creating a chain. I implemented various methods to manipulate this chain, including insertions, deletions, and traversal logic.



---

## 🎯 Key Functionalities
* **Insertion:** Flexible methods to add nodes to the `front`, `back`, or at a `specific index` (`insert_at`).
* **Deletion:** Robust methods to remove nodes from the `front`, `back`, or by a `specific value`.
* **Traversal:** A `print_values` method that uses a "runner" pointer to traverse and display the entire list.
* **Edge Case Handling:** Logic to manage operations on empty lists or lists with a single element.

---

## 🛠️ Key Concepts
* **Node-Based Architecture:** Understanding how `SLNode` acts as a container for data (`value`) and a reference (`next`).
* **The "Runner" Pattern:** A common technique in linked lists where a temporary variable traverses the list to find specific positions without losing the `head` reference.
* **Memory Management:** Manually updating pointers to maintain the integrity of the chain during insertions and removals.
* **Method Chaining:** Every modification method returns `self` to allow for fluent, chainable calls.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Run the script in your terminal:

```bash
python singly_linked_list.py