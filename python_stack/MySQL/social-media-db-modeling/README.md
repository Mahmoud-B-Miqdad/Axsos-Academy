<div align="center">

# 📊 Database Design: Social Media Likes System
**Entity Relationship Modeling & Database Architecture**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-ERD_Modeling-blue?style=for-the-badge)

</div>

---

## 📝 Description
In this project, I transformed a social media post wireframe into a fully structured database schema. The core objective was to analyze UI elements (User, Post, Likes) and derive the necessary database tables, focusing on building logical relationships that ensure data integrity and scalability.

---

## 🎯 Key Concepts
* **Requirement Analysis:** Analyzing the wireframe to identify core entities such as `Users` and `Posts`.
* **Many-to-Many Relationship:** Implementing a many-to-many relationship between users and posts using a join table named `Likes`.
* **Normalization:** Ensuring data is properly distributed to prevent redundancy, where each user has personal info and each post is linked to its author.
* **Naming Conventions:** Adhering to professional naming standards, specifically using singular forms for foreign keys (`user_id`, `post_id`) to improve query clarity.

---

## 🛠️ Implementation Highlights
* **Schema Design:** The ERD was built using MySQL Workbench and consists of:
    * **Users Table:** Stores basic identity information.
    * **Posts Table:** Stores content and image URLs, linked to the post author.
    * **Likes Table:** Acts as a join table to track user interactions with posts.
* **Data Integrity:** Utilizing Primary Keys and Foreign Keys to enforce constraints and ensure data connectivity.
* **Temporal Tracking:** Including `created_at` and `updated_at` timestamps for historical data tracking.

---

## 🚀 How to Explore
1. Open the provided `.mwb` file using **MySQL Workbench**.
2. Review the relationships between the three tables:
   - **One-to-Many:** Between `users` and `posts` (One user can author multiple posts).
   - **Many-to-Many:** Via the `likes` table (Multiple users can like multiple posts).
3. To generate the SQL script, use the `Forward Engineer` feature within the software.