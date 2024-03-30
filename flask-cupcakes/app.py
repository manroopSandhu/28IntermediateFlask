"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route("/")
def root():
    """Render homepage"""

    return render_template("index.html")

@app.route('/api/cupcakes')
def list_cupcakes():
    """return all cupcakes in system
    Returns JSON like:
    {cupcakes: [{id, flavor, rating, size, image}]}"""

    # fetches all cupcake objects from the database. 
    # "cupcakes.to_dict()" is a method defined for upcake objects. it converts cupcakes object into a dictionary represtation
    cupcakes = [cupcakes.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Add cupcake, return data about new cupcake
    
    Returns JSON like:
    {cupcake: [{id, flavor, rating, size, image}]}"""

    data = request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None
    )
    db.session.add(cupcake)
    db.session.commit()

    #post requests should return HTTP status of 201 created
    return (jsonify(cupcake=cupcake.to_dict()), 201)

@app.route('/api/cupcakes/<int:cupcake_id')
def get_cupcake(cupcake_id):
    """return data on specific cupcake
    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_addict())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake from data in request, return updated data
    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}"""
    
    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())

@app.route('api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def remove_cupcake(cupcake_id):
    """Delete cupcake and return confirmation message
    Returns JSON of {message: "DElETED"}"""

    cupcake =Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="DELETED")