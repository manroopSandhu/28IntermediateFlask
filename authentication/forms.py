from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


# create a class loginForm with the FlaskForm parameter
class loginForm(FlaskForm):
    """Login Form"""

    # set the username to a stringfield and make it's validators required with the min length 1 and max 20
    username = StringField(
        "username", validators=[InputRequired(), Length(min=1, max=20)],)

    # set the password to a passwordfield and make it's validators required with the min 6 and max 55
    password = PasswordField("password", validators=[InputRequired(), Length(min=6, max=55)],)

    # create a class register form with the FlaskForm parameter
    class registerForm(FlaskForm):

        # set the username to a stringfield and make it's validators required with the min length 1 and max 20
        username = StringField("username", validators=[InputRequired(), Length(min=1, max=20)],)

        # set the password to a passwordfield and make it's validators required with the min 6 and max 55
        password = PasswordField("password", validators= [InputRequired(), Length(min=1, max=20)],)

        # set the email to a stringField and give it the 
        email = StringField("Email", validators=[InputRequired(), Email(), Length(max=50)],)

        # set the first_name & last_name to a stringField and make its validators required with a max length of 30
        first_name = StringField("First Name", validators=[InputRequired(), Length(max=30)],)

        last_name = StringField("Last Name", validators=[InputRequired(), Length(max=30)],)

    # create a FeedbackForm with the FlaskForm parameter
    class FeedbackForm(FlaskForm):
        """Add feedback Form"""

        title = StringField("Title", validators=[InputRequired(), Length(max=100)],)

        content = StringField("Content", validators=[InputRequired()])

    class DeleteForm(FlaskForm):
        """"""