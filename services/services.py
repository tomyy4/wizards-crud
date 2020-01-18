from repositories.repositories import WizardRepository, HouseRepository


class WizardService:
    def __init__(self, repository):
        self.repository = WizardRepository()

    def get_all_wizards(self):
        return self.repository.all()

    def get_wizard_by_id(self, wizard_id):
        return self.repository.get_by_id(wizard_id)

    def create_wizard(self, name,age, house_id):
        can_register_wizard = WizardHasReceivedLetter()
        return self.repository.create(name, age, house_id) if can_register_wizard else False

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

    def create_house(self, name, max_students):
        return self.repository.create(name, max_students)

    def update_house(self, id, name):
        return self.repository.update(id, name)

    def delete_house(self, id):
        return self.repository.delete(id)


# class WizardHasProperAge:
#    def __init__(self, age):
#        self.age = age

#    def execute(self):
#        return True if self.age < 18 else False and print('fuck you')


class WizardHasReceivedLetter:
    def __init__(self):
        self.execute()

    def execute(self):
        import random
        bool(random.getrandbits(1))

# Student can join a new subject


