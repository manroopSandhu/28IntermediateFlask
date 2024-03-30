from flask_sqlalchemy import SQLAlchemy
GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

class Pet(db.Model):
    """Adoptable pets"""
    # the tablename should be pets
    __tablename__ = "pets"

    # the id Column should be an integer and increment
    id = db.Column(db.Integer, primary_key=True)
    # the name Column should be a text and it needs to be filled in
    name = db.Column(db.text, nullable=False)
    # the species Column should be a text and it needs to be filled in
    species = db.Column(db.text, nullable=False)
    # the photo_url Column needs to be a text
    photo_url = db.Column(db.Text)
    # the age Column needs to be an integer
    age = db.Column(db.Integer)
    # the notes need to be a text
    notes = db.Column(db.Text)
    # the available column needs to be true or false. it needs to be filled in and should be defaulted to true
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image for pet"""

        return self.photo_url or GENERIC_IMAGE
    
    def connect_db(app):
        """connect this database to provided Flask app
        
        You should call this in your Flask app"""

        db.app = app
        db.init_app(app)

        