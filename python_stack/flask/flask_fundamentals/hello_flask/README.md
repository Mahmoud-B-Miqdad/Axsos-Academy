<div align="center">

# 🌐 Python Web: Intro to Flask
**Building Your First Web Server**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Flask_Web_Framework-black?style=for-the-badge)

</div>

---

## 📝 Description
This assignment introduces the basics of server-side web development using the **Flask** micro-framework. I created a simple application that defines a route and serves a response, providing the fundamental understanding of how web requests and responses work in a Python environment.



---

## 🎯 Key Concepts
* **Flask Application Object:** The `app` instance is the central object that handles all requests and configurations.
* **Routing:** Using the `@app.route('/')` decorator to map a URL pattern to a specific Python function.
* **Development Mode:** Using `debug=True` to enable hot-reloading and helpful error messages, which is essential during development.
* **The Entry Point:** The `if __name__ == "__main__":` block ensures the server only runs if the file is executed directly.

---

## 🛠️ Implementation Highlights
* **Web Server Interaction:** The code demonstrates the cycle of a browser making a request to the root URL and the server returning a string response.
* **Decorators:** Learning how Python decorators modify the behavior of functions (linking them to URLs).

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

3. Open your browser and navigate to http://127.0.0.1:5000/.