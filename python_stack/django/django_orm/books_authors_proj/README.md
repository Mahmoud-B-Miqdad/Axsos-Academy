<div align="center">

# 🚀 Django ORM: Relational Database Models (Many-to-Many)
**Data Schema Relational Integrity, Junction Table Constraints, Reverse Lookups & Schema Evolution**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Database](https://img.shields.io/badge/Focus-Many__To__Many__ORM-darkblue?style=for-the-badge)

</div>

---

## 📝 Description
This project focuses on executing advanced relational database configuration concepts inside Django's Object-Relational Mapper (ORM) engine. The core requirement involved implementing a structural Many-to-Many relationship mapping parent `Book` entry blocks to multiple dependent `Author` rows, and vice-versa. By utilizing automatic junction table generation and defining explicit abstraction shortcuts (`related_name`), this project showcases complex multi-entity management, dynamic relationship bridging, relational cross-queries, and backward database schema evolution utilizing continuous fields migration logic.

---

## 🎯 Key Concepts
* **Many-to-Many Relationship Constraints:** Establishing flexible bidirectional table linkages via `models.ManyToManyField` to map multiple records horizontally across storage structures through an implicit bridge table.
* **Junction Table Lifecycles:** Utilizing native Django abstractions to seamlessly manage row mapping records without throwing structural data orphans during relational assignments.
* **Reverse Relational Lookups:** Leveraging custom `related_name="authors"` properties on the database relationship pointer, enabling target elements to seamlessly evaluate upstream related collection records via structural attributes (`book.authors.all()`).
* **Schema Evolution & Migrations:** Inserting a field modification (`notes = models.TextField(null=True, blank=True)`) onto a live data framework and using dynamic fallback configurations to preserve overall data integrity.

---

## 🛠️ Implementation & Query Highlights
* **Relational Core Queries Handled:**
    * **Sequential Record Ingestion:** Verified clean programmatic creation of multiple independent objects for both data structures.
    * **Targeted Forward Collections:** Fetched complete nested child collections bound directly to precise instances (`author.books.all()`).
    * **Reverse Instance Traversals:** Inspected dynamic field parent configurations backwards from a single terminal target reference row (`book.authors.all()`).
    * **Dynamic Relationship Alterations:** Validated direct collection manipulation strategies including sequential element pushes (`.add()`) and precise contextual relation drops (`.remove()`).

---

## 🗂️ Relational CRUD Query Script Reference
Below is the continuous sequential script log executed within the interactive workspace terminal console:

```python
# 0. Import active applications model schemas
from books_authors_app.models import Book, Author

# 1. Create 5 initial template Book records
b1 = Book.objects.create(title="C Sharp", desc="C# Programming Language")
b2 = Book.objects.create(title="Java", desc="Java Programming Language")
b3 = Book.objects.create(title="Python", desc="Python Programming Language")
b4 = Book.objects.create(title="PHP", desc="PHP Programming Language")
b5 = Book.objects.create(title="Ruby", desc="Ruby Programming Language")

# 2. Create 5 different Author records
a1 = Author.objects.create(first_name="Jane", last_name="Austen")
a2 = Author.objects.create(first_name="Emily", last_name="Dickinson")
a3 = Author.objects.create(first_name="Fyodor", last_name="Dostoevsky")
a4 = Author.objects.create(first_name="William", last_name="Shakespeare")
a5 = Author.objects.create(first_name="Lao", last_name="Tzu")

# 3. Update a specific book title smoothly
book_csharp = Book.objects.get(title="C Sharp")
book_csharp.title = "C#"
book_csharp.save()

# 4. Change an author's attribute configuration mid-lifecycle
author_4 = Author.objects.get(id=4)
author_4.first_name = "Bill"
author_4.save()

# 5. Assign the first author to the first 2 books
author_1 = Author.objects.get(id=1)
book_1 = Book.objects.get(id=1)
book_2 = Book.objects.get(id=2)
author_1.books.add(book_1, book_2)

# 6. Assign the second author to the first 3 books
author_2 = Author.objects.get(id=2)
book_3 = Book.objects.get(id=3)
author_2.books.add(Book.objects.get(id=1), Book.objects.get(id=2), book_3)

# 7. Assign the third author to the first 4 books
author_3 = Author.objects.get(id=3)
book_4 = Book.objects.get(id=4)
author_3.books.add(Book.objects.get(id=1), Book.objects.get(id=2), Book.objects.get(id=3), book_4)

# 8. Assign the fourth author to all recorded books via programmatic loop
author_4 = Author.objects.get(id=4)
all_books = Book.objects.all()
for book in all_books:
    author_4.books.add(book)

# 9. Retrieve all authors belonging to the 3rd book via reverse relationship attribute
book_3_authors = Book.objects.get(id=3).authors.all()

# 10. Execute a relational deletion to remove the first author from the 3rd book
book_3 = Book.objects.get(id=3)
author_1 = Author.objects.get(id=1)
book_3.authors.remove(author_1)

# 11. Cross-assign the 5th author as one of the authors of the 2nd book
book_2 = Book.objects.get(id=2)
author_5 = Author.objects.get(id=5)
book_2.authors.add(author_5)

# 12. Find and display all books that the 3rd author is part of
author_3_books = Author.objects.get(id=3).books.all()

# 13. Find and display all authors that contributed to the 5th book
book_5_authors = Book.objects.get(id=5).authors.all()
```

---

## 🚀 How to Explore
1. Track core blueprint updates adjusting current schemas: `python manage.py makemigrations`.
2. Push relational parameters structural fields onto the active storage setup: `python manage.py migrate`.
3. Enter the unified Django framework interactive shell interface: `python manage.py shell`.
4. Process any target code commands from the reference script block to observe the reverse query responses instantly.
