<div align="center">

# 🛠️ Database Design: User Dashboard System
**Full-Featured Administrative & Messaging Ecosystem**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Architecture-User_Permissions-orange?style=for-the-badge)

</div>

---

## 📝 Description
This project involves designing a robust relational database schema for a **User Dashboard** application based on specific wireframe requirements. The system is built to handle user registration, tiered access levels (Admin vs. Normal), personalized profiles, and an inter-user messaging/commenting system.

---

## 🎯 Key Concepts
* **User Level Authorization:** Implementing a `user_level` attribute to distinguish between administrative powers (adding/editing/removing users) and standard user capabilities.
* **Complex Messaging Logic:** Modeling a system where users can leave messages for others, and those messages can host multiple threaded comments.
* **One-to-Many Reciprocity:** Handling multiple relationships from the same table, specifically in the `messages` entity where a user can be both a sender and a recipient.
* **Profile Management:** Integrating extended user data such as `description` (bio) as required by the wireframe profile views.

---

## 🛠️ Implementation Highlights
* **Schema Design (As seen in `image_fd3de4.png`):**
    * **Users Table:** Stores core credentials, profile descriptions, and the critical `user_level` for access control.
    * **Messages Table:** Acts as the primary interaction layer, linking a sender (`users_id`) to a specific `recipient_id`.
    * **Comments Table:** Provides a secondary interaction layer, allowing users to comment specifically on messages (`messages_id`).
* **Relational Integrity:** 
    * Used **Foreign Keys** to ensure comments and messages are always tied to existing users.
    * Implemented **Cascading Logic** (implied) to maintain data consistency if a user or message is removed.
* **Wireframe Alignment:** Every field in the database (from `first_name` to `password_confirmation` logic) directly corresponds to the forms provided in the `image_fd3e1a.png` wireframes.

---

## 🚀 How to Explore
1. Compare the **ERD (`image_fd3de4.png`)** with the **Wireframe (`image_fd3e1a.png`)** to see how UI elements map to database columns.
2. Note the **Messaging Flow**:
   - A user leaves a message on another user's wall (`messages` table).
   - Other users can reply to that specific message (`comments` table).
3. Review the **Admin Control**: The `user_level` field determines if the UI should grant access to the "Manage Users" table shown in the wireframes.