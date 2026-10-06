class Course:
    def __init__(self, course_id, name, credits_num):
        self._id = course_id
        self._name = name
        self._credits = credits_num

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_credits(self):
        return self._credits