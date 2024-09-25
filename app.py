"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secretkey'

connect_db(app)
with app.app_context():
    db.create_all()
