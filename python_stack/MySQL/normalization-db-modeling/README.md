<div align="center">

# 🛠️ Database Design: Normalization Mastery
**Transforming Flat Data into Relational Excellence**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Database](https://img.shields.io/badge/Focus-3NF_Compliance-green?style=for-the-badge)

</div>

---

## 📝 Description
This project demonstrates the process of **Database Normalization**. I took an initial ERD that violated multiple normalization forms and redesigned it to ensure data integrity, eliminate redundancy, and optimize the storage of student information and their diverse interests.

---

## 🎯 Key Normalization Steps
*   **First Normal Form (1NF):** Eliminated the multi-valued `interests` field by moving it to a separate table, ensuring each column contains atomic values.
*   **Second Normal Form (2NF):** Ensured all non-key attributes are fully functional and dependent on the primary key.
*   **Third Normal Form (3NF):** Removed transitive dependencies. Specifically, I isolated address information (Street, City, Zip Code) into its own `addresses` table to ensure that non-key fields only depend on the primary key.

---

## 🛠️ Implementation Highlights
*   **Many-to-Many (M:M) Relationship:** Created the `student_interests` join table. This satisfies the requirement to track multiple interests per student and multiple students per interest without data duplication.
*   **Address Optimization:** Instead of having repetitive address lines in the `students` table, I established a dedicated `addresses` entity to centralize location data.
*   **Refined Entity Structure:**
    *   **Students:** Clean profile data linked via foreign keys to Dojos and Addresses.
    *   **Dojos:** Independent entity for training locations.
    *   **Interests:** A lookup table for unique hobbies/skills.
    *   **Student_Interests:** The bridge facilitating complex relationships.

---

## 🚀 How to Explore
1. **Compare Models:** Reference the "before" model in the assignment instructions versus my "after" model in the provided ERD.
2. **Trace the Links:** Look at the `student_interests` table to see how it resolves the Many-to-Many relationship which is a hallmark of a normalized database.
3. **Data Integrity:** Observe how changing a city name in the `addresses` table now updates all associated students automatically, preventing data anomalies.