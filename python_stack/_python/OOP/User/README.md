<div align="center">

# 👤 Python OOP: User Account Management
**Implementing Method Chaining and Object Interaction**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Focus-Object_Oriented_Programming-blue?style=for-the-badge)

</div>

---

## 📝 Description
This assignment focuses on creating a `User` class capable of managing its own account balance through deposit, withdrawal, and transfer operations. The project highlights the use of **Method Chaining**, allowing for a fluent and expressive way to execute multiple transactions in a single line of code.



---

## 🎯 Core Features
* **Transaction Management:** Methods to handle deposits and withdrawals with basic validation logic.
* **Method Chaining:** Every operational method returns `self`, enabling the fluent syntax (e.g., `user.deposit().deposit().withdraw()`).
* **Inter-user Transfers:** A dedicated method to move funds safely between two different `User` instances.
* **Account Reporting:** A clear mechanism to display current user information and balance.

---

## 🛠️ Key Concepts
* **Classes & Objects:** Defining the `User` blueprint and instantiating multiple independent users.
* **The `self` Keyword:** Essential for accessing instance-specific data like `account_balance` and `name`.
* **Method Chaining:** Returning the object instance to allow immediate subsequent method calls on the same object.
* **Defensive Programming:** Including conditional checks (e.g., `if amount <= self.account_balance`) to prevent negative balances during withdrawals and transfers.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Navigate to the directory containing this script.
3. Run the following command in your terminal:

```bash
python user_account.py