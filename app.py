"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, redirect, flash, session, jsonify
from models import db, Cupcake, connect_db, serialize_obj

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secretkey'

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/api/cupcakes')
def get_all_cupcakes():
    """send all cupcake data"""
    cupcakes = [serialize_obj(obj) for obj in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """send data for one cupcake"""
    cupcake = serialize_obj(Cupcake.query.get_or_404(cupcake_id))
    return jsonify(cupcake=cupcake)

@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    """create new cupcake row"""
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    new_cupcake = Cupcake(flavor=flavor,size=size,rating=rating,image=image)
    return jsonify(cupcake=serialize_obj(new_cupcake))

        
