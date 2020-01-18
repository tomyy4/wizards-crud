from flask_seeder import Seeder
from models.models import House


class HouseSeeder(Seeder):
  def run(self):

    houses = {House(1, 'Griffindor', 50),House(1, 'Slytherin', 50) }

    for house in houses:
        print('importing house')
        self.db.session.add(house)

