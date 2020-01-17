from flask import Flask
from repositories.repositories import WizardRepository, HouseRepository
from services.services import WizardService, HouseService
from db.database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Hello World'


@app.route('/wizards')
def wizards():
    service = WizardService(WizardRepository)
    wizards = service.get_all_wizards()
    wizard_names = {w.name for w in wizards}
    return 'wizards'


@app.route('/houses')
def houses():
    service = HouseService(HouseRepository)
    houses = service.get_all_houses()
    return 'houses'


if __name__ == '__main__':
    app.run(debug=True)



