import unittest
from models.base_models import Wizard, House
from services.house_services import HouseService
from services.wizard_services import WizardService
from repositories.repositories import BaseWizardRepository, BaseHouseRepository


class CreateWizardTest(unittest.TestCase):
    def test_wizard_is_created_with_right_parameters(self):
        w = Wizard('Harry',17, 1, 0, 0, 1)

        b = BaseWizardRepository()
        service = WizardService(b)
        create_wizard = service.create_wizard(
            w.name, w.age, w.has_received_letter, w.dark_wizard, w.voldemort_friend, w.house_id
        )
        self.assertTrue(create_wizard)

    def test_cannot_create_wizard_older_than_18_wizard(self):
        w = Wizard('Harry',19,1 ,0 ,0, 1)
        b = BaseWizardRepository()
        service = WizardService(b)
        create_wizard = service.create_wizard(
            w.name, w.age, w.has_received_letter, w.dark_wizard, w.voldemort_friend, w.house_id
        )
        self.assertFalse(create_wizard)

    def test_cannot_register_if_has_not_received_letter(self):
        w = Wizard('Harry',19, 0, 0, 0, 1)
        b = BaseWizardRepository()
        service = WizardService(b)
        create_wizard = service.create_wizard(
            w.name, w.age, w.has_received_letter, w.dark_wizard, w.voldemort_friend, w.house_id
        )
        self.assertFalse(create_wizard)


    def test_cannot_register_if_will_turn_into_dark_mage(self):
        w = Wizard('Harry', 15, 1, 1, 0, 1)
        b = BaseWizardRepository()
        service = WizardService(b)
        create_wizard = service.create_wizard(
            w.name, w.age, w.has_received_letter, w.dark_wizard, w.voldemort_friend, w.house_id
        )
        self.assertFalse(create_wizard)

    def test_cannot_register_if_is_friend_with_voldemort(self):
        w = Wizard('Harry', 15, 1, 0, 1, 1)
        b = BaseWizardRepository()
        service = WizardService(b)
        create_wizard = service.create_wizard(
            w.name, w.age, w.has_received_letter, w.dark_wizard, w.voldemort_friend, w.house_id
        )
        self.assertFalse(create_wizard)

class CreateHouseTest(unittest.TestCase):
    def test_cannot_create_house_if_teaches_dark_arts(self):
        h = House('Griffindor', 50, 1)
        repo = BaseHouseRepository()
        service = HouseService(repo)
        create_house = service.create_house(h.name, h.students, h.students)
        self.assertFalse(create_house)

    def test_house_cannot_have_more_thant_50_students(self):
        h = House('Griffindor', 51, 1)
        repo = BaseHouseRepository()
        service = HouseService(repo)
        create_house = service.create_house(h.name, h.students, h.students)
        self.assertFalse(create_house)

if __name__ == "__main__":
    unittest.main()
