from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    name = StringField(label='Book Name', validators=[DataRequired()])
    author = StringField(label='Book Author', validators=[DataRequired()])
    rating = StringField(label='Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditForm(FlaskForm):
    rating = StringField(label='Rating', validators=[DataRequired()])
    submit = SubmitField('submit')