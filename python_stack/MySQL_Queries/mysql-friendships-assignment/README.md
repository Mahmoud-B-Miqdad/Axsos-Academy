<div align="center">

# 🤝 MySQL: Friendships (Self-Join Mastery)
**Modeling Recursive Relationships & Social Network Logic**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Self_Join-yellow?style=for-the-badge)

</div>

---

## 📝 Description
In this project, I implemented a social-network-style database focused on user friendships. The core challenge was to manage a **Many-to-Many self-referential relationship**, where a single `users` table acts as both the source and the target of a friendship. This project also includes "Ninja Queries" designed to extract complex social statistics and sorted relationship data.

---

## 🎯 Key SQL Concepts Applied
* **Self-Join Strategy:** Utilizing the `users` table twice in a single query by using Aliases (`users AS user2`) to distinguish between the user and their friend.
* **Recursive Many-to-Many:** Implementing a join table (`friendships`) that references the same parent table twice through two distinct foreign keys (`user_id` and `friend_id`).
* **Subqueries & Aggregations:** Using nested `SELECT` statements and `GROUP BY` to identify power users (those with the highest number of friends).
* **Conditional Filtering & Sorting:** Applying `WHERE` and `ORDER BY` to filter specific social circles and present them in alphabetical order.

---

## 🛠️ Query Highlights
The script covers foundational and advanced "Ninja" level tasks:
1. **Schema Design:** Crafting a self-referencing relationship with `ON DELETE CASCADE` to ensure data integrity.
2. **Relationship Mapping:** Populating a social graph with specific connections between 6 unique users.
3. **Friendship Statistics:** Calculating total platform activity and identifying the most "popular" user.
4. **Targeted Discovery:** Retrieving and sorting friends for specific profiles (e.g., Amy and Marky).

---

## 🚀 How to Explore
1. **SQL Script:** Open `friendships_queries.sql` to examine the schema architecture and the self-join logic.
2. **Visual Results:** Check the `/screenshots` folder to see the generated social graph and the output of the Ninja queries.
3. **Database Setup:** The script is self-contained and will create the `friendships_schema` database upon execution.