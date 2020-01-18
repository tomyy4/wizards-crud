from db.database import db


class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    max_students = db.Column(db.Integer, nullable=False)
    students = db.relationship('Wizard', backref='students', lazy=True)

    def __repr__(self):
        return self.name


class Wizard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    house = db.relationship('House')

    def __repr__(self):
        return self.name
