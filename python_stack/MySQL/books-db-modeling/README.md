<div align="center">

# 📚 Database Design: Books & Favorites System
**Relational Data Modeling for User Collections**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Many_to_Many_Mapping-purple?style=for-the-badge)

</div>

---

## 📝 Description
In this project, I designed a relational database schema for an application that tracks users, books, and user-curated lists of favorite books. The primary goal was to model the relationship where many users can favorite many different books, ensuring a seamless data flow for personalized reading lists.

---

## 🎯 Key Concepts
* **Requirement Interpretation:** Translating the need for a "Favorite List" into a functional relational structure.
* **Many-to-Many (M:M) Association:** Implementing a join table (`favorites`) to resolve the complex relationship between `users` and `books`.
* **Schema Design Trade-offs:** Following the assignment's guidance to include the `author` directly within the `books` table for simplicity, while acknowledging that a separate table would offer higher normalization.
* **Database Integrity:** Using unique identifiers (Primary Keys) and correctly linked Foreign Keys to maintain record consistency across the schema.

---

## 🛠️ Implementation Highlights
* **ERD Architecture:** Created using MySQL Workbench with the following entities:
    * **Users Table:** Stores user profiles (First and Last Name).
    * **Books Table:** Contains book metadata including `title` and `author`.
    * **Favorites Table (Join Table):** Acts as the bridge, linking `users_id` and `books_id` to track individual preferences.
* **Standardized Metadata:** Every table includes `created_at` and `updated_at` timestamps for robust data auditing and tracking.
* **Naming Conventions:** Adhered to clean naming practices, ensuring foreign keys are singular and descriptive.

---

## 🚀 How to Explore
1. Open the `.mwb` file in **MySQL Workbench**.
2. Navigate to the **EER Diagram** view to visualize the table connections.
3. Observe the **Many-to-Many** link:
   - Notice how the `favorites` table allows a single book to be favorited by multiple users.
   - Trace how a single user can have an extensive list of favorite books within the same bridge table.