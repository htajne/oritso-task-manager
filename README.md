# Oritso Task Manager - MVC Assignment

**Full-stack Task Management application implementing CRUD + Search operations using Flask MVC pattern.** [file:1]

## 🎯 **Assignment Objectives Met**

- ✅ **Create** - Add new tasks via modal form
- ✅ **Read** - List all tasks with pagination
- ✅ **Update** - Edit tasks via dedicated page
- ✅ **Delete** - Remove tasks with confirmation
- ✅ **Search** - Filter by title/status

## 🛠 **Tech Stack**

## 📋 **Database Design (DB-First Approach)**

**ER Diagram:** Single `tasks` entity [file:1]

┌──────────────────────┐
│ tasks │
├──────────────────────┤
│ id (PK, AUTO) │
│ title (TEXT)_ │
│ description (TEXT) │
│ due_date (DATE) │
│ status (TEXT)_ │
│ remarks (TEXT) │
│ created*on (TS)* │
│ updated*on (TS)* │
│ created*by (TEXT)* │
│ updated*by (TEXT)* │
└──────────────────────┘

- = Indexed fields for performance

**Indexes:** `title`, `status`, `created_on` for search performance

## 🚀 **Quick Start**

```bash
# 1. Clone & Install
git clone <your-repo>
cd oritso-task-manager
pip install -r requirements.txt

# 2. Initialize Database
python init_db.py

# 3. Run Application
python app.py

Visit: http://localhost:5000

PROJECT STRUCTURE (MVC)

├── app.py          # Controller (Routes + Logic)
├── models.py       # Model (Task ORM)
├── forms.py        # Forms (Validation)
├── templates/      # View (HTML/Jinja2)
├── init_db.py      # DB Setup
├── requirements.txt
└── README.md
```
