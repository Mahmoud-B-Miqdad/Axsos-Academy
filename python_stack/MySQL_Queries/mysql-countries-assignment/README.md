<div align="center">

# 🌍 MySQL Queries: World Database Exploration
**Data Retrieval, Filtering & Aggregation Analysis**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Complex_Queries-blue?style=for-the-badge)

</div>

---

## 📝 Description
This project focuses on extracting meaningful insights from a relational database containing global geographic and demographic data. I authored a series of optimized SQL queries to solve specific business questions, ranging from simple data filtering to complex multi-table joins and groupings.

---

## 🎯 Key SQL Concepts Applied
* **Multi-Table Joins:** Connecting `countries`, `cities`, and `languages` using `INNER JOIN` and `LEFT JOIN` to consolidate related information.
* **Aggregations:** Utilizing `COUNT()` and `GROUP BY` to generate summary reports, such as city counts per country and country counts per region.
* **Complex Filtering:** Applying multiple conditional clauses (`WHERE`) with logical operators to isolate data based on population, surface area, and government forms.
* **Data Ordering:** Implementing `ORDER BY` to present the most relevant records first (e.g., sorting by population or percentage in descending order).

---

## 🛠️ Query Highlights
The solution covers 8 distinct analytical tasks, including:
1. **Linguistic Analysis:** Identifying countries where specific languages are spoken.
2. **Demographic Filtering:** Isolating high-population cities within specific districts and countries.
3. **Geopolitical Reports:** Categorizing countries by government types and life expectancy thresholds.
4. **Regional Summaries:** Providing a high-level view of global distribution by region.

---

## 🚀 How to Explore
1. **SQL Script:** Open the `countries_queries.sql` file to view the structured and commented queries.
2. **Execution Results:** Navigate to the `/screenshots` folder to see the output tables for each query as executed in MySQL Workbench.
3. **Database Setup:** Ensure you have the `world` database schema imported into your MySQL server before running the script.