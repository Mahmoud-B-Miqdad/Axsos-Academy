<div align="center">

# 🚀 Backend Development: Ninja Gold Game
**Session Array Manipulation, Hidden Form Elements, State Logging & Win/Loss Boundaries**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Backend](https://img.shields.io/badge/Focus-Session_Arrays_%26_Logs-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project implements the "Ninja Gold Game," a mini-RPG strategy simulation that tests complex data state mutations within Django's session architecture. The app utilizes a multi-form canvas embedded with secure hidden parameters. Each form triggers randomized currency generation matrices (with both positive earnings and negative gamble structures), maps events into timestamps, pushes nested status maps into real-time history logs, and evaluates endgame boundaries based on goal wealth or limited move allowances.

---

## 🎯 Key Concepts
* **Hidden Element Parameters:** Passing targeted application data dynamically using `<input type="hidden">` tags inside independent forms to isolate backend routes seamlessly.
* **Complex Data Objects in Sessions:** Modifying server storage to manage composite multi-nested array sets (`request.session['activities']`) rather than just simple numerical types.
* **Chronological Insertion Sorting:** Injecting real-time string payloads using `.insert(0, activity)` to force a top-down reverse-chronological event timeline display.
* **Multi-Conditional Loop Terminals:** Designing logical gateways that continuously test dynamic conditions (e.g., reaching 500 gold or executing 15 moves) to lock out forms and declare terminal match conclusions.

---

## 🛠️ Implementation & Sensei Highlights
* **Sensei Requirements Achieved:**
    * **Move Limit & Win Thresholds:** Enforced strict game metrics limiting users to exactly 15 action loops or a 500 gold win condition.
    * **Dynamic Style Injections:** Rendered context-specific Bootstrap colors (`text-success`, `text-danger`) based on transactional outcomes.
    * **Interactive History Tracker:** Created a scrollable overflow log wrapper showcasing chronological records combined with exact system execution timestamps.
    * **Form Defensive Toggling:** Leveraged Django conditional attributes (`{% if request.session.game_over %}`) to automatically disable interactive inputs upon hitting completion states.

---

## 🗂️ API Architecture Reference

| Endpoint | Method | Action | View Function | Redirection / Render |
| :--- | :--- | :--- | :--- | :--- |
| `/` | GET | Builds base game tracking structures and displays primary gold canvas | `index` | *None (Renders template)* |
| `/process_money` | POST | Extracts hidden form values, executes random reward rolls, and logs outputs | `process_money` | Redirects to `/` |
| `/reset` | GET/POST | Flushes persistent session states completely to reboot application parameters | `reset` | Redirects to `/` |

---

## 🚀 How to Explore
1. Fire up the local development engine through your terminal room: `python manage.py runserver`.
2. Browse your local address target: `http://localhost:8000/`.
3. Select your location form strategy choice (**Farm**, **Cave**, **House**, or **Casino**) and click **Find Gold!**.
4. Monitor your interactive **Moves** counter and observe the real-time activity log append updates instantly.
5. Aim to hit the **500 gold** threshold to declare a victory loop before burning through your **15 maximum moves allowance**.
6. Press the **Reset Game** control to flush existing active arrays and reboot back to absolute starting default states.