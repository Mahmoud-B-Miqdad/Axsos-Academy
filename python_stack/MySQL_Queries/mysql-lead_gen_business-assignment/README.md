<div align="center">

# 📈 MySQL Analytics: Lead Gen Business Data Insights
**Business Intelligence & Advanced Report Generation**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Business_Intelligence-green?style=for-the-badge)

</div>

---

## 📝 Description
This project focuses on generating high-level business intelligence reports for a Lead Generation company. The objective was to extract actionable data regarding revenue, site performance, and lead generation efficiency. The queries showcase an advanced ability to aggregate data across multiple dimensions such as time, clients, and specific domains.

---

## 🎯 Key SQL Concepts Applied
* **Advanced Aggregations:** Using `SUM()`, `COUNT()`, and `GROUP BY` to calculate revenue and performance metrics across different timeframes.
* **String Aggregation (`GROUP_CONCAT`):** Consolidating multiple row values (like domain names) into a single field for cleaner administrative reports.
* **Complex Date Functions:** Extracting months and years from timestamps using `MONTHNAME()` and `YEAR()`, and filtering data within specific chronological ranges.
* **Multi-Dimensional Grouping:** Grouping results by multiple columns (e.g., Client ID + Year + Month) to provide granular monthly revenue breakdowns.
* **Advanced Joins:** Implementing `LEFT JOIN` to ensure data completeness, specifically for including sites that haven't generated leads yet.

---

## 🛠️ Query Highlights
The solution features 10 comprehensive business queries, including:
1. **Revenue Auditing:** Monthly total revenue reports for specific years.
2. **Client Performance:** Tracking lead generation volume per client within specific date ranges.
3. **Site Management:** Summarizing site ownership and creation frequency per month.
4. **Interactive Reporting:** Generating lists of all domains owned by a client in a single concatenated string.

---

## 🚀 How to Explore
1. **SQL Script:** Examine the `lead_gen_queries.sql` for the full logic and optimization techniques.
2. **Result Screenshots:** The `/screenshots` directory contains visual evidence of each query’s result set from MySQL Workbench.
3. **Analytical Flow:** The queries are ordered to follow a typical business reporting lifecycle, from simple summaries to deep-dive analytics.