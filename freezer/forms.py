from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField,
    FloatField, SelectField
)
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class AddMeal(FlaskForm):
    buy_date = DateField('buy date', validators=[DataRequired()] )
    expiration_date = DateField('buy date', validators=[DataRequired()] )
    freezing_date = DateField('buy date', validators=[DataRequired()] )
    description =  StringField('description', validators=[DataRequired()])
    units = IntegerField('units', validators=[DataRequired()])
    weight = FloatField('weight', validators=[DataRequired()])
    unity = SelectField('unity', coerce=str, validators=[DataRequired()])
    category = SelectField('category', coerce=int, validators=[DataRequired()])
    subcategory = SelectField('subcategory', coerce=int, validators=[DataRequired()])
    drawer = IntegerField('drawer')
    submit = SubmitField('Add Meal')


class DeleteMeal(FlaskForm):
    meal_id = IntegerField('Meal id', validators=[DataRequired()] )
    submit = SubmitField('Delete Meal')