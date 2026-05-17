<div align="center">

# 🚀 Backend Development: Great Number Game
**Session State Management, Algorithmic Validation, Conditionals & Defensive Routing**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Backend](https://img.shields.io/badge/Focus-Game_Logic_%26_Sessions-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project implements the "Great Number Game," a web-based, real-time numerical guessing simulation driven by Django's stateful session engine. The system generates a pseudo-random target number between 1 and 100 upon engine initialization. It processes user payloads via POST requests, updates attempt tracks against strict thresholds, updates dynamic color alert states based on context, and introduces defensive controls to lock or reset gameplay when win/loss boundaries are met.

---

## 🎯 Key Concepts
* **Pseudo-Random Engine Coupling:** Utilizing Python's native `random.randint(1, 100)` logic encapsulated within session initialization cycles to maintain isolated target states.
* **Algorithmic Match Evaluation:** Designing multi-branch evaluation matrix structures (`if/elif/else`) to instantly determine low, high, or precise numeric matches.
* **State-Driven UI Mutation:** Mutating element wrapper attributes natively by injecting contextual Bootstrap styling parameters (`bg-danger`, `bg-success`) straight out of server memory storage arrays.
* **Defensive Route Guards:** Building structural validation rules inside data views to prevent post-completion interactions and lock active forms once the game loop hits its logical terminal block.

---

## 🛠️ Implementation & Bonus Highlights
* **Ninja & Sensei Bonuses Achieved:**
    * **Strict Attempt Thresholds:** Integrated an incremental tracking system limiting the client to a maximum of 5 attempts before enforcing a structural "Game Over" penalty.
    * **Dynamic Form Toggling:** Handled template conditioning rules (`{% if not request.session.game_over %}`) to automatically hide the input panel once user parameters resolve.
    * **Full Storage Purging:** Utilized Django's atomic session purging mechanism (`request.session.flush()`) to wipe backend records cleanly and re-instantiate identical state templates during new runs.

---

## 🗂️ API Architecture Reference

| Endpoint | Method | Action | View Function | Redirection |
| :--- | :--- | :--- | :--- | :--- |
| `/` | GET | Initiates random state metrics and displays active guessing canvas | `index` | *None (Renders template)* |
| `/guess` | POST | Extracts user digit inputs, steps attempt metrics, and tests boundaries | `guess` | Redirects to `/` |
| `/reset` | GET/POST | Flushes persistent session slots cleanly to reset game variables | `reset` | Redirects to `/` |

---

## 🚀 How to Explore
1. Fire up the local development engine using your terminal console: `python manage.py runserver`.
2. Direct your browser address to: `http://localhost:8000/`.
3. Input your logical numeric guess parameter (restricted gracefully between 1 and 100) and press **Submit**.
4. Observe the color-coded outcome notification wrappers defining current parameter positioning variables ("Too high!", "Too low!").
5. Secure a matching victory within **5 moves** to reveal the success board, or trigger the attempt capacity threshold to face the custom failure loop.
6. Click **Play again!** to instantly dispatch a `flush()` directive and spin up a completely fresh randomized track.