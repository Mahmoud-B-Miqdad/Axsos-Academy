<div align="center">

# 🌐 Python Web: Flask Routing Mastery
**Mastering Converters and Error Handling**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Focus-Advanced_Routing-black?style=for-the-badge)

</div>

---

## 📝 Description
This assignment demonstrates more sophisticated routing techniques in Flask. I implemented route converters to enforce data types (e.g., ensuring a parameter is an integer) and added a global error handler to manage undefined routes, which is a crucial step in building robust web applications.



---

## 🎯 Key Concepts
* **URL Converters:** Using `<int:num>` to restrict URL parameters to specific data types, preventing errors before they reach the function.
* **String Multiplication:** Utilizing Python's powerful string manipulation `(word + " ") * num` to dynamically generate repetitive content.
* **Global Error Handling:** Using `@app.errorhandler(404)` to provide a user-friendly response when a requested route does not exist.
* **Dynamic Content Generation:** Returning processed strings directly based on URL parameters.

---

## 🛠️ Implementation Highlights
* **Data Validation:** By specifying `int` in the route, Flask automatically handles the conversion and returns a 404 if the input is not a number.
* **User Experience:** The custom 404 handler replaces the default browser error page with a helpful, custom message.

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
- http://127.0.0.1:5000/champion
- http://127.0.0.1:5000/say/Mahmoud
- http://127.0.0.1:5000/repeat/3/Hello
- http://127.0.0.1:5000/undefined_route (Triggers the 404 error handler)