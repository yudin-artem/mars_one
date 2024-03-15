from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = IntegerField('Командир', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    worksize = IntegerField('Время выполнения', validators=[DataRequired()])
    collaborators = TextAreaField("Рабочие", validators=[DataRequired()])
    is_finished = BooleanField("Завершено")
    submit = SubmitField('Применить')
