# flask-SQLAlchemy repositories
from models.models import Wizard, House
from db.database import db


class WizardRepository:

    def all(self):
        return Wizard.query.all()

    def get_by_id(self, id):
        return Wizard.query.get(id)

    def create(self, name, age, house_id):
        w = Wizard(name=name, age=age, house_id=house_id)

        db.session.add(w)
        db.session.commit()

    def update(self, wizard_id, new_name, new_age, new_house_id):
        w = Wizard.query.get(wizard_id)

        return w.query.update({'name': new_name, 'age': new_age, 'house_id': new_house_id})

    def delete(self, id):
        return Wizard.query.filter_by(id=id).delete()


class HouseRepository:

    def all(self):
        return House.query.all()

    def get_by_id(self, id):
        return House.query.get(id)

    def create(self, name, max_students):
        h = House(name=name, max_students=max_students)

        db.session.add(h)
        db.session.commit()


    def update(self, house_id, new_name,max_students):
        h = House.query.get(house_id, max_students)

        return h.query.update({'name': new_name, 'max_students':max_students})

    def delete(self, id):
        return House.query.filter_by(id=id).delete()


