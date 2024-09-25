from app import app
from models import db, Cupcake


def seed_cupcake_data():
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    db.session.add_all([c1, c2])
    db.session.commit()
    print('DATA SEEDED>>>>>')

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.query(Cupcake).delete()
    seed_cupcake_data()