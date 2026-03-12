from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=200)])
    description = TextAreaField('Description', validators=[Length(max=1000)])
    due_date = DateField('Due Date')
    status = SelectField('Status', choices=[
        ('Pending', 'Pending'), 
        ('In Progress', 'In Progress'), 
        ('Completed', 'Completed')
    ], default='Pending')
    remarks = TextAreaField('Remarks', validators=[Length(max=500)])
