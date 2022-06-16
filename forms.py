from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat','dog','porcupine'])])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message = "Please enter a URL")])
    age = IntegerField("Age", validators=[Optional(),NumberRange(min = 0, max=30, message="your pet is too old.")])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for adding pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL(message = "Please enter a URL")])
    notes = StringField("Notes")
    available = BooleanField("Available")
