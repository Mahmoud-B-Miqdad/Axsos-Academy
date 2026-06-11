<div align="center">

# 🎓 Django Full-Stack: Bootcamp Courses Hub (One-to-One & AJAX Architecture)
**Strict One-to-One Decoupling, Model Manager Validations, Hierarchical Comment Matrices & Async AJAX Destructors**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Database](https://img.shields.io/badge/Focus-One__To__One__&__AJAX-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project delivers an enterprise-grade academic course manager tracking developer bootcamp tracks using Django's structural MTV framework. Rather than storing large textual definitions inside the primary table, this architecture implements a strict **One-to-One (1:1)** field abstraction to decouple heavy course definitions into an isolated persistence layer. Driven by a dedicated `CourseManager` model operator, the system intercepts inbound parameters to enforce business character thresholds, supports recursive nested **One-to-Many (1:M)** feedback rows, and leverages asynchronous operational workflows to execute clean object removal.

---

## 🎯 Key Concepts & Objectives
* **Isolated One-to-Many Abstraction:** Implementing specialized database-level bindings via `models.OneToOneField` to cleanly split core entity tables from heavy textual meta-attributes.
* **Model-Tier Validation Isolation:** Utilizing centralized custom managers (`CourseManager`) to audit string metrics before allocating database memory slots.
* **Dependent Entity Cascade Chains:** Configuring downstream integrity configurations (`on_delete=models.CASCADE`) to guarantee that wiping a parent row automatically flushes descriptions and sub-comments.
* **Asynchronous UX Destruction:** Serving atomic endpoints designed to execute table row drops over network transactions without forcing full client page recycles.

---

## 🛠️ Implemented Features & Bonuses
* **Atomic Ingestion Matrix:** Bundled transaction handler (`create_course_with_desc`) that seeds both the `Course` parent row and the associated `Description` record simultaneously.
* **⚡ NINJA BONUS (Relational Description Separation & Comments):** * Extracted descriptions completely into an independent data class mapped cleanly back via custom related lookups (`course.desc_info`).
  * Appended a fully operational recursive `Comment` subsystem allowing students to attach multiple text feedback records directly onto specific courses.
* **🔥 SENSEI BONUS (Asynchronous Modal-Driven AJAX Elimination):**
  * Developed a reactive asynchronous endpoint (`/courses/<id>/delete-ajax/`) that connects directly with frontend script handlers. This allows users to confirm removal within a dynamic modal and immediately fades out the target entry without refreshing the DOM.

---

## 🗂️ Unified API Routing Layout

| Web Path Endpoint | Allowed Method | Triggered Action Method | System Operational Behavior |
| :--- | :--- | :--- | :--- |
| `/` | GET | `views.index` | Renders the cockpit board featuring creation interfaces and listing logs. |
| `/courses/create/` | POST | `views.create_course` | Routes fields through the manager to evaluate properties and allocate rows. |
| `/courses/<int:course_id>/destroy/` | POST / GET | `views.destroy_course` | Standard RESTful navigation pathway rendering confirmation layouts. |
| `/courses/<int:course_id>/comments/` | GET / POST | `views.course_comments` | Dedicated hub managing nested multi-row feedback logs for specific entries. |
| `/courses/<id>/delete-ajax/` | POST / DELETE | `views.delete_course_ajax` | **Asynchronous Hub:** Purges database parameters instantly and emits JSON sync codes. |

---

## 🚀 How to Explore
1. Update database storage schemas to apply multi-table blueprints:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Fire up the local development runtime:
     ```bash
    python manage.py runserver
     ```
3. Connect client browsers targeting the local portal endpoint: `http://localhost:8000/`.
4. Test the validation gate by submitting a course name under 5 characters or descriptions under 15 characters to view custom model error payloads.
5. Click Remove to activate the SENSEI BONUS AJAX Modal Framework and watch entries clean themselves up live from the data dashboard grid.
