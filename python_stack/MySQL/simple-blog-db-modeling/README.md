<div align="center">

# 📅 Database Design: Simple Blog System
**Relational Architecture for Content Management & Social Interaction**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-ERD_Modeling-blue?style=for-the-badge)
![Backend](https://img.shields.io/badge/Logic-One_to_Many-orange?style=for-the-badge)

</div>

---

## 📝 Description
This project involves the structural design of a "Simple Blog" database system. Based on initial wireframes for user authentication, post creation, and commenting, I developed a relational schema that ensures data integrity and seamless interaction between users and content. The design focuses on capturing the lifecycle of a blog post—from the author's initial entry to the community's feedback through comments.

---

## 🎯 Key Concepts
* **Hierarchical Data Flow:** Establishing a clear path from Users to Posts, and subsequently to Comments.
* **Relational Integrity:** Implementing One-to-Many relationships to ensure every post and comment is attributed to a verified user.
* **Authentication Readiness:** Designing the `users` entity with necessary fields (email, password) to support secure login and registration flows seen in the wireframes.
* **Content Versioning:** Utilizing timestamp auditing (`created_at`, `updated_at`) to track content history and sort feeds chronologically.

---

## 🛠️ Implementation Highlights
* **ERD Architecture:** Crafted using MySQL Workbench with three pivotal entities:
    * **Users Table:** The foundation of the system, storing credentials and unique identifiers.
    * **Posts Table:** Contains the core blog content, linked to the `users` table via a Foreign Key (`users_id`).
    * **Comments Table:** A multi-referenced entity that links to both a specific User (author) and a specific Post.
* **Relational Mapping:**
    * **User → Posts (1:N):** One user can author multiple articles, but each article belongs to one author.
    * **User → Comments (1:N):** One user can provide feedback across various posts.
    * **Post → Comments (1:N):** Each blog post can host an unlimited thread of community comments.
* **Data Typing:** Careful selection of `TEXT` for dynamic content lengths and `DATETIME` for precise event logging.

---

## 🚀 How to Explore
1. **Schema Review:** Open the provided ERD image or `.mwb` file to examine the table connections.
2. **Cardinality Check:** Observe how the "crow's foot" notation correctly illustrates that a single Post can have many Comments, but a Comment is tied to exactly one Post.
3. **Wireframe Alignment:** Compare the database fields with the "Simple Blog" wireframes; notice how the "Posted by: Andrew" UI element maps directly to the `users_id` relationship in the `posts` table.
4. **Query Potential:** Consider how a single `JOIN` operation can retrieve a post along with its author's email and all associated comments.