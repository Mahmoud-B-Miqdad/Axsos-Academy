<div align="center">

# 🛒 Django Full-Stack: Amadon Secure E-Commerce (PRG Pattern & Price Integrity)
**Post-Redirect-Get (PRG) Architecture, Client-Side Tamper Proofing, Session State Persistence & Transactional Aggregate DB Queries**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Focus-Backend__Data__Integrity-red?style=for-the-badge)
![Database](https://img.shields.io/badge/Pattern-Post__Redirect__Get-darkblue?style=for-the-badge)

</div>

---

## 📝 Description
This project implements a highly secure, transactional full-stack e-commerce engine named **Amadon**. Engineered specifically to combat common security flaws in commercial web workflows, this architecture focuses heavily on server-side pricing verification and strict double-submit middleware protection. By migrating calculation matrices out of form structures and leveraging Django's session layers alongside a custom `OrderManager`, the platform insulates financial attributes against manual frontend developer console injections and accidental transaction reprocessing.

---

## 🎯 Core Engineering Lessons & Objectives
* **Post-Redirect-Get (PRG) Workflow:** Eliminating the critical industry mistake of rendering HTML templates directly inside standard `POST` request channels. If a buyer reloads their post-purchase dashboard, the client browser fires a safe `GET` pathway, preventing accidental double billing on credit cards.
* **Tamper-Proof Data Ingestion:** Eradicating severe architectural flaws where price figures are embedded into hidden input elements (`<input type="hidden" name="price">`). The system passes only a fixed, read-only entity ID (`product_id`) and isolates price lookup securely on the server side via the transactional model engine.
* **Asymmetric Session Hydration:** Caching live calculated metrics into stateless client cookies/sessions temporarily to transmit data snapshots safely across isolated request wrappers without leaving active parameters hanging in accessible URL query parameters.

---

## 🛠️ Implemented Features & Core Architecture
* **Server-Controlled Verification Core:** Uses an isolated model manager pipeline (`process_purchase`) to match product ids against trusted persistent rows, automatically discarding price changes manipulated on client machines.
* **Comprehensive Historical Analytics:** Utilizes optimized database-tier aggregations (`models.Sum`) to track, calculate, and compile combined lifetime purchase parameters (`total_items` and `total_spent`) on the fly.
* **Encapsulated Checkout Cockpit:** A isolated confirmation dashboard route (`/checkout/`) that fetches and formats temporary session contextual summaries cleanly before automatically destroying mutable staging logs.

---

## 🗂️ RESTful API Routing & Protection Blueprint

| Web Path Endpoint | HTTP Method | Target Controller Action | Operational System Behavior |
| :--- | :--- | :--- | :--- |
| `/` | GET | `views.index` | Renders the primary store showcase layout listing available catalog inventories. |
| `/buy/` | **POST Only** | `views.buy_product` | Intercepts identifiers, pulls immutable prices from DB, registers logs, and initiates PRG session cache. |
| `/checkout/` | **GET Only** | `views.checkout` | Safely extracts and displays temporary single-session receipts and historical summary dashboards. |

---

## 🛡️ Security Proof of Concept (Testing the Flaws)
1. **The Double-Submit Test:** Place a purchase order, land on the `/checkout/` route, and press **F5 / Refresh**. Notice that the metrics remain unchanged because your backend redirects the browser request into a clean, un-cacheable `GET` track.
2. **The Inspect Element Price Attack:** Open up your browser's element inspector tool, alter a product form price parameter to `$0.01` or any arbitrary layout configuration, and hit buy. Notice how the system charges your receipt the exact amount listed inside your persistent `Product` row, completely neutralizing the injection payload.

---

## 🚀 How to Explore
1. Initialize structural migrations to construct store items and order history log tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Open your interactive shell environment to seed mock merchandise parameters into your backend DB:
   ```bash
   python manage.py shell
   ```
3. Run the secure runtime server environment:
    ```python
    from your_app.models import Product
Product.objects.create(description="Dojo T-Shirt", price=19.99)
Product.objects.create(description="Dojo Sweater", price=29.99)
Product.objects.create(description="Dojo Cup", price=4.99)
Product.objects.create(description="Algorithm Book", price=49.99)
    ```
4. Access `http://localhost:8000/` and run purchase checks to witness clean session-state routing handling data seamlessly.