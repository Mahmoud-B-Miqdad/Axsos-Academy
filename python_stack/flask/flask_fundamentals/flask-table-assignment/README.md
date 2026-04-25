<div align="center">

# 📋 Python Web: Rendering Data Tables
**Managing Collections and Bootstrap Integration**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Jinja2_Collections-black?style=for-the-badge)

</div>

---

## 📝 Description
In this assignment, I learned how to pass complex data structures (a list of dictionaries) from the Flask backend to an HTML template. I then used **Jinja2** to iterate through this collection and render it into a clean, professional-looking table using **Bootstrap 5** for styling.



---

## 🎯 Key Concepts
* **Data Collections:** Handling lists of dictionaries (`users`), which simulates real-world data coming from a database.
* **Jinja2 Iteration:** Using the `{% for user in users %}` loop to dynamically generate table rows (`<tr>`) based on the data length.
* **Accessing Keys:** Retrieving specific dictionary values using bracket notation `user['first_name']` within the template.
* **Bootstrap Integration:** Leveraging CDN-based CSS frameworks to quickly implement modern, responsive table designs without writing extensive custom CSS.
* **Dynamic Concatenation:** Demonstrating the ability to manipulate data presentation within the view, such as combining fields to create a "Full Name" column.

---

## 🛠️ Implementation Highlights
* **Clean Templating:** The logic separates the data preparation (in `server.py`) from the presentation (in `index.html`).
* **Visual Hierarchy:** Used Bootstrap's `table-dark` header and `table-hover` classes to improve user readability and interaction.

---

## 🚀 How to Run
1. Ensure your directory structure is as follows:
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

- http://127.0.0.1:5000/table