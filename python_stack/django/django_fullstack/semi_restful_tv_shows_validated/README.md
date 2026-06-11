<div align="center">

# 📺 Django Full-Stack: Validated TV Shows Portal (Fat Model & AJAX Integration)
**Custom Model Managers, Structural Integrity Constraints, Dynamic Temporal Validations & AJAX Asynchronous Handshakes**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Database](https://img.shields.io/badge/Focus-Fat__Model__&__AJAX-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project delivers an advanced, production-ready backend framework designed to enforce strict business logic and data sanitation rules using Django's **Fat Model / Skinny Controller** architectural pattern. Extending the semi-restful CRUD platform, this iteration insulates the underlying database using a custom `ShowManager` subsystem. The system intercepts inbound POST parameters to execute comprehensive validations—ranging from basic character length thresholds to historical timeline checks and case-insensitive uniqueness constraints—while providing an asynchronous gateway for instant real-time feedback.

---

## 🎯 Key Concepts & Objectives
* **Fat Model Architecture:** Decoupling validation and transactional procedures away from view controllers by encapsulating data manipulation directly inside custom `models.Manager` classes.
* **Temporal Integrity Constraints:** Normalizing, parsing, and verifying user-submitted date logs against continuous server-side runtimes to reject forward-dated entries.
* **Case-Insensitive Uniqueness Indexes:** Executing database lookups using advanced query modifiers (`title__iexact=title`) to intercept conflicting or redundant titles before record mutations.
* **Asynchronous UX Validation Handshakes:** Serving dedicated endpoints designed to process inline UI verification tasks via asynchronous background calls.

---

## 🛠️ Implemented Features & Bonuses
* **Custom Validation Engine:** Built an error matrix router tracking specific input failures, preserving form states, and delivering tailored messaging to client interfaces.
* **⚡ NINJA BONUS (Past Timeline & Optional Length Gates):** * Enforces that all broadcast premiere entries must strictly reside in past historical timelines (`release_date < today`).
  * Transforms the `description` attribute into an optional parameter while maintaining a minimum 10-character quality threshold if supplied.
* **🔥 SENSEI BONUS (Global Title Uniqueness & AJAX Engine):**
  * Configured multi-scenario filter exclusion engines (`.exclude(id=show_id)`) allowing smooth title reuse preservation during updates, but blocking conflict creation across new rows.
  * Developed an asynchronous web gateway (`/shows/validate-ajax/`) that listens to live blur inputs on form fields to display validation warnings instantly before submittal.

---

## 🗂️ Unified API Routing Layout

| Web Path Endpoint | Allowed Method | Triggered Action Method | System Operational Behavior |
| :--- | :--- | :--- | :--- |
| `/` | GET | `views.root_redirect` | Root controller interceptor pushing traffic to primary dashboards. |
| `/shows/` | GET | `views.index` | Renders the primary database log listing table view. |
| `/shows/new/` | GET | `views.new_show` | Renders a clean structural creation form panel. |
| `/shows/create/` | POST | `views.create_show` | Routes fields through the Model Manager to commit new rows or bounce validation errors. |
| `/shows/<int:show_id>/` | GET | `views.show_detail` | Pulls out individual parameters and descriptive logs for a specific instance. |
| `/shows/<id>/edit/` | GET | `views.edit_show` | Pre-populates the structural layout form with active entity parameters. |
| `/shows/<id>/update/` | POST | `views.update_show` | Invokes targeted manager routines to safely apply edits or return feedback. |
| `/shows/<id>/destroy/` | POST / GET | `views.destroy_show` | Purges targeted structural items from active persistence memory pools. |
| `/shows/validate-ajax/` | GET / POST | `views.validate_ajax` | **Asynchronous Hub:** Returns instant JSON-serialized validation states to live client views. |

---

## 🚀 How to Explore
1. Track schema enhancements and commit field adjustments within your project terminal:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Spawn local developer engines:
    ```bash
    python manage.py runserver
    ```
3. Connect client browsers targeting the root endpoint `http://localhost:8000/`.
4. Fill out the creation form to view error triggers when title constraints or future dates are supplied.
5. Notice how fields evaluate themselves instantly through the AJAX SENSEI BONUS framework as you move from one form control to the next.