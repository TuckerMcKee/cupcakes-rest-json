"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

def serialize_obj(obj):
    id = obj.id
    flavor = obj.flavor
    size = obj.size
    rating = obj.rating
    image = obj.image
    return {'id':id,'flavor':flavor,'size':size,'rating':rating,'image':image}

class Cupcake(db.Model):
    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text,nullable=False)
    rating = db.Column(db.Float,nullable=False)
    image = db.Column(db.Text, default='https://tinyurl.com/demo-cupcake', nullable=False)
