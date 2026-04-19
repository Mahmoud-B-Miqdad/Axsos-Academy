<div align="center">

# 🧪 Python Testing: MathDojo Unit Tests
**Automated Testing for Fluent APIs**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Testing](https://img.shields.io/badge/Focus-Unit_Testing-brightgreen?style=for-the-badge)

</div>

---

## 📝 Description
This assignment integrates unit testing with our custom `MathDojo` class. By using the `unittest` framework, I ensured the reliability of the chainable arithmetic methods. A key focus of this assignment was implementing `setUp()`, which initializes a fresh instance of the class before every individual test case, ensuring total isolation and accuracy.



---

## 🎯 Key Features
* **Isolated Environment:** The `setUp()` method guarantees that every test case starts with a new `MathDojo` instance, preventing data leakage between tests.
* **Complex Test Cases:** Validated that both individual method chains and complex, multi-operation chains (`add` and `subtract` combined) produce the mathematically correct `result`.
* **Assertion Testing:** Used `assertEqual` to verify that the internal state (`self.result`) matches the expected output after various operations.

---

## 🛠️ Key Concepts
* **Test Isolation:** The importance of resetting states before each test to maintain test independence.
* **`setUp` Method:** A specialized `unittest` lifecycle method that automates the preparation for testing.
* **API Verification:** Verifying that a fluent API (method chaining) remains stable even when complex arguments (`*nums`) are passed.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Navigate to the directory containing this script.
3. Run the following command in your terminal:

```bash
python test_math_dojo.py