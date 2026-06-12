<div align="center">

# 📚 Django Full-Stack: Favorite Books Management Hub (M2M & Authorization Guards)
**Multi-Relational DB Blueprints, Secure Ownership Validation Barriers, Cascading One-to-Many Layouts & Many-to-Many Toggle Systems**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Authorization__Guards-red?style=for-the-badge)
![Database](https://img.shields.io/badge/Focus-Many__To__Many__Toggles-darkblue?style=for-the-badge)

</div>

---

## 📝 Description
This project implements a comprehensive **Favorite Books Management Ecosystem** built on top of Django's MTV model, combining strict account identity layers with complex, overlapping entity connections. Moving beyond basic data storage, this architecture defines two distinct relationship bounds between users and content records: a singular ownership bridge (**One-to-Many**) tracking the profile that initially spawned the record, and a dynamic interest network (**Many-to-Many**) governing user-curated catalogs. Powered by isolated model managers (`BookManager` and `UserManager`), the system blocks data injection by embedding authorization locks within the database communication layer.

---

## 🎯 Core Engineering Lessons & Objectives
* **Hybrid Structural Relations:** Implementing dual-purpose architecture where an entity (`Book`) simultaneously holds a foreign key pointer (`uploaded_by`) and a multi-directional junction table relationship (`users_who_like`) mapping back to the same class (`User`).
* **Model-Tier Authorization Barriers:** Moving access permissions away from routing handlers into model managers (`update_book`). This ensures database query modifications are automatically blocked if the active user ID fails the record ownership challenge.
* **Atomic Double-Action Ingestion:** Programming complex creation pipelines (`create_book`) that safely generate a new database row and immediately map its primary key into the junction tracking workspace within a single transactional lifecycle.
* **Bi-Directional Status Toggling:** Creating parameter-driven views (`toggle_favorite`) that dynamically append (`.add()`) or decouple (`.remove()`) relational rows inside database junction maps.

---

## 🛠️ Implemented Features & Architecture Breakdown

### 1. Robust Identity & Protection Layers
* **Secure Access Framework:** Uses encrypted password processing via **Bcrypt** alongside isolated session checks to lock out public access to dashboard portals.
* **Compliance Checks:** Evaluates incoming demographics using chronological date parsing to guarantee strict **COPPA 13+ compliance** before writing records.

### 2. Relational Content Matrix & Controls
* **Implicit Creator Cataloging:** Automatically binds newly registered book rows to the active user profile, eliminating hidden form manipulation flaws.
* **Granular Profile Workspaces:** Specialized view layout engines that determine interface elements dynamically:
  * **Owners:** Granted exclusive permissions to alter parameters or purge records entirely from persistence layers.
  * **Contributors/Guests:** Displayed read-only overview fields equipped with conditional toggle parameters to adjust favorite statuses.
* **🔥 SENSEI & NINJA BONUS (Unified Toggle Control & Personal Catalogs):**
  * Integrated a clean, string-action parameterized pathway (`favorite/<str:action>`) to handle item pinning and unpinning gracefully through a single backend endpoint.
  * Configured a custom query index dashboard (`/favorites`) designed to pull and isolate a user's unique list of liked books on demand.

---

## 🗂️ Unified API Routing Layout

| Web Path Endpoint | HTTP Method | Target Controller Action | Operational System Behavior |
| :--- | :--- | :--- | :--- |
| `/` | GET | `views.index` | Renders split authentication portals handling core account registration & access verification. |
| `/register` | **POST Only** | `views.register` | Validates onboarding data, hashes inputs via Bcrypt, and initialises active user sessions. |
| `/login` | **POST Only** | `views.login` | Tests credentials against stored hashes to grant dashboard entry permissions. |
| `/logout` | GET / POST | `views.logout` | Clears structural session records and signs out the current active profile. |
| `/books` | **GET Protected**| `views.books_index` | **Primary Hub:** Compiles the primary global catalog, add-book views, and full community libraries. |
| `/books/add` | **POST Only** | `views.add_book` | Processes input data fields to insert a book row and pin it to user favorites. |
| `/books/<int:book_id>` | **GET Protected**| `views.book_detail` | Detailed view route that analyzes record ownership to display update blocks or basic metadata lists. |
| `/books/<id>/update` | **POST Only** | `views.update_book` | **Secured:** Triggers manager verification barriers to safely modify book properties. |
| `/books/<id>/delete` | POST / GET | `views.delete_book` | **Secured:** Permanently purges a book record from database tables (Allowed for owners only). |
| `/books/<id>/favorite/<str:action>`| GET / POST | `views.toggle_favorite` | ** Junc Table Operator:** Processes string actions (`add`/`remove`) to update active table structures. |
| `/favorites` | **GET Protected**| `views.my_favorites` | Extracts and renders a dedicated community listing showing only the current user's liked items. |

---

## 🛡️ Security Validation & Integrity Proofs

### The Cross-User Infiltration Attack Simulation
1. Log in with **User A** and create a specific book instance (e.g., *ID: 42*).
2. Log out and re-authenticate as **User B**.
3. Attempt to bypass front-end view restrictions by firing an explicit terminal `POST` payload or typing directly into the URL path: `http://localhost:8000/books/42/update`.
4. Notice how your backend custom manager (`update_book`) intercepts the context, checks ownership metrics (`book_to_edit.uploaded_by.id == user_id`), rejects execution, and returns an unauthorized warning message without modifying database records.

---

## 🚀 Quickstart Installation
1. Apply relational schema adjustments to generate user, catalog, and joint tracking rows:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Spawn the development local background runtime engine:
   ```bash
   python manage.py runserver
   ```
3. Open your browser environment targeting `http://localhost:8000/`.
4. Register accounts to test the Many-to-Many junction mapping systems and watch the ownership control boards adapt perfectly in real time.