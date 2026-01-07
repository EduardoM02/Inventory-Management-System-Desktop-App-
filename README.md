# Inventory Management System Desktop App
<img src="https://img.shields.io/badge/STATUS-In_Development-g"> <img src="https://img.shields.io/badge/Release_date-December-blue">

Desktop application for managing product inventory, categories, and stock movements. Built with Python, PySide6, SQLAlchemy, and PostgreSQL, following a modular and layered architecture.

---

## :star: Features
- Category management (CRUD)
- Product management with category assignment
- Stock movements (in / out) with history
- Real-time search and filtering
- Data validation and error handling
- Relational database with integrity constraints
- Desktop GUI built with PySide6 (Qt)

---

## :hammer: Architecture
The project follows a clean layered architecture to ensure maintainability and scalability

Responsibilities by layer:
- **Repositories**: database queries and persistence
- **Services**: business rules and validations
- **Controllers**: UI logic and user interactions
- **UI**: PySide6 views and dialogs

---

## ✔️: Tech Stack
- Python 3.10+
- PySide6 (Qt for Python)
- SQLAlchemy (ORM)
- PostgreSQL
- psycopg2
- MVC / Service-Repository pattern

---

## 📁 Setup & Installation
1. Clone repository:<pre>
      git clone https://github.com/EduardoM02/Inventory-Management-System-Desktop-App-.git
      cd Inventory-Management-System-Desktop-App-
2. Create virtual environment:<pre>
      python -m venv .venv
      source .venv/bin/activate   # Linux/Mac
      .venv\Scripts\activate      # Windows
3. Install dependencies:<pre>
      pip install -r requirements.txt
4. Configure environment variables (using .env-example)

---

## 💾 Database Setup
1. Create a PostgreSQL database
2. Run the schema script:
   psql -d inventory_db -f database/schema.sql
3. Configure `.env` variables

---

## ▶️ Run the application
python main.py

---

## 📘 What I Learned
- Designing a desktop application with clean architecture
- Managing complex CRUD operations with relational data
- Handling database integrity and business rules
- Structuring scalable Python projects
- Integrating PySide6 with SQLAlchemy

---

## Future Improvements
- UI styling with QSS (themes / dark mode)
- Sidebar navigation
- Sorting and pagination
- User authentication
- Export reports (PDF / Excel)

---

## Author
Eduardo Montaño Gonzalez
Python Developer

Contact: eduardomg0212@gmail.com
GitHub: https://github.com/EduardoM02
