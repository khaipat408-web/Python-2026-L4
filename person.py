class Person:
    def __init__(self, person_id, name, dob):
        self._id = person_id
        self._name = name
        self._dob = dob
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob