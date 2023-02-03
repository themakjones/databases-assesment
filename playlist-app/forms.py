"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name', validators=[InputRequired(message=['Name is required']), Length(min=1, max=30, message=['Name should be between 1 and 30 characters long'])])
    description = StringField('Description', validators=[Length(max=100, message=['Description cannot be more than 100 characters long'])])

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired(message=['Title is required']), Length(max=50, message=['Title should be less than 50 characters'])])
    artist = StringField('Artist Name', validators=[InputRequired(message=['Artist name is required']), Length(max=50, message=['Artist name should be less than 50 characters'])])

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
