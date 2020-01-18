from repositories.repositories import WizardRepository, HouseRepository


class WizardService:
    def __init__(self, repository):
        self.repository = WizardRepository()

    def get_all_wizards(self):
        return self.repository.all()

    def get_wizard_by_id(self, wizard_id):
        return self.repository.get_by_id(wizard_id)

    def create_wizard(self, name, house_id):
        return self.repository.create(name, house_id)

    def update_wizard(self, wizard_id, name, house_id):
        return self.repository.update(wizard_id, name, house_id)

    def delete_wizard(self, id):
        return self.repository.delete(id)


class HouseService:
    def __init__(self, repository):
        self.repository = HouseRepository()

    def get_all_houses(self):
        return self.repository.all()

    def get_house_by_id(self, id):
        return self.repository.get_by_id(id)

    def create_house(self, name):
        return self.repository.create(name)

    def update_house(self, id, name):
        return self.repository.update(id, name)

    def delete_house(self, id):
        return self.repository.delete(id)

