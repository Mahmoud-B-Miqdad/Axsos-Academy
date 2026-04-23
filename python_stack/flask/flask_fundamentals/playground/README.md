<div align="center">

# 🎨 Python Web: Flask Playground
**Dynamic Content Rendering with Jinja2**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Jinja2_Templates-black?style=for-the-badge)

</div>

---

## 📝 Description
This assignment introduces the integration of **Flask** with **HTML templates**. Instead of returning static strings, I used the `render_template` function to dynamically generate web pages. I also utilized **Jinja2** templating logic (loops and inline CSS styles) to create a "Playground" that renders a variable number of boxes with custom colors based on URL parameters.



---

## 🎯 Key Concepts
* **`render_template`:** Serving HTML files located in the `templates` folder to the user.
* **Jinja2 Templating:** Using logic syntax like `{% for i in range(num) %}` directly inside HTML to generate dynamic content.
* **Inline CSS Injection:** Passing the `color` variable from Python to HTML to dynamically change the `background-color` style property.
* **Multi-Route Handling:** Using multiple decorators for a single function to handle different URL patterns (`/play`, `/play/<x>`, `/play/<x>/<color>`) seamlessly.

---

## 🛠️ Implementation Highlights
* **Dynamic Generation:** The page layout changes based on the URL inputs—the number of boxes and their colors are controlled entirely by the user through the URL.
* **Default Arguments:** The `play(x=3, color="lightblue")` function signature ensures the page works even if the user provides no parameters.

---

## 🚀 How to Run
1. Ensure the directory structure is as follows:
   ```text
   /project_folder
   ├── server.py
   └── templates/
       └── index.html
    ```

2. Run the server:

   ```bash
   python server.py
    ```

3. Test the different routes in your browser:

- http://127.0.0.1:5000/play (3 blue boxes)
- http://127.0.0.1:5000/play/5 (5 blue boxes)
- http://127.0.0.1:5000/play/8/red (8 red boxes)
