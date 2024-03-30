from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app"""

    db.app = app
    db.init_app(app)

    # create a user class
    class User(db.Model):

        # give the tablename the title of "users"
        __tablename__ = "users"

        # set the usernames to a column with a max string of 20, cannot be left empty, needs to be unique, and is the primary key
        usersnames = db.Column(db.String(20), nullable=False, unique=True, primary_key=True)

        # set the passwords to be a column with the text attribute and cannot be empty
        passwords = db.Column(db.Text(), nullable=False)

        # set the email to be a Column with the String attribute and cannot be empty
        email = db.Column(db.String(50), nullable=False)

        # set the first_name to be a column with the string attribute and cannot be empty
        first_name = db.Column(db.String(30), nullable=False)

        last_name = db.Column(db.String(30), nullable=False)

        # set the feedback to be a relationship 
        feedback = db.relationship("Feedback", backref="user", cascase="all, delete")


        @classmethod
        def register(cls, username, password, first_name, last_name, email):
            """Register a user hasing thier password"""

            hashed = bcrypt.generate_password_hash(password)

            hashed_utf8 = hashed.decode("utf8")
            user = cls(username=username, password=hashed_utf8, first_name=first_name, last_name=last_name, email=email)

            db.session.add(user)

            return user
        
        @classmethod
        def authenticate(cls, username, password):
            user = User.query.filter_by(username=username).first()

            if user and bcrypt.check_password_hash(user.password, password):
                return user
            else:
                return False
        
        class Feedback(db.Model):
            """Feedback."""

            __tablename__ = "feedback"

            id = db.Column(db.Integer, primary_key=True)
            title = db.Column(db.String(100), nullable=False)
            content = db.Column(db.Text, nullable=False)
            username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False,)