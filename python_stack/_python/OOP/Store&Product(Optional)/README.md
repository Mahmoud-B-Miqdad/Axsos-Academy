<div align="center">

# 🛒 Python OOP: Store and Product Management
**Implementing Business Logic with Object-Oriented Design**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Focus-Object_Oriented_Design-blue?style=for-the-badge)

</div>

---

## 📝 Description
This project simulates a basic store inventory management system. By using two interconnected classes—`Product` and `Store`—I implemented features to manage products, update prices dynamically based on business rules (inflation and clearance), and handle sales operations.



---

## 🎯 Core Features
* **Inventory Management:** Adding products to a store and printing a detailed inventory report.
* **Dynamic Pricing:** * `inflation`: Applies a global price increase to all items.
    * `set_clearance`: Applies a specific discount to all products within a chosen category.
* **Sales Logic:** Finding products by ID, displaying their info before sale, and removing them from the store inventory.

---

## 🛠️ Key Concepts
* **Composition:** The `Store` class maintains a collection of `Product` instances, showing how objects can own and manage other objects.
* **Encapsulation:** Logic for updating price resides within the `Product` class, while logic for inventory management resides in the `Store` class.
* **Iteration & Filtering:** Using loops and conditional statements to perform bulk updates on specific groups of objects (e.g., clearance by category).
* **ID-based Retrieval:** Efficiently locating objects within a list using unique identifiers.

---

## 🚀 How to Run
1. Ensure `product.py` and `store.py` are in the same directory.
2. Run the main execution script:

```bash
python main.py