<div align="center">

# 📺 Django Full-Stack: Semi-Restful TV Shows Hub (Full CRUD Automation)
**Complete Database CRUD Integration, RESTful Routing Architecture, Dynamic Context Forms & Data Persistence**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Full__CRUD__Application-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project delivers a robust, full-stack enterprise wrapper designed to handle complete programmatic **CRUD (Create, Read, Update, Delete)** operations inside Django's MTV layer. Modeled around a dynamic `Show` entity tracking television broadcasts, networks, and release timelines, the system maps clean RESTful routing pathways to dedicated graphical interfaces. Users can seamlessly query the global persistent infrastructure, spawn new elements through interactive HTML forms, parse relational detail nodes, modify live runtime instances, and cleanly flush data records out of active storage.

---

## 🎯 Key Concepts & Objectives
* **Semi-Restful Routing Paradigms:** Structuring clean, standardized URI path structures mapped logically to target controller actions for predictable web operations.
* **Full CRUD Data Matrix:** Engineering end-to-end data pipelines covering record Creation, Retrieval, Updates, and Destruction.
* **Context Form Hydration:** Pre-populating HTML update components dynamically with real-time persistent data snapshots mapped directly from specific database rows (`Show.objects.get(id=id)`).
* **Robust Temporal Tracking:** Formatting and parsing date metadata configurations safely using specialized database core fields (`models.DateField`).

---

## 🛠️ Implemented Features & Core Operations
* **Global Aggregation Display:** A unified landing catalog featuring reactive listing blocks summarizing active TV shows alongside targeted action controls.
* **Symmetrical Add/Edit Workspaces:** Two decoupled form components: one for clean multi-field input insertion, and another specialized workspace for handling live dynamic record modifications.
* **Instance Profile Closures:** Individual detailed cards revealing specific production networks, historical release timestamps, and descriptive summaries.
* **Administrative Data Purging:** Integrated precise transactional actions triggering instant row removal parameters from the backend persistence layer.

---

## 🗂️ RESTful API Routing & Architecture

| Web Path Endpoint | Allowed Request Method | Triggered Core Controller | Operational System Behavior |
| :--- | :--- | :--- | :--- |
| `/` | GET | `views.index` | Renders the primary workspace cockpit showing a matrix list of all records. |
| `/new` | GET | `views.new` | Generates a clean, blank structural form card to insert a brand new show. |
| `/create` | POST | `views.create` | Ingests multi-input parameters to commit a new persistent `Show` row. |
| `/<int:show_id>` | GET | `views.show` | Extracts and displays individual comprehensive profile logs for a specific target. |
| `/<int:show_id>/edit` | GET | `views.edit` | Renders the update form card pre-populated with active object properties. |
| `/<int:show_id>/update` | POST | `views.update` | Validates and saves field modifications to overwrite existing database items. |
| `/<int:show_id>/destroy` | POST / GET | `views.destroy` | Processes transactional database updates to instantly purge the targeted row. |

---

## 🚀 How to Explore
1. Run structural schema initialization flags inside your project terminal terminal:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Spawn the Django framework interactive local server:
    ```bash
    python manage.py runserver
    ```
3. Connect your terminal browser to the core root dashboard: `http://localhost:8000/`.
4. Click on Add a New Show to create fresh data points, select Edit to modify details, and explore the Delete actions to watch the database flush and sync elements dynamically in real time.