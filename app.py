from flask import Flask, render_template
from repositories.repositories import WizardRepository, HouseRepository
from services.services import WizardService, HouseService
from db.database import db
from db.config import config


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = config['sqlite']
app.config['SQLALCHEMY_DATABASE_URI'] = config['mysql']
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
    return render_template('wizards.html', wizards=wizards)


@app.route('/wizard/<int:wizard_id>')
def wizard_by_id(wizard_id):
    service = WizardService(WizardRepository)
    wizard = service.get_wizard_by_id(wizard_id)
    return render_template('wizard.html', wizard=wizard)


@app.route('/wizard/new')
def create_wizard():
    service = HouseService(HouseRepository)
    houses = service.get_all_houses()
    return render_template('new_wizard.html', houses=houses)


@app.route('/houses')
def houses():
    service = HouseService(HouseRepository)
    houses = service.get_all_houses()
    return render_template('houses.html', houses=houses)


@app.route('/house/<int:house_id>')
def house_by_id(house_id):
    service = HouseService(HouseRepository)
    house = service.get_house_by_id(house_id)
    return render_template('house.html', house=house)

if __name__ == '__main__':
    app.run(debug=True)



