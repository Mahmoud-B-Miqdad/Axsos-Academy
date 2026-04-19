<div align="center">

# 🏦 Python OOP: User and Bank Account
**Mastering Object-Oriented Programming and Composition**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Focus-OOP_&_Composition-blue?style=for-the-badge)

</div>

---

## 📝 Description
This project demonstrates OOP principles in Python. It models a banking system where a `User` class manages a `BankAccount` object. I implemented robust features like deposit, withdrawal with overdraft fees, interest yielding, and inter-user transfers, all utilizing **Method Chaining** for cleaner, more fluent code.



---

## 🎯 Core Features
* **Composition:** The `User` class "has a" `BankAccount`, demonstrating how classes can interact to build complex systems.
* **Method Chaining:** Every method returns `self`, allowing for fluent calls like `acc.deposit().withdraw().display()`.
* **Business Logic:** Implemented specific banking rules such as charging a $5 fee for insufficient funds and yielding interest on positive balances.
* **Inter-object Communication:** The `transfer_money` method facilitates transactions between two different `User` instances.

---

## 🛠️ Key Concepts
* **Classes & Objects:** Defining blueprints for Users and Bank Accounts.
* **Encapsulation:** Keeping data (balance, interest rate) and behavior (deposit, withdraw) bundled within their respective classes.
* **The `self` Keyword:** Correctly accessing instance attributes and methods.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Ensure you have the `BankAccount.py` and `User.py` files in the same directory.
3. Run the main script (e.g., `main.py`) in your terminal:

```bash
python main.py