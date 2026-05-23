<div align="center">

# 🚀 Django ORM: Users Model & Shell Manipulation
**Database Design, Migrations, Object-Relational Mapping & Interactive Shell Queries**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Database](https://img.shields.io/badge/Focus-ORM_%26_Queries-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project focuses on database abstraction layer principles using the Django Object-Relational Mapper (ORM). The primary objective was to translate a structured Entity Relationship Diagram (ERD) into a functional Python class model (`single_model_orm`). After creating database schemas via structural migration scripts, the Django Interactive Shell console was leveraged to execute a sequence of transactional CRUD tasks—covering instance instantiation, collection filtering, non-destructive row mutations, primary key deletions, and sequential data ordering.

---

## 🎯 Key Concepts
* **ERD-to-Model Mapping:** Translating standard database attributes (`VARCHAR`, `INT`, `DATETIME`) into Django model fields (`CharField`, `IntegerField`, `DateTimeField`).
* **Automated Auditing Fields:** Implementing tracking parameters using `auto_now_add=True` (to lock record generation dates) and `auto_now=True` (to track continuous timestamp modifications).
* **Interactive Data Querying:** Utilizing the active backend workspace terminal (`python manage.py shell`) to programmatically interface with connected storage drivers without manual SQL syntax scripts.
* **Persistent Record Management:** Running standard instance queries such as `.create()`, `.get()`, `.save()`, and `.delete()` to execute persistent mutations directly on live database records.

---

## 🛠️ Implementation & Bonus Highlights
* **Bonus & Advanced Core Queries Handled:**
    * **Dynamic Selection Filters:** Targeted precise record rows via uniquely isolated criteria structures (`User.objects.get(id=3)`).
    * **Transactional Alterations:** Updated targeted text arrays and securely committed states directly to storage tables via automated execution routines (`.save()`).
    * **Ordered Sequence Lists:** Sorted model data queries in ascending sequence by invoking the `.order_by('field')` operation.
    * **Descending Order Bonus:** Completed advanced data formatting challenges by adding inverted dash notation blocks (`.order_by('-field')`) to reverse query collection outputs.

---

## 🗂️ CRUD Query Script Reference
Below is the sequential log of the operations executed inside the interactive console workspace:

```python
# 0. Import active applications model schemas
from users_app.models import *

# 1. Create 3 new user records
User.objects.create(first_name="Ahmad", last_name="Ali", email_address="ahmad@email.com", age=25)
User.objects.create(first_name="Sami", last_name="Mansour", email_address="sami@email.com", age=30)
User.objects.create(first_name="Mahmoud", last_name="Miqdad", email_address="mahmoud@email.com", age=22)

# 2. Retrieve all active users
User.objects.all()

# 3. Retrieve the last user instance
User.objects.last()

# 4. Retrieve the first user instance
User.objects.first()

# 5. Change specific user attributes (id=3 last name modification)
user3 = User.objects.get(id=3)
user3.last_name = "Pancakes"
user3.save()

# 6. Delete a target row entry from the system (id=2)
User.objects.get(id=2).delete()

# 7. Get all user records sorted by first name in ascending order
User.objects.order_by('first_name')

# 8. BONUS: Get all user records sorted by first name in descending order
User.objects.order_by('-first_name')
```

---

## 🚀 How to Explore
1. Build local migration blueprints tracking your code schemas: `python manage.py makemigrations`.
2. Push generated blueprint architecture onto your active database: `python manage.py migrate`.
3. Boot up the Python interactive console workspace: `python manage.py shell`.
4. Copy and execute any query block from the reference table above to observe the real-time Django QuerySet feedback structures directly on your terminal screen.