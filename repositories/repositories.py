# flask-SQLAlchemy repositories
from models.models import Wizard, House
from db.database import db
from abc import ABC


class BaseWizardRepository(ABC):
    def all(self):
        pass

    def get_by_id(self):
        pass

    def create(self, name, age, house_id):
        pass

    def update(self, wizard_id, new_name, new_age, new_house_id):
        pass

    def delete(self, id):
        pass

    def get_by_name(self, name):
        pass


class BaseHouseRepository(ABC):
    def all(self):
        pass

    def get_by_id(self):
        pass

    def create(self, name, max_students):
        pass

    def update(self, house_id, new_name,max_students):
        pass

    def delete(self, id):
        pass

    def get_by_name(self, name):
        pass


class WizardRepository(BaseWizardRepository):

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
        w.name = new_name
        w.age = new_age
        w.house_id = new_house_id

        db.session.add(w)
        db.session.commit()

    def delete(self, id):
        return Wizard.query.filter_by(id=id).delete()

    def get_by_name(self, name):
        return Wizard.query.filter_by(name=name).first()


class HouseRepository(BaseHouseRepository):

    def all(self):
        return House.query.all()

    def get_by_id(self, id):
        return House.query.get(id)

    def create(self, name, max_students):
        h = House(name=name, max_students=max_students)

        db.session.add(h)
        db.session.commit()

    def update(self, house_id, new_name,max_students):
        h = House.query.get(house_id)
        h.name = new_name
        h.max_students = max_students

        db.session.add(h)
        db.session.commit()

    def delete(self, id):
        return House.query.filter_by(id=id).delete()

    def get_by_name(self, name):
        return House.query.filter_by(name=name).first()
