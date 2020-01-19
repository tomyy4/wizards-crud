

class WizardService:
    def __init__(self, repository):
        self.repository = repository

    def get_all_wizards(self):
        return self.repository.all()

    def get_wizard_by_id(self, wizard_id):
        return self.repository.get_by_id(wizard_id)

    def create_wizard(self, name, age, has_received_letter, dark_wizard, voldemort_friend, house_id):
        s = CanRegisterWizard(age, has_received_letter,dark_wizard, voldemort_friend, house_id)
        can_register_wizard = s.execute()

        if can_register_wizard:
            self.repository.create(name, age, house_id)
            return True

        return False

    def update_wizard(self, wizard_id, name, age, house_id):
        return self.repository.update(wizard_id, name, age, house_id)

    def delete_wizard(self, id):
        return self.repository.delete(id)


class CanRegisterWizard:
    def __init__(self, age, letter, dark_wizard, voldemort_friend, house_id):
        self.age = age
        self.letter = letter
        self.dark_wizard = dark_wizard
        self.voldemort_friend = voldemort_friend
        self.house_id = house_id
        self.wizard_has_proper_age = WizardHasProperAge(self.age)
        self.has_received_letter = HasReceivedLetter(self.letter)
        self.wont_turn_dark_mage = WizardWontTurnIntoADarkMage(self.dark_wizard)
        self.is_not_voldemort_friend = WizardIsNotFriendWithVoldemort(self.voldemort_friend)

    def execute(self):
        if not self.has_received_letter.execute():
            False

        if not self.wizard_has_proper_age.execute():
            return False

        if not self.wont_turn_dark_mage.execute():
            return False

        if not self.is_not_voldemort_friend.execute():
            return False

        return True


class WizardHasProperAge:
    def __init__(self, age):
        self.age = age

    def execute(self):
        return False if int(self.age) > 18 else True


class WizardWontTurnIntoADarkMage:
    def __init__(self, dark_wizard):
        self.dark_wizard = dark_wizard

    def execute(self):
        return int(self.dark_wizard) == 0


class WizardIsNotFriendWithVoldemort:
    def __init__(self, friend_with_voldemort):
        self.friend_with_voldemort = friend_with_voldemort

    def execute(self):
        return int(self.friend_with_voldemort) == 0


class HasReceivedLetter:
    def __init__(self, has_received_letter):
        self.has_received_letter = has_received_letter

    def execute(self):
        return int(self.has_received_letter) == 1

