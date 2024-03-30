from flask import Flask, url_for, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "Mouse123"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension

@app.route("/")
def list_pets():
    """List all pets"""

    # Retrieve all the data from Pet
    pets = Pet.query.all()
    return render_template("pet_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet"""

    # create an alias for AddPetForm from forms
    form = AddPetForm()
    
    # check if form is a POST request and if it is valid
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # set create an alias for "Pet" and all the data that comes before it with the alias name of new_pet
        new_pet = Pet(**data)
        # add the new_pet onto the session
        db.session.add(new_pet)
        # commit it
        db.session.commit()
        # flash a message saying the "new_pet's name" has been added
        flash(f"{new_pet.name} added.")
        # redirect to the list_pets URl
        return redirect(url_for('list_pets'))
    # else
    else:
        # represent form for editing
        return render_template("pet_add_form.html", form=form)
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    # if form is POST on submit 
    if form.validate_on_submit():
        # pet.notes = the notes data entered on the form
        pet.notes = form.notes.data
        # pet.available = the availibility data enterd on the form
        pet.available = form.available.data
        # pet.photo_url = the photo_url data on the form
        pet.photo_url = form.photo_url.data
        # commit this session
        db.session.commit()
        # flash a message saying the pet.name updated
        flash(f"{pet.name} updated.")
        # redirect to the url for list_pets
        return redirect(url_for('list_pets'))
    # else
    else:
        # failed; re-present form for editing
        return render_template("pet_edit_form.html", form=form, pet=pet)
    
@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    # set info to the pet.name and pet.age 
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)