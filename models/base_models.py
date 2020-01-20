

class Wizard:
    def __init__(self, id, name, age, house_id):
        self.id = id
        self.name = name
        self.age = age
        self.house_id = house_id


class House:
    def __init__(self, id, name, max_students):
        self.id = id
        self.name = name
        self.students = max_students
