<div align="center">

# 🥷 Django Full-Stack: Dojos & Ninjas Portal (One-to-Many UI Integration)
**Relational Data Mapping, Dynamic Foreign Key Dropdowns, Reverse Lookup Iteration & Cascading Deletions**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Database](https://img.shields.io/badge/Focus-One__To__Many__UI-darkgreen?style=for-the-badge)

</div>

---

## 📝 Description
This project delivers a complete dynamic interface wrapper built over a robust One-to-Many database schema inside Django's MTV architecture. Building upon backend ORM models, this platform exposes responsive forms to simultaneously add new parent records (`Dojos`) and dependent child items (`Ninjas`) linked instantly via relational select dropdowns. The front-end view leverages reverse lookup capabilities to group nested rosters cleanly under their parent headings, while supporting advanced administrative features like cascading entity drops and accurate computational row metrics.

---

## 🎯 Key Concepts & Objectives
* **Relational Form Mapping:** Incorporating active multi-input forms to feed structural data models dynamically from standard HTML environments.
* **Foreign Key Dropdown Binding:** Extracting query arrays from primary master schemas (`Dojo.objects.all()`) to populate dynamic form option elements `<select>` targeting precise database record linkages.
* **Reverse Roster Lookups:** Employing attribute abstraction bindings (`dojo.ninjas.all`) right within Django template markup tags to loop through child objects associated with single parental nodes.
* **Post-Redirect-Get (PRG) Workflow:** Routing successful data ingestions using secure backend redirections (`return redirect('/')`) to keep active data stores safe from accidental duplicate submissions caused by client page refreshes.

---

## 🛠️ Implemented Features & Bonuses
* **Dynamic Dojo & Ninja Forms:** Two distinct structural entry cards allowing smooth data insertion into both sides of the relational database.
* **⚡ NINJA BONUS (Cascading Deletions):** Integrated a quick-action tracking mechanism via targeted POST route components (`/delete_dojo/<int:dojo_id>`) to trigger a clean cascading wipeout on parent models and instantly drop all associated dependent records from the persistence storage.
* **🔥 SENSEI BONUS (Computational Roster Metrics):** Attached real-time quantitative count indicators (`{{ dojo.ninjas.count }}`) directly next to parent entries to dynamically display the number of active ninjas registered within each Dojo.

---

## 🗂️ API Architecture Reference

| Web Path Endpoint | Allowed Request Method | Triggered Core Controller | Operational System Behavior |
| :--- | :--- | :--- | :--- |
| `/` | GET | `views.index` | Renders the main cockpit page displaying all dojos, counts, rosters, and forms. |
| `/add_dojo` | POST | `views.create_dojo` | Ingests structural data fields to commit a new parent Dojo record. |
| `/add_ninja` | POST | `views.create_ninja` | Links child parameters to selected target parent entities via ForeignKey. |
| `/delete_dojo/<id>` | POST | `views.delete_dojo` | Executes an instant administrative cascading drop on targeted entities. |

## 🚀 How to Explore
1. Initialize local server engines within terminal workspaces: `python manage.py runserver`.
2. Connect client browsers targeting standard local endpoints: `http://localhost:8000/`.
3. Fill out the Add a Dojo component to create brand new training stations.
4. Head over to the Add a Ninja form to insert new fighters directly into your newly created dojos via the dynamic dropdown list.
5. Test the NINJA BONUS feature by clicking the `Delete Dojo` action buttons to watch parent and child blocks clean themselves up instantly
