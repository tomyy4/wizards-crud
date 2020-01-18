
class HouseService:
    def __init__(self, repository):
        self.repository = repository

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

    def update_house(self, id, name, max_students):
        return self.repository.update(id, name, max_students)

    def delete_house(self, id):
        return self.repository.delete(id)


class HouseIsNotFull:
    def __init__(self, house_id, service):
        self.house_id = house_id
        self.h_service = service

    def execute(self):
        house = self.h_service.get_house_by_id(self.house_id)

        return False if house.max_students > 50 else True


class CanCreateHouse:
    def __init__(self, max_students,teaches_dark_arts):
        self.max_students = max_students
        self.teaches_dark_arts = teaches_dark_arts
        self.less_than_50_students = HouseHasLessThan50Students(self.max_students)
        self.house_does_not_teaches_dark_arts = HouseDoesNotTeachDarkArts(self.teaches_dark_arts)

    def execute(self):
        if not self.less_than_50_students.execute():
            return False

        if not self.house_does_not_teaches_dark_arts.execute():
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

