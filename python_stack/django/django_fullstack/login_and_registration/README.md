<div align="center">

# 🔐 Django Full-Stack: Secure Identity & Authentication System (Bcrypt & COPPA Compliance)
**Custom Model Managers, Safe Password Hashing, Multi-Tier Server Validations & AJAX Email Availability Handshakes**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Bcrypt__Cryptography-red?style=for-the-badge)
![Compliance](https://img.shields.io/badge/Compliance-COPPA__13+-darkblue?style=for-the-badge)

</div>

---

## 📝 Description
This project implements a secure, industry-standard **Login and Registration System** built on top of Django's MTV framework. Emphasizing tight application-tier security and structural decoupling, this architecture moves the entire user verification, email uniqueness constraints, and dynamic age calculations into a custom `UserManager`. Rather than leaking sensitive hashing logic into views, the backend processes incoming credentials through one-way salty encryption using **Bcrypt**, establishes protected multi-route session access rules, and provides live feedback channels.

---

## 🎯 Core Engineering Lessons & Objectives
* **Model-Tier Cryptography Integration:** Encapsulating one-way string transformations (`bcrypt.hashpw`) directly inside the model manager lifecycle to prevent plain-text credentials from shifting exposed across peripheral system logs.
* **Stateless Route Access Isolation:** Wrapping standard validation decorators around private internal hubs (like `/success`) to instantly kick out unauthenticated or spoofed request calls back to login portals.
* **Regulatory Compliance Calculations:** Overriding plain year-difference checks by monitoring relative month/day tuple boundaries to accurately determine real-world chronological age, satisfying **COPPA regulations**.

---

## 🛠️ Implemented Features & Architecture Breakdown

### 1. Robust Core Registration & Login Verification
* **Name Fields:** Enforces minimum length limits (2+ characters) and restricts string types strictly to alphabetical character sets via Python's `.isalpha()`.
* **Email Constraints:** Validates syntax accuracy using comprehensive Regular Expressions (`EMAIL_REGEX`) and blocks lookup duplicates against active DB records.
* **Password Confirm Matching:** Audits structural complexity and checks token parity before calling encryption hooks.

### 2. ⚡ NINJA BONUS (Temporal Checkers & Email Unique Constraints)
* Mitigates invalid database logging by verifying that the user-provided date of birth strictly resides in past calendar timelines (`birth_date < today`).
* Uses case-insensitive search techniques to intercept existing emails early, ensuring safe user onboarding pipelines.

### 3. 🔥 SENSEI BONUS (COPPA Age Verification & AJAX Live Availability Engine)
* **COPPA Compliance:** Rejects registrations for individuals under **13 years old** directly at the server level, appending specific errors to the validation dictionary.
* **AJAX Integration:** Includes an asynchronous web route (`/check-email`) that communicates with live client-side validation logic. This evaluates email availability on the fly as the user types, before form submittal.

---

## 🗂️ RESTful Authentication Routing Diagram

| Web Path Endpoint | HTTP Method | Target Controller Action | Operational System Behavior |
| :--- | :--- | :--- | :--- |
| `/` | GET | `views.index` | Renders the primary dashboard containing clean split forms for Login & Registration. |
| `/register` | **POST Only** | `views.register` | Validates records, passes text to model managers, encrypts inputs, and establishes sessions. |
| `/login` | **POST Only** | `views.login` | Evaluates email exists, matches token against Bcrypt hashes, and grants dashboard authorization. |
| `/success` | **GET Protected**| `views.success` | **Protected Hub:** Displays a welcome workspace for authenticated active sessions only. |
| `/logout` | GET / POST | `views.logout` | Clears and flushes the server session storage block, redirecting traffic back home. |
| `/check-email` | **AJAX GET** | `views.check_email` | Processes background requests to return JSON availability states for live UI validation. |

---

## 🛡️ Security Testing Protocols

### The Sandbox Route Bypass Attack
1. Clear your local browser cookies or open up an incognito environment.
2. Directly type the absolute route path into your browser address bar: `http://localhost:8000/success`.
3. Notice how your security view architecture intercepts the request context, confirms an empty user ID session block, and throws a safe redirect back to `/`.

### The COPPA Compliance Boundary Verification
1. Attempt to register a user with a birth date that makes them exactly 12 years and 11 months old based on today's server date.
2. Notice how the system captures the specific tuple offset and prevents database insertion, requesting compliance approval.

---

## 🚀 Quickstart Installation
1. Apply structural tables and compile user authentication rows:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Launch the server instance:
   ```bash
   python manage.py runserver
   ```
3. Connect your browser to `http://localhost:8000/` to test input rules and watch live AJAX fields process validation errors seamlessly.