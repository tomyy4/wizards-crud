from flask import Blueprint, render_template, request
from services.house_services import HouseService
from repositories.repositories import HouseRepository


house = Blueprint('house', __name__,template_folder='templates/',static_folder='static')


@house.route('/houses')
def houses():
    service = HouseService(HouseRepository())
    houses = service.get_all_houses()

    return render_template('house/houses.html', houses=houses)


@house.route('/house/<int:house_id>')
def house_by_id(house_id):
    service = HouseService(HouseRepository())
    house = service.get_house_by_id(house_id)
    return render_template('house/house.html', house=house)


@house.route('/house/new', methods=['GET','POST'])
def create_house():
    if request.method == 'POST':
        name = request.form['house_name']
        max_students = request.form['max_students']
        teaches_dark_arts = request.form['teaches_dark_arts']
        service = HouseService(HouseRepository())
        success = service.create_house(name, max_students, teaches_dark_arts)

        if success:
            return render_template('house/house_success.html')
        return render_template('house/house_error.html')

    return render_template('house/new_house.html')


@house.route('/house/update/<int:house_id>', methods=['GET','POST'])
def update_house(house_id):
    service = HouseService(HouseRepository())

    if request.method == 'POST':
        service.update_house(
            request.form['house_id'],
            request.form['house_name'],
        )

        return render_template('house/houses.html')

    house = service.get_house_by_id(house_id)

    if house is None:
        return 'Not Found'

    return render_template('house/update_house.html', house=house)


@house.route('/house/delete', methods=['GET','POST'])
def delete_house():
    service = HouseService(HouseRepository())
    houses = service.get_all_houses()

    if request.method == 'POST':
        service.delete_house(request.form['houses_id'])

        return render_template('house/houses.html', houses=houses)

    return render_template('house/delete_house.html', houses=houses)
