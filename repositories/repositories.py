# flask-SQLAlchemy repositories
from models.models import Wizard, House


class WizardRepository:

    def all(self):
        return Wizard.query.all()

    def get_by_id(self, id):
        return Wizard.query.get(id)

    def create(self, **kwargs):
        return Wizard.create(**kwargs)


class HouseRepository:

    def all(self):
        return House.query.all()

    def get_by_id(self, id):
        return House.query.get(id)

    def create(self, args):
        pass