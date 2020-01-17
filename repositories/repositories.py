# flask-SQLAlchemy repositories
from models.models import Wizard, House


class WizardRepository:

    def all_wizards(self):
        return Wizard.query.all()


class HouseRepository:

    def all_houses(self):
        return House.query.all()
