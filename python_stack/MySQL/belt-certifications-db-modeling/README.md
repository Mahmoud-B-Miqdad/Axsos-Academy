<div align="center">

# 🥋 Database Design: Belt Certifications System
**Many-to-Many Relationship Architecture & Skill Tracking**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Many_to_Many-red?style=for-the-badge)

</div>

---

## 📝 Description
In this assignment, I designed a relational database to track student certifications in a "Belt System" (commonly used in martial arts or coding bootcamps). Based on the provided wireframe, the system needs to manage students who can earn multiple belts, and belts that can be held by many students. This required a robust **Many-to-Many** mapping to maintain data integrity and avoid redundancy.

---

## 🎯 Key Concepts
* **Many-to-Many (M:M) Logic:** Identifying that a single user (e.g., Andrew Lee) can achieve multiple certifications (yellow, red, black), requiring a Join Table.
* **Join Table Implementation:** Creating the `users_belts` table to act as the intermediary between `users` and `belts`.
* **Data Normalization:** Storing belt colors in a dedicated table to ensure consistency and prevent typos across the system.
* **Scalable Certification Tracking:** Designing the schema so that adding a new belt type or a new student doesn't require modifying the table structure.

---

## 🛠️ Implementation Highlights
* **Schema Architecture:** Built in MySQL Workbench with the following components:
    * **Users Table:** Stores student profiles (First Name, Last Name).
    * **Belts Table:** A lookup table for all available certification levels (Color).
    * **Users_Belts (Join Table):** Tracks which student has which belt, including a timestamp for when the certification was achieved.
* **Standardized Naming:** Clean table names and precise foreign key naming (`users_id`, `belts_id`) for intuitive querying.
* **Audit Ready:** Every record includes `created_at` and `updated_at` to track the history of certifications.

---

## 🚀 How to Explore
1. Open the `.mwb` file in **MySQL Workbench**.
2. Review the **Relationship Lines**:
   - Trace how the `users_belts` table connects the two primary entities.
   - Observe the One-to-Many relationships converging into the Join Table to form the Many-to-Many structure.
3. Check the **Attributes**: Notice the focus on minimal, high-impact columns to keep the database lean and performant.