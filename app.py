from flask import Flask, render_template, request, redirect, url_for
from repositories.repositories import WizardRepository, HouseRepository
from services.services import WizardService, HouseService
from db.database import db
from db.config import config
import pdb
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = config['sqlite']
app.config['SQLALCHEMY_DATABASE_URI'] = config['mysql']
app.config['SECRET_KEY'] = SECRET_KEY
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


@app.route('/wizard/new', methods=['GET','POST'])
def create_wizard():

    if request.method == 'POST':
        name = request.form['wizard_name']
        house_id = request.form['house_options']
        service = WizardService(WizardRepository)
        service.create_wizard(name,house_id)

        return render_template('wizard_success.html')

    h_service = HouseService(HouseRepository)
    houses = h_service.get_all_houses()
    # houses_ids = [h.id for h in houses]
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


@app.route('/house/new', methods=['GET','POST'])
def create_house():
    if request.method == 'POST':
        name = request.form['house_name']
        service = HouseService(HouseRepository)
        service.create_house(name)

        return render_template('house_success.html')

    return render_template('new_house.html')


if __name__ == '__main__':
    app.run(debug=True)




