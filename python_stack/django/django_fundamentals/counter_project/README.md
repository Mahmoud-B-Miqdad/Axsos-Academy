<div align="center">

# 🚀 Backend Development: Session Counter Application
**State Management, Session Handling, Persistent Data & Form Increments**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Backend](https://img.shields.io/badge/Focus-Session_%26_State-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project demonstrates stateless-to-stateful architecture implementation using Django's built-in session engine. The goal was to build a secure clicker mechanism that monitors web activity through two independent counters: actual page views/visits and user-triggered custom counter logic. The application captures persistent cookies, manipulates active memory structures via POST requests, and implements comprehensive memory flushing techniques to demonstrate full state control.

---

## 🎯 Key Concepts
* **Session Persistence:** Leveraging server-side cookies to persist integer states across disparate server-client roundtrips.
* **POST-to-Redirect Pattern:** Isolating analytical manipulations inside dedicated execution routes (`/plus_two`, `/reset`) before using `redirect()` to guide safe UI updates without form re-submission anomalies.
* **Dynamic Form Increments:** Parsing raw string payloads into dynamic integers via `int(request.POST.get())` to enable client-defined modifications.
* **Session Cleansing & Destruction:** Using custom state deletion routines (`del request.session['key']`) to selectively wipe storage references without breaking underlying runtime threads.

---

## 🛠️ Implementation & Bonus Highlights
* **Ninja & Sensei Bonuses Achieved:**
    * **Independent Metrics Tracking:** Distinguished actual dashboard visits from arbitrary manual increment counters successfully.
    * **Dynamic Parameter Increments:** Built an advanced input terminal enabling users to process custom multi-step increments dynamically.
    * **Granular State Flushes:** Integrated dedicated UI controls triggering isolated structural resets alongside total engine flushes (`destroy_session`).
* **Visual & Structural Design:** Styled the dashboard using Bootstrap 5 alongside modular template inclusions (`{% load static %}`) to pull static CSS styling structures neatly.

---

## 🗂️ API Architecture Reference

| Endpoint | Method | Action | View Function | Redirection |
| :--- | :--- | :--- | :--- | :--- |
| `/` | GET | Displays visit/counter dashboard metrics and tracks true page loads | `index` | *None (Renders template)* |
| `/plus_two` | POST | Automatically increments user counter metric by step value of 2 | `plus_two` | Redirects to `/` |
| `/custom_increment` | POST | Extracts specified user input and increments counter dynamically | `custom_increment` | Redirects to `/` |
| `/reset` | POST | Directs the active manual counter tracker back to absolute zero | `reset` | Redirects to `/` |
| `/destroy_session` | POST | Clears both cookie hashes entirely from backend system storage | `destroy_session` | Redirects to `/` |

---

## 🚀 How to Explore
1. Fire up the local development engine using the terminal: `python manage.py runserver`.
2. Browse to `http://localhost:8000/` to register your initial page visit.
3. Reload the browser page directly to witness the **Page Visits** tracking mount autonomously.
4. Interact with the **+2**, **Increase** (with custom inputs), and **Reset** controllers to observe local session modifications.
5. Tap **Destroy Session** to trigger a total storage flush and verify the counters reset back to zero.