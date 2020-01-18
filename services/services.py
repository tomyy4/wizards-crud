from repositories.repositories import WizardRepository, HouseRepository


class WizardService:
    def __init__(self):
        self.repository = WizardRepository()

    def get_all_wizards(self):
        return self.repository.all()

    def get_wizard_by_id(self, wizard_id):
        return self.repository.get_by_id(wizard_id)

    def create_wizard(self, name, age, has_received_letter, house_id):
        s = CanRegisterWizard(age, has_received_letter, house_id)
        can_register_wizard = s.execute()

        if can_register_wizard:
            self.repository.create(name, age, house_id)
            return True

        return False

    def update_wizard(self, wizard_id, name, house_id):
        return self.repository.update(wizard_id, name, house_id)

    def delete_wizard(self, id):
        return self.repository.delete(id)


class HouseService:
    def __init__(self):
        self.repository = HouseRepository()

    def get_all_houses(self):
        return self.repository.all()

    def get_house_by_id(self, id):
        return self.repository.get_by_id(id)

    def create_house(self, name, max_students, teaches_dark_arts):
        s = CanCreateHouse(max_students, teaches_dark_arts)
        can_register_house = s.execute()

        if can_register_house:
            self.repository.create(name, max_students)
            print('success')
            return True

        return False

    def update_house(self, id, name):
        return self.repository.update(id, name)

    def delete_house(self, id):
        return self.repository.delete(id)


class CanRegisterWizard:
    def __init__(self, age, has_received_letter, house_id):
        self.age = age
        self.has_received_letter = has_received_letter
        self.house_id = house_id
        self.wizard_has_proper_age = WizardHasProperAge(self.age)
        self.has_received_letter = HasReceivedLetter(self.has_received_letter)
        self.house_is_not_full = HouseIsNotFull(self.house_id)

    def execute(self):
        if not self.has_received_letter.execute():
            print('Wizard has not received letter')
            False

        if not self.house_is_not_full.execute():
            print('House is Full')
            return False

        if not self.wizard_has_proper_age.execute():
            print('Wizard has not proper age')
            return False

        return True


class WizardHasProperAge:
    def __init__(self, age):
        self.age = age

    def execute(self):
        return False if int(self.age) > 18 else True


# Student can join a new subject


class HasReceivedLetter:
    def __init__(self, has_received_letter):
        self.has_received_letter = has_received_letter

    def execute(self):
        return False if self.has_received_letter == 0 else True


class HouseIsNotFull:
    def __init__(self, house_id):
        self.house_id = house_id
        self.h_service = HouseService()

    def execute(self):
        house = self.h_service.get_house_by_id(self.house_id)

        return False if house.max_students > 10 else True


class CanCreateHouse:
    def __init__(self, max_students,teaches_dark_arts):
        self.max_students = max_students
        self.teaches_dark_arts = teaches_dark_arts
        self.less_than_50_students = HouseHasLessThan50Students(self.max_students)
        self.house_does_not_teaches_dark_arts = HouseDoesNotTeachDarkArts(self.teaches_dark_arts)

    def execute(self):
        if not self.less_than_50_students.execute():
            print('House already has more thatn 50 students')
            return False

        if not self.house_does_not_teaches_dark_arts.execute():
            print('Houses can\'t teach dark arts')
            return False

        return True


class HouseHasLessThan50Students:
    def __init__(self, max_students):
        self.max_students = max_students

    def execute(self):
        return int(self.max_students) < 51


class HouseDoesNotTeachDarkArts:
    def __init__(self, teaches_dark_arts):
        self.teaches_dark_arts = teaches_dark_arts

    def execute(self):
        return int(self.teaches_dark_arts) == 0
