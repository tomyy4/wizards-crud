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


@app.route('/wizards', methods=['GET'])
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
        age = request.form['wizard_age']
        house_id = request.form['house_options']
        service = WizardService(WizardRepository)

        wizard_ok = render_template('wizard_success.html')
        wizard_not_ok = render_template('wizard_error.html')
        return wizard_ok if service.create_wizard(name, age, house_id) else wizard_not_ok

    h_service = HouseService(HouseRepository)
    houses = h_service.get_all_houses()
    # houses_ids = [h.id for h in houses]
    return render_template('new_wizard.html', houses=houses)


@app.route('/wizard/update/<int:wizard_id>', methods=['GET','POST'])
def update_wizard(wizard_id):
    w_service = WizardService(WizardRepository)
    h_service = HouseService(HouseService)
    houses = h_service.get_all_houses()
    if request.method == 'POST':
        w_service.update_wizard(
            request.form['wizard_id'],
            request.form['wizard_name'],
            request.form['wizard_house'])

        return render_template('wizards_success.html')

    wizard = w_service.get_wizard_by_id(wizard_id)

    if wizard is None:
        return 'Not Found'

    current_house = h_service.get_house_by_id(wizard.house_id)

    return render_template('update_wizard.html', wizard=wizard, houses=houses, current_house=current_house)

@app.route('/wizard/delete', methods=['GET','POST'])
def delete_wizard():
    service = WizardService(WizardRepository)
    wizards = service.get_all_wizards()

    if request.method == 'POST':
        service.delete_wizard(request.form['wizards_id'])

        return render_template('wizards.html', wizards=wizards)

    return render_template('delete_wizard.html', wizards=wizards)


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
        max_students = request.form['max_students']
        service = HouseService(HouseRepository)
        create = service.create_house(name, max_students)
        house_success = render_template('house_success.html')
        house_error = render_template('house_error.html')
        return house_success if create else house_error

    return render_template('new_house.html')


@app.route('/house/update/<int:house_id>', methods=['GET','POST'])
def update_house(house_id):
    service = HouseService(HouseRepository)

    if request.method == 'POST':
        service.update_house(
            request.form['house_id'],
            request.form['house_name'],
        )

        return render_template('houses.html')

    house = service.get_house_by_id(house_id)

    if house is None:
        return 'Not Found'

    return render_template('update_house.html', house=house)


@app.route('/house/delete', methods=['GET','POST'])
def delete_house():
    service = HouseService(HouseRepository)
    houses = service.get_all_houses()

    if request.method == 'POST':
        service.delete_house(request.form['houses_id'])

        return render_template('houses.html', houses=houses)

    return render_template('delete_house.html', houses=houses)


if __name__ == '__main__':
    app.run(debug=True)




