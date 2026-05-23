<div align="center">

# 🚀 Django ORM: Relational Database Models (One-to-Many)
**Data Schema Relational Integrity, Foreign Key Constraints, Reverse Lookups & Schema Evolution**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Database](https://img.shields.io/badge/Focus-One_To_Many_ORM-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project focuses on executing relational database configuration concepts inside Django's Object-Relational Mapper (ORM) engine. The core requirement involved implementing a structural One-to-Many relationship mapping parent `Dojo` entry blocks to multiple dependent child `Ninja` sub-rows. By utilizing database-level cascading rules (`models.CASCADE`) and defining explicit abstraction shortcuts (`related_name`), this project showcases complex dependency management, table flushing, relational cross-queries, and backward database schema evolution utilizing continuous fields migration logic.

---

## 🎯 Key Concepts
* **One-to-Many Relationship Constraints:** Establishing rigid table linkages via `models.ForeignKey` to link distinct records hierarchically across storage structures.
* **Cascading Delete Lifecycles:** Attaching `on_delete=models.CASCADE` parameters to ensure that purging a parent entity immediately drops all dependent child entries without throwing structural data orphans.
* **Reverse Relational Lookups:** Leveraging custom `related_name="ninjas"` properties on the database foreign key pointer, enabling parent elements to seamlessly evaluate downstream related collection records via structural attributes (`dojo.ninjas.all()`).
* **Schema Evolution & Migrations:** Inserting a field modification (`desc = models.TextField(default="old dojo")`) onto a live data framework and using dynamic fallback configurations to preserve overall data integrity.

---

## 🛠️ Implementation & Query Highlights
* **Relational Core Queries Handled:**
    * **Table Clearances:** Verified clean cascading executions by invoking global clear methods (`Dojo.objects.all().delete()`).
    * **Targeted Related Collections:** Fetched complete nested child collections bound directly to precise parent instances (`dojo1.ninjas.all()`).
    * **Reverse Instance Traversals:** Inspected dynamic field parent configurations backwards from a single terminal target reference row (`last_ninja.dojo`).
    * **Dynamic Description Overrides:** Validated custom field instantiation changes alongside text field insertions seamlessly.

---

## 🗂️ Relational CRUD Query Script Reference
Below is the continuous sequential script log executed within the interactive workspace terminal console:

```python
# 0. Import active applications model schemas
from dojo_ninjas_app.models import *

# 1. Create 3 initial template Dojo records
dojo1 = Dojo.objects.create(name="Coding Dojo", city="Burbank", state="CA")
dojo2 = Dojo.objects.create(name="Silicon Valley Dojo", city="San Jose", state="CA")
dojo3 = Dojo.objects.create(name="Online Dojo", city="Remote", state="WA")

# 2. Delete the 3 dojos just created to verify cascading delete loops
Dojo.objects.all().delete()

# 3. Create 3 new persistent Dojo records
dojo1 = Dojo.objects.create(name="Dojo A", city="Ramallah", state="PS")
dojo2 = Dojo.objects.create(name="Dojo B", city="Amman", state="JO")
dojo3 = Dojo.objects.create(name="Dojo C", city="Cairo", state="EG")

# 4. Create 3 ninjas that belong to the first dojo instance
Ninja.objects.create(first_name="Mahmoud", last_name="Ali", dojo=dojo1)
Ninja.objects.create(first_name="Ahmad", last_name="Sami", dojo=dojo1)
Ninja.objects.create(first_name="Saeed", last_name="Hassan", dojo=dojo1)

# 5. Create 3 ninjas that belong to the second dojo instance
Ninja.objects.create(first_name="Rami", last_name="Kamal", dojo=dojo2)
Ninja.objects.create(first_name="Omar", last_name="Fadi", dojo=dojo2)
Ninja.objects.create(first_name="Youssef", last_name="Nader", dojo=dojo2)

# 6. Create 3 ninjas that belong to the third dojo instance
Ninja.objects.create(first_name="Khaled", last_name="Ziad", dojo=dojo3)
Ninja.objects.create(first_name="Zain", last_name="Tareq", dojo=dojo3)
Ninja.objects.create(first_name="Anas", last_name="Majd", dojo=dojo3)

# 7. Retrieve all ninjas belonging to the first dojo via reverse relationship attribute
dojo1.ninjas.all()

# 8. Retrieve all ninjas belonging to the very last dojo instance recorded
last_dojo = Dojo.objects.last()
last_dojo.ninjas.all()

# 9. Retrieve the master dojo instance object linked directly to the last ninja record
last_ninja = Ninja.objects.last()
last_ninja.dojo 

# 10. Create a new dojo specifying a unique text property after field modification migrations
new_dojo = Dojo.objects.create(name="Advanced Dojo", city="Gaza", state="PS", desc="This is a new custom description")
```

---

## 🚀 How to Explore
1. Track core blueprint updates adjusting current schemas: `python manage.py makemigrations`.
2. Push relational parameters structural fields onto the active storage setup: `python manage.py migrate`.
3. Enter the unified Django framework interactive shell interface: `python manage.py shell`.
4. Process any target code commands from the reference script block to observe the reverse query responses instantly.
