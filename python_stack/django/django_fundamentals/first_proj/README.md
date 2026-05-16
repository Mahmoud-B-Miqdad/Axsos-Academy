<div align="center">

# 🚀 Backend Development: First Django Project
**URL Routing, Dynamic Parameters, HTTP Redirects & JSON Responses**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Backend](https://img.shields.io/badge/Focus-Routing_%26_Views-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project marks the initial step into full-stack backend development using the Django framework. The objective was to spin up a new Django ecosystem, instantiate a specialized core application (`blogs_app`), and build a comprehensive URL routing layout. The project cleanly demonstrates how incoming HTTP requests map to view logic, handles dynamic path variables, executes safe client-side redirects, and delivers structured JSON payloads for API consumption.

---

## 🎯 Key Concepts
* **App-Level Routing Isolation:** Decoupling routing logic by keeping configuration locally within the application (`urls.py`) rather than overcrowding the root project configuration.
* **Dynamic Route Parameters:** Utilizing path converters like `<int:number>` to capture variables directly from the URL and feed them into controller views.
* **HTTP Redirect Flows:** Leveraging `redirect()` to guide navigation paths smoothly between data submission endpoints and display feeds.
* **RESTful JSON Delivery:** Serving raw data using `JsonResponse` to support API standards instead of standard HTML text rendering.

---

## 🛠️ Implementation Highlights
* **Routing Strategy (`urls.py`):** Structured an organized list of patterns managing 8 distinctive routes cleanly matching the strict checklist requirements.
* **Functional View Logic (`views.py`):**
    * **Redirection Controllers:** Configured `/` to auto-forward to `/blogs`, and the creation handler (`/blogs/create`) to guide users back to the root application path.
    * **Dynamic Placeholders:** Crafted modular views (`show`, `edit`, `destroy`) accepting an integer parameter to simulate targeted CRUD functionalities on specific posts.
    * **Bonus Endpoint:** Implemented native Python dictionaries processed via `JsonResponse` to spit out standard structured web content.

---

## 🗂️ API Architecture Reference

| Endpoint | Method | Action | View Function |
| :--- | :--- | :--- | :--- |
| `/` | GET | Redirects to `/blogs` | `root` |
| `/blogs` | GET | Displays main blog index feed | `index` |
| `/blogs/new` | GET | Displays form placeholder to make a blog | `new` |
| `/blogs/create` | POST/GET | Redirects back to `/` | `create` |
| `/blogs/<number>` | GET | Dynamically displays details for a specific blog | `show` |
| `/blogs/<number>/edit` | GET | Displays an edit form placeholder for a specific blog | `edit` |
| `/blogs/<number>/delete` | GET/POST | Deletes the post and redirects back to `/blogs` | `destroy` |
| `/blogs/json` | GET | Returns a structured JSON dictionary package | `json_response` |

---

## 🚀 How to Explore
1. Make sure you have **Django** installed, then run the development server via terminal: `python manage.py runserver`.
2. Open your browser and point it to `http://localhost:8000/` to watch the auto-redirect to `/blogs` take place instantly.
3. Test dynamic variables by manually visiting `http://localhost:8000/blogs/15` and check the string injection.
4. Hit `http://localhost:8000/blogs/json` to see raw API content output formatted natively in JSON.