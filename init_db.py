import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from app import app, db
from models import Task

load_dotenv()

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()
    
    # Add sample data - due date is 2 days from now
    due_date = datetime.now().date() + timedelta(days=2)
    
    sample_tasks = [
        Task(title="Complete Oritso Assignment", 
             description="Build task manager with full CRUD operations",
             due_date=due_date,
             status="In Progress", 
             remarks="Due in 2 days - Himanshu Tajne",
             created_by="Himanshu Tajne"),
        Task(title="Deploy to GitHub", 
             status="Completed",
             created_by="Himanshu Tajne")
    ]
    
    for task in sample_tasks:
        db.session.add(task)
    
    db.session.commit()
    print("✅ Database initialized with 2 sample tasks!")
    print("📊 User: Himanshu Tajne")
    print("📅 First task due date: 2 days from now")
    print("🚀 Run 'python app.py' to start the application")
