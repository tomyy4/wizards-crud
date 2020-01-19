from flask import Blueprint, render_template, request
from services.house_services import HouseService
from services.wizard_services import WizardService

from repositories.repositories import WizardRepository, HouseRepository

wizard = Blueprint('wizard', __name__,template_folder='templates/',static_folder='static')


@wizard.route('/wizards', methods=['GET'])
def wizards():
    service = WizardService(WizardRepository())
    wizards = service.get_all_wizards()

    return render_template('wizard/wizards.html', wizards=wizards)


@wizard.route('/wizard/<int:wizard_id>')
def wizard_by_id(wizard_id):
    service = WizardService(WizardRepository())
    wizard = service.get_wizard_by_id(wizard_id)

    return render_template('wizard/wizard.html', wizard=wizard) if wizard else render_template('wizard/wizard_not_found.html')


@wizard.route('/wizard/new', methods=['GET','POST'])
def create_wizard():
    h_service = HouseService(HouseRepository())
    houses = h_service.get_all_houses()

    if request.method == 'POST':
        service = WizardService(WizardRepository())
        new_wizard = service.create_wizard(
            request.form['wizard_name'],
            request.form['wizard_age'],
            request.form['has_received_letter'],
            request.form['voldemort_friend'],
            request.form['dark_wizard'],
            request.form['house_options'],
        )

        if new_wizard:
            return render_template('wizard/wizard_success.html')
        return render_template('wizard/wizard_error.html')

    return render_template('wizard/new_wizard.html', houses=houses)


@wizard.route('/wizard/update/<int:wizard_id>', methods=['GET','POST'])
def update_wizard(wizard_id):
    w_service = WizardService(WizardRepository())
    h_service = HouseService(HouseRepository())
    houses = h_service.get_all_houses()

    if request.method == 'POST':
        w_service.update_wizard(
            request.form['wizard_id'],
            request.form['wizard_name'],
            request.form['wizard_age'],
            request.form['wizard_house'])

    wizard = w_service.get_wizard_by_id(wizard_id)
    current_house = h_service.get_house_by_id(wizard.house_id)

    if wizard is not None:
        return render_template('wizard/update_wizard.html',
                                wizard=wizard,
                               houses=houses,
                               current_house=current_house)
    else:
        return render_template('wizard/wizard_not_found.html')


@wizard.route('/wizard/delete', methods=['GET','POST'])
def delete_wizard():
    service = WizardService(WizardRepository())
    wizards = service.get_all_wizards()

    if request.method == 'POST':
        service.delete_wizard(request.form['wizards_id'])

        return render_template('wizard/wizards.html', wizards=wizards)

    return render_template('wizard/delete_wizard.html', wizards=wizards)

