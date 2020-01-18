

class Wizard:
    def __init__(self, name, age, has_received_letter, dark_wizard, voldemort_friend, house_id):
        self.name = name
        self.age = age
        self.has_received_letter = has_received_letter
        self.dark_wizard = dark_wizard
        self.voldemort_friend = voldemort_friend
        self.house_id = house_id


class House:
    def __init__(self, name, max_students, teaches_dark_arts):
        self.name = name
        self.students = max_students
        self.teaches_dark_arts = teaches_dark_arts
