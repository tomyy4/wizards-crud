from repositories.repositories import WizardRepository, HouseRepository


class WizardService:
    def __init__(self, repository):
        self.repository = WizardRepository()

    def get_all_wizard(self):
        return self.repository.all_wizards()


class HouseService:
    def __init__(self, repository):
        self.repository = HouseRepository()

    def get_all_houses(self):
        return self.repository.all_houses()