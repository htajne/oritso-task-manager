# Oritso Task Manager - MVC Assignment

**Full-stack Task Management application implementing CRUD + Search operations using Flask MVC pattern.** [file:1]

## 🎯 **Assignment Objectives Met**

- ✅ **Create** - Add new tasks via modal form
- ✅ **Read** - List all tasks with pagination
- ✅ **Update** - Edit tasks via dedicated page
- ✅ **Delete** - Remove tasks with confirmation
- ✅ **Search** - Filter by title/status

## 📋 **Database Design (DB-First Approach)**

erDiagram

    TASK {
        
        int id PK "AUTO_INCREMENT"
        
        varchar title "NOT NULL, INDEX"
        
        text description
        
        date due_date
        
        varchar status "DEFAULT 'Pending', INDEX" 
        
        text remarks
        
        timestamp created_on "DEFAULT CURRENT_TIMESTAMP, INDEX"
        
        timestamp updated_on "DEFAULT CURRENT_TIMESTAMP"
        
        varchar created_by "DEFAULT 'Himanshu Tajne'"
        
        varchar updated_by "DEFAULT 'Himanshu Tajne'"
    }
    
    %% Performance Indexes
    TASK ||--|| TASK : "title INDEX (search)"
    TASK ||--|| TASK : "status INDEX (filter)" 
    TASK ||--|| TASK : "created_on INDEX (sort)"
    
    %% Key Constraints
    TASK ||--o{ TASK : "PK: id"
    TASK ||--o{ TASK : "Audit Trail"


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
├── templates/      # View (HTML)
├── init_db.py      # DB Setup
├── requirements.txt
└── README.md
```
**VISUAL REPRESENTATIONS**
<img width="961" height="794" alt="Screenshot 2026-03-12 223237" src="https://github.com/user-attachments/assets/7251a391-6d6f-4f94-bdc7-60d84985303b" />

<img width="962" height="749" alt="Screenshot 2026-03-12 223258" src="https://github.com/user-attachments/assets/e029f0d1-4c48-49d9-be60-255711335bed" />

<img width="1003" height="870" alt="Screenshot 2026-03-12 223352" src="https://github.com/user-attachments/assets/9e810786-161d-4a4a-8e77-3f2aed8fb93f" />




