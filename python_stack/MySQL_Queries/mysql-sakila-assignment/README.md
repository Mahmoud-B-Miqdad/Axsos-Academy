<div align="center">

# 🎬 MySQL Queries: Sakila Movie Database
**Advanced Relational Data Extraction & Multi-Join Analysis**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Relational_Integrity-red?style=for-the-badge)

</div>

---

## 📝 Description
This project showcases advanced SQL querying techniques using the famous **Sakila** database. The focus was on navigating through a complex web of relationships (Actors, Films, Categories, and Customers) to retrieve specific business insights. The queries demonstrate high proficiency in connecting multiple tables to build meaningful datasets.

---

## 🎯 Key SQL Concepts Applied
* **Deep Table Joins:** Navigating through up to 5 interconnected tables (e.g., `film` ↔ `film_actor` ↔ `actor` ↔ `film_category` ↔ `category`) to fulfill complex data requests.
* **Pattern Matching:** Utilizing the `LIKE` operator with wildcards (`%`) to filter specific data within "Special Features" strings.
* **Logical Data Filtering:** Combining multiple conditions using `AND`, `IN`, and equality operators to refine search results based on genres, ratings, and rental rates.
* **String Manipulation:** Using `CONCAT()` to merge first and last names for cleaner, professional-looking reports.

---

## 🛠️ Query Highlights
The solution addresses 8 rigorous analytical tasks:
1. **Customer Geography:** Locating customers based on specific city IDs.
2. **Genre-Specific Research:** Extracting all films categorized under "Comedy" or "Drama".
3. **Actor Portfolio Tracking:** Listing all movies associated with specific actors (e.g., Sandra Kilmer).
4. **Targeted Inventory Analysis:** Filtering films by rating and special features for specific store locations.

---

## 🚀 How to Explore
1. **SQL Script:** View the well-commented queries in the `sakila_queries.sql` file.
2. **Visual Proof:** Check the `/screenshots` folder for screenshots of the execution outputs, demonstrating the accuracy of each query.
3. **Database Environment:** These queries are designed to run on the standard **Sakila Sample Database**.