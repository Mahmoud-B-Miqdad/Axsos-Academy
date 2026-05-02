<div align="center">

# 🍽️ Database Design: Food Reviews System
**Relational Mapping & Complex Entity Association**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Relational_Schema-orange?style=for-the-badge)

</div>

---

## 📝 Description
This project focuses on designing a robust database schema for a "Food Reviews" application. Based on a provided wireframe, I architected a system that manages restaurants, handles user authentication data, and stores detailed ratings and reviews. The goal was to ensure that every review is accurately linked to both a specific user and a specific restaurant.

---

## 🎯 Key Concepts
* **Requirement Translation:** Mapping UI components like "Star Ratings", "Review Text", and "Restaurant Names" into appropriate SQL data types.
* **Complex Many-to-Many Implementation:** Handling the relationship where many users can review many restaurants through a central `reviews` table.
* **Data Categorization:** Organizing restaurant-specific data (name, address) separately from user-specific data (first name, last name, email) to maintain a normalized structure.
* **Referential Integrity:** Linking tables using composite foreign keys to ensure that a review cannot exist without an associated user and restaurant.

---

## 🛠️ Implementation Highlights
* **ERD Architecture:** Designed using MySQL Workbench with the following core entities:
    * **Users Table:** Captures essential user information including unique emails.
    * **Restaurants Table:** Stores metadata for each food establishment.
    * **Reviews Table (Join Table):** The heart of the system, containing `content`, `rating`, and timestamp data, connecting users to restaurants.
* **Precise Key Management:** Renaming foreign keys to ensure clarity within the schema logic.
* **Audit Fields:** Consistent use of `created_at` and `updated_at` across all tables for data tracking and auditing.

---

## 🚀 How to Explore
1. Open the `.mwb` file in **MySQL Workbench**.
2. Examine the **Three-Tier Architecture**:
   - `users` (Owner of the review)
   - `restaurants` (Subject of the review)
   - `reviews` (The transactional bridge)
3. Review the data types (e.g., `TEXT` for content, `VARCHAR` for ratings) to see how they accommodate real-world user input.