<div align="center">

# 🌐 Python Web: Flask Routing & Parameters
**Mastering Dynamic URL Handling**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Flask_Routing-black?style=for-the-badge)

</div>

---

## 📝 Description
This assignment builds upon the basic Flask server by implementing **Dynamic Routing**. I learned how to capture variables directly from the URL (like names and IDs) and use them within my Python functions. This is a fundamental concept for building RESTful APIs and personalized web experiences.



---

## 🎯 Key Concepts
* **Dynamic Route Parameters:** Using `<variable>` syntax in `@app.route()` to define placeholders in the URL.
* **Function Arguments:** Passing those URL placeholders directly as arguments to the corresponding Python view functions.
* **Multiple Parameters:** Handling more than one dynamic value in a single route (e.g., `/users/<username>/<id>`).
* **Route Mapping:** Managing multiple endpoints (`/`, `/success`, `/hello/<name>`, `/users/<username>/<id>`) within a single application.

---

## 🛠️ Implementation Highlights
* **Flexible URLs:** The server can now respond dynamically to different inputs without needing hardcoded routes for every possibility.
* **Server-Side Printing:** Using `print()` inside routes to log received data to the console for easier debugging during the development phase.

---

## 🚀 How to Run
1. Ensure `flask` is installed:
   ```bash
   pip install flask
    ```
2. Run the server:

   ```bash
   python server.py
    ```

3. Test the different routes in your browser:

- http://127.0.0.1:5000/
- http://127.0.0.1:5000/success
- http://127.0.0.1:5000/hello/Mahmoud
- http://127.0.0.1:5000/users/Miqdad/1