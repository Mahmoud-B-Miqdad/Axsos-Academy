<div align="center">

# ♟️ Python Web: Dynamic Checkerboard
**Advanced Jinja2 Logic and Static File Management**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Jinja2_Logic-black?style=for-the-badge)

</div>

---

## 📝 Description
In this project, I built a dynamic checkerboard generator. The core objective was to use **Nested Loops** in Jinja2 to create a grid of boxes, and **Conditional Logic** (`if/else`) to alternate colors based on the row and column index. Additionally, I implemented static file management to serve external CSS stylesheets.



---

## 🎯 Key Concepts
* **Nested Loops in Jinja2:** Using `{% for row in range(y) %}` inside another loop for `col` to render a 2D grid structure.
* **Modular Arithmetic:** Using the modulo operator `(row + col) % 2 == 0` to determine the alternating pattern (checkerboard effect) for the colors.
* **Conditional Templating:** Implementing `{% if %}`, `{% elif %}`, and `{% else %}` blocks to switch between different color themes (Red/Black vs. Green/White).
* **Static Asset Management:** Utilizing `url_for('static', filename='...')` to correctly link CSS files, ensuring the application follows Flask's best practices for static file serving.

---

## 🛠️ Implementation Highlights
* **Dynamic Grid Size:** The board size is fully configurable via the URL parameters `x` and `y`.
* **State Management:** The server uses default arguments (`color="red"`, `x=8`, `y=8`) to ensure the board renders correctly even with minimal URL inputs.
* **Separation of Concerns:** Logic resides in `server.py`, structure in `index.html`, and design in `style.css`.

---

## 🚀 How to Run
1. Ensure your directory structure is as follows:
   ```text
   /project_folder
   ├── server.py
   ├── static/
   │   └── css/
   │       └── style.css
   └── templates/
       └── index.html
    ```

2. Run the server:

   ```bash
   python server.py
    ```

3. Test the different routes in your browser:

- http://127.0.0.1:5000/red
- http://127.0.0.1:5000/green/10/10
- http://127.0.0.1:5000/red/4/4