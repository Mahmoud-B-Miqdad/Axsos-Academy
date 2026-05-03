<div align="center">

# 🌐 Database Design: Multi-User Blog Platform
**Complex Relational Architecture & User Activity Tracking**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Admin_Roles_&_Analytics-cyan?style=for-the-badge)

</div>

---

## 📝 Description
In this comprehensive project, I engineered a database schema for a blog platform similar to Blogspot. The architecture supports multi-administrator management, content creation (posts/comments), file attachments, and a sophisticated user activity tracking system. The goal was to build a scalable foundation that balances administrative flexibility with detailed analytical insights.

---

## 🎯 Key Concepts
* **Collaborative Administration:** Implementing a `blog_admins` join table to allow multiple users to co-manage a single blog with specific administrative rights.
* **Content Hierarchy:** Designing a multi-layered structure where `Blogs` contain `Posts`, and `Posts` host both `Content/Comments` and `Files`.
* **User Analytics & Tracking:** Developing a `page_views` entity to capture granular data, including IP addresses, visit durations, and specific pages visited by logged-in users.
* **Complex Relationship Mapping:** Managing several **One-to-Many** and **Many-to-Many** associations simultaneously to ensure data integrity across the entire platform.

---

## 🛠️ Implementation Highlights
* **Schema Architecture:** Created in MySQL Workbench featuring:
    * **Users & Blogs:** The core entities for registration and site ownership.
    * **Admins System:** A bridge between Users and Blogs to facilitate co-administration.
    * **Post Management:** Specialized tables for `posts` and `files` to handle media-rich content.
    * **Interaction & Tracking:** Dedicated tables for `content` (comments/replies) and `page_views` (activity logs).
* **Naming Conventions:** Utilized professional, singular foreign key naming (e.g., `blogs_id`, `users_id`) for high query readability.
* **Temporal Auditing:** Uniform implementation of `created_at` and `updated_at` timestamps across all major entities.

---

## 🚀 How to Explore
1. Open the `.mwb` file in **MySQL Workbench**.
2. Examine the **Central Hub**: Notice how the `users` table connects to nearly every part of the system (as authors, admins, and visitors).
3. Review the **Analytics Logic**: Check the `page_views` table to see how user session data is structured for future reporting.
4. Trace the **Admin Flow**: Observe how a user is linked to a blog through the `blog_admins` table to enable shared management permissions.