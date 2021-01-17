from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, NumberRange, Optional, Length, Email, InputRequired
from wtforms_components import IntegerField, SelectField

from datetime import datetime


class MovieEditForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])

    year = IntegerField(
        "Year",
        validators=[
            Optional(),
            NumberRange(min=1887, max=datetime.now().year),
        ],
    )

class NewUserForm(FlaskForm):
    user_name = StringField("Name", validators=[DataRequired(), Length(max = 50)])
    password = PasswordField("Password", validators=[DataRequired()])
    age = IntegerField("Age", validators=[NumberRange(min=12, max = 99)])
    gender = SelectField("Gender", choices=['Male', 'Female'])
    instrument = SelectField(u'Instrument', choices=['Drums', 'Vocals', 'Electroguitar', 'Bass Guitar', 'Piano'])
    city = SelectField(u'City', choices=['Istanbul', 'Denizli', 'Izmir', 'Ankara', 'Antalya'])
    level = SelectField(u'Level', choices=['Basic', 'Novice', 'Intermediate', 'Advanced', 'Expert'])
    goal = SelectField(u'Goal', validators=[Optional()], choices=['Fun', 'Socializing', 'Concerts - Serious', 'Concerts - Relaxed'])

class NewBandForm(FlaskForm):
    band_name = StringField("Band Name", validators=[DataRequired(), Length(max = 50)])
    city = SelectField(u'City', choices=['Istanbul', 'Denizli', 'Izmir', 'Ankara', 'Antalya'])
    genre = SelectField(u'Genre', choices=['Blues', 'Country', 'Dance', 'Electronic', 'Hip Hop', 'Jazz', 'Latin', 'Pop', 'Rap', 'Rock', 'Other'])
    level = SelectField(u'Level', choices=['Basic', 'Novice', 'Intermediate', 'Advanced', 'Expert'])

class BandRequestForm(FlaskForm):
    goal = SelectField(u'Goal', validators=[Optional()], choices=['Fun', 'Socializing', 'Concerts - Serious', 'Concerts - Relaxed'])
    genre = SelectField(u'Genre', choices=['Blues', 'Country', 'Dance', 'Electronic', 'Hip Hop', 'Jazz', 'Latin', 'Pop', 'Rap', 'Rock', 'Other'])
    
class MemberRequestForm(FlaskForm):
    instrument = SelectField(u'Instrument', choices=['Drums', 'Vocals', 'Electroguitar', 'Bass Guitar', 'Piano'])
    pref_gender = SelectField(u'Gender', validators=[Optional()], choices=['Male', 'Female'])
    goal = SelectField(u'Goal', validators=[Optional()], choices=['Fun', 'Socializing', 'Concerts - Serious', 'Concerts - Relaxed'])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])