from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length


class TaskCreateForm(FlaskForm):
    id = HiddenField('ID')
    name = StringField('Название', validators=[DataRequired(), Length(min=1, max=64)])
    start_pos = HiddenField('Начальная позиция',
                            validators=[DataRequired(), Length(min=1, max=128)], default='start')
    end_pos = HiddenField('Конечная позиция', validators=[DataRequired(), Length(min=1, max=128)], default='end')
    submit = SubmitField('Добавить')


class TournamentCreateForm(FlaskForm):
    id = HiddenField('ID')
    name = StringField('Название турнира', validators=[DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Добавить')
