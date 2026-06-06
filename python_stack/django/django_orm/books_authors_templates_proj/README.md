<div align="center">

# 📚 Django Full-Stack: Books & Authors Hub (Many-to-Many UI Integration)
**Bi-directional M2M Mapping, Dynamic Exclusion Dropdowns, Dual Cockpit Routing & Contextual Database Bridging**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Many__To__Many__UI-darkblue?style=for-the-badge)

</div>

---

## 📝 Description
This project delivers a sophisticated full-stack dynamic interface wrapped over a complex Many-to-Many database schema using Django's MTV architecture. Transitioning away from sandboxed shell operations into production-ready web dashboards, the platform exposes two unified management consoles: the **Books Index** and the **Authors Index**. Each dashboard allows live record insertion into its respective table, while supporting specialized target profile views. Through these views, users can bind relational assets together via HTML select elements using a fully-integrated backend junction controller.

---

## 🎯 Key Concepts & Objectives
* **Full-Stack M2M Infrastructure:** Exposing automated relational bridge tables directly to the UI layer for smooth end-to-end data processing.
* **Bi-directional Template Rendering:** Engineering symmetric templates where book cards query nested author profiles, and author cards list associated works via inverse lookups.
* **Post-Redirect-Get (PRG) Workflow:** Directing valid form ingestions into clear contextual routes to avoid accidental database duplicates during client reload actions.
* **Complex Multi-Model Traversal:** Injecting multiple independent database collections simultaneously inside unified template view context payloads.

---

## 🛠️ Implemented Features & Bonuses
* **Dual Admin Dashboards:** Dedicated operational cards to create new structural `Book` rows and `Author` items independently without configuration dependencies.
* **Interconnected Detail Layouts:** Specialized individual profile pages (`show_book` and `show_author`) that aggregate primary metadata alongside active relational rosters.
* **🔥 SENSEI BONUS (Dynamic Association Filter):** Integrated advanced query parameters within controllers using Django's structural filter exclusions (`.exclude(id__in=...)`). This logic recalculates the database contents dynamically so that select dropdown lists **only** display entities *not yet associated* with the active record, keeping the data clean.

---

## 🗂️ API Architecture & Routing Reference

| Web Path Endpoint | Allowed Request Method | Triggered Core Controller | Operational System Behavior |
| :--- | :--- | :--- | :--- |
| `/` | GET | `views.index` | Renders the main Books dashboard showing all books, models, and creation forms. |
| `/books/create` | POST | `views.create_book` | Processes input data fields to commit a new persistent `Book` row. |
| `/books/<int:book_id>` | GET | `views.show_book` | Displays specific book parameters, co-authors, and filtered eligibility select fields. |
| `/books/<id>/add_author` | POST | `views.add_author_to_book` | Bridges a chosen author record to the current book within the junction table. |
| `/authors` | GET | `views.authors_index` | Renders the primary Authors dashboard with a listing table and creation forms. |
| `/authors/create` | POST | `views.create_author` | Processes input data fields to commit a new persistent `Author` row. |
| `/authors/<int:author_id>` | GET | `views.show_author` | Displays specific author metadata, compiled books bibliography, and filtered select menus. |
| `/authors/<id>/add_book` | POST | `views.add_book_to_author` | Bridges a chosen book record to the current author within the junction table. |

---

## 🚀 How to Explore
1. Prepare initial database models and map blueprints inside your workspace terminal:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Initialize local server instances:
    ```bash
    python manage.py runserver  
    ```