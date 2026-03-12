import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from dotenv import load_dotenv
from models import db, Task
from forms import TaskForm

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-prod')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    search = request.args.get('search', '').strip()
    
    # Search functionality
    query = Task.query
    if search:
        query = query.filter(
            db.or_(
                Task.title.ilike(f'%{search}%'),
                Task.status.ilike(f'%{search}%')
            )
        )
    
    tasks = query.order_by(Task.created_on.desc()).all()
    
    if form.validate_on_submit():
        try:
            task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            status=form.status.data,
            remarks=form.remarks.data,
            created_by="Himanshu Tajne",
            updated_by="Himanshu Tajne"
            )
            db.session.add(task)
            db.session.commit()
            flash('Task created successfully!', 'success')
            logger.info(f'Task created: {task.title}')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating task: {str(e)}', 'danger')
            logger.error(f'Create error: {e}')

    
    return render_template('index.html', form=form, tasks=tasks, search=search)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)
    
    if form.validate_on_submit():
        try:
            task.title = form.title.data
            task.description = form.description.data
            task.due_date = form.due_date.data
            task.status = form.status.data
            task.remarks = form.remarks.data
            task.updated_by = "Himanshu Tajne"
            db.session.commit()
            flash('Task updated successfully!', 'success')
            logger.info(f'Task updated: {task.id}')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating task: {str(e)}', 'danger')
            logger.error(f'Update error: {e}')
    
    return render_template('edit.html', form=form, task=task)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    try:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!', 'success')
        logger.info(f'Task deleted: {task.id}')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting task: {str(e)}', 'danger')
        logger.error(f'Delete error: {e}')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
