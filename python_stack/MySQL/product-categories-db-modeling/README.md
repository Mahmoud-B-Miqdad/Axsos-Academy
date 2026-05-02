<div align="center">

# 🏷️ Database Design: Product Categories System
**Hierarchical Data Structures & Many-to-Many Relationships**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Self_Referencing_Tables-green?style=for-the-badge)

</div>

---

## 📝 Description
This project involves designing a specialized database schema for an e-commerce "Product Categories" system. The challenge was twofold: managing a vast array of products across multiple categories and implementing a hierarchical structure (Sub-categories) within a single table. This ensures that the application can handle complex navigation menus like the one seen in the provided wireframe.

---

## 🎯 Key Concepts
* **Self-Referential Relationships:** Implementing a "Parent-Child" hierarchy within the `categories` table using a `parent_id` to allow for nested sub-categories.
* **Many-to-Many Association:** Creating a bridge table (`category_products`) to allow a single product to belong to multiple categories (e.g., an Action Figure appearing in both "Toys" and "Collectibles").
* **Schema Scalability:** Designing the architecture to support an unlimited depth of sub-categories without changing the table structure.
* **Data Precision:** Utilizing appropriate SQL types like `DECIMAL(8,2)` for product pricing to ensure financial accuracy.

---

## 🛠️ Implementation Highlights
* **ERD Architecture:** Developed in MySQL Workbench featuring:
    * **Products Table:** Stores essential product details like name and price.
    * **Categories Table:** Uses a self-join mechanism to organize hierarchical data.
    * **Category_Products Table:** Manages the complex mapping between products and their various categories.
* **Naming Consistency:** Employing clean, pluralized table names and singular, descriptive foreign keys.
* **Standardized Timestamps:** Automatic tracking of record creation and updates for better data management.

---

## 🚀 How to Explore
1. Open the `.mwb` file in **MySQL Workbench**.
2. Observe the **Circular Relationship** on the `categories` table—this is the logic driving the sub-category system.
3. Trace the **Many-to-Many** link through the `category_products` table to see how products are assigned to their respective headers.