<div align="center">

# 🏦 Python OOP: Bank Account Class
**Implementing Fluent Interfaces with Method Chaining**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Focus-Method_Chaining-blue?style=for-the-badge)

</div>

---

## 📝 Description
This assignment focuses on designing a robust `BankAccount` class. Beyond basic banking operations, the core objective was to implement **Method Chaining**, a technique where each method returns the instance (`self`), allowing multiple operations to be performed in a single, readable line of code.



---

## 🎯 Key Features
* **Initialization:** Flexible constructor with default values for interest rates and initial balances.
* **Banking Operations:** * `deposit`: Increases account balance.
    * `withdraw`: Decreases balance with logic for insufficient funds (applying a $5 fee).
    * `yield_interest`: Applies interest only if the balance is positive.
* **Method Chaining:** All operational methods return `self` to enable fluent syntax.

---

## 🛠️ Key Concepts
* **Method Chaining:** Understanding that returning `self` allows the caller to immediately call another method on the same instance.
* **Logic Implementation:** Combining conditional statements (`if/else`) with mathematical updates to maintain data integrity.
* **Encapsulation:** Grouping attributes (`int_rate`, `balance`) and methods within a class structure.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Navigate to the directory containing this script.
3. Run the following command in your terminal:

```bash
python bank_account.py