from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, DateField, PasswordField, BooleanField, \
    SelectMultipleField, SelectField, RadioField
from wtforms.validators import DataRequired, ValidationError, NumberRange, EqualTo
from app.models import User, Player, PlayerClass, PlayerRace

class CreateCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    str = StringField('Strength', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    dex = StringField('Dexterity', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    con = StringField('Constitution', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    int = StringField('Intelligence', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    wis = StringField('Wisdom', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    cha = StringField('Charisma', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    level = StringField('Level', validators=[DataRequired(), NumberRange(1, 20, "Level must be in the range 1 - 20")])
    xp = StringField('XP')
    player_class = SelectField('Class', validators=[DataRequired()], coerce=int)
    player_race = SelectField('Race', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Update Character')