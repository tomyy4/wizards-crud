from repositories.repositories import WizardRepository, HouseRepository


class WizardService:
    def __init__(self, repository):
        self.repository = WizardRepository()

    def get_all_wizards(self):
        return self.repository.all()

    def get_wizard_by_id(self, wizard_id):
        return self.repository.get_by_id(wizard_id)

    def create_wizard(self, **kwargs):
        return self.repository.create(**kwargs)


class HouseService:
    def __init__(self, repository):
        self.repository = HouseRepository()

    def get_all_houses(self):
        return self.repository.all()

    def get_house_by_id(self, id):
        return self.repository.get_by_id(id)

