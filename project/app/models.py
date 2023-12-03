class User:
    def __init__(self, _id, name, lastname):
        self.id = _id
        self.name = name
        self.lastname = lastname

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname
        }

users = []
