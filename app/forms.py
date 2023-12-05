from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, DateField, PasswordField, BooleanField, \
    SelectMultipleField, SelectField, RadioField
from wtforms.validators import DataRequired, ValidationError, NumberRange, EqualTo
from app.models import User, Player, PlayerClass, PlayerRace

class CreateCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    strength = StringField('Strength', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    dexterity = StringField('Dexterity', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    constitution = StringField('Constitution', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    intelligence = StringField('Intelligence', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    wisdom = StringField('Wisdom', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    charisma = StringField('Charisma', validators=[DataRequired(), NumberRange(3, 20, "Stat must be in the range 3 - 20")])
    level = StringField('Level', validators=[DataRequired(), NumberRange(1, 20, "Level must be in the range 1 - 20")])
    xp = StringField('XP')
    player_class = SelectField('Class', validators=[DataRequired()], coerce=int)
    player_race = SelectField('Race', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Update Character')

    def validate_stats(self, level, strength, dexterity, constitution, intelligence, wisdom, charisma):
        max_skill_points = 16 + int(level)
        if int(strength) + int(dexterity) + int(constitution) + int(intelligence) + int(wisdom) + int(charisma) > max_skill_points:
            raise ValidationError("Number of skill points expended exceeds " + str(max_skill_points))
