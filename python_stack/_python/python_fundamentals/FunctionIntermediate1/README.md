<div align="center">

# 🎲 Python Fundamentals: Random Integers
**Building a Custom Random Number Generator**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Random](https://img.shields.io/badge/Focus-Modules_&_Logic-yellow?style=for-the-badge)

</div>

---

## 📝 Description
This assignment demonstrates the use of Python's built-in `random` module. I implemented a custom function, `randInt`, that generates a random integer within a specified range, handling edge cases such as swapped min/max values and negative bounds.

---

## 🎯 Key Features
* **Default Parameters:** The function defaults to a range of 0 to 100.
* **Error Handling:** Validates inputs to ensure the maximum value is not negative and handles cases where the minimum is greater than the maximum.
* **Random Calculation:** Utilizes `random.random()` to generate floating-point numbers and scales them to the desired range, then rounds the result to an integer.

---

## 🛠️ Key Concepts
* **`random` Module:** Accessing built-in library functions to generate pseudo-random numbers.
* **Parameter Defaults:** Setting values for parameters in a function signature, allowing flexibility in how the function is called.
* **Tuple Unpacking:** Using `min, max = max, min` to efficiently swap values when the input range is provided in reverse.
* **Rounding:** Converting float precision results into integers using `round()`.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Navigate to the directory containing this script.
3. Run the following command in your terminal:

```bash
python random_int.py