import unittestimport unittest
from flask import json
from project.app import create_app
from project.app.models import users, User

class UsersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True
        #testowe dane
        users.clear()
        users.append(User(_id=1, name="Jan", lastname="Kowalski"))
        users.append(User(_id=2, name="Anna", lastname="Nowak"))

    def test_get_users(self):
        response = self.app.get('/users')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_get_user(self):
        response = self.app.get('/users/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], "Jan")

    def test_get_user_not_found(self):
        response = self.app.get('/users/3')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        response = self.app.post('/users', json={"name": "Piotr", "lastname": "Wiœniewski"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['name'], "Piotr")

    def test_update_user(self):
        response = self.app.patch('/users/1', json={"name": "Pawe³"})
        self.assertEqual(response.status_code, 204)
        self.assertEqual(users[0].name, "Pawe³")

    def test_replace_user(self):
        response = self.app.put('/users/1', json={"name": "Pawe³", "lastname": "Górski"})
        self.assertEqual(response.status_code, 204)
        self.assertEqual(users[0].lastname, "Górski")

    def test_delete_user(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(users), 1)

    def test_create_user_with_invalid_data(self):
        response = self.app.post('/users', json={"name": "Bez Nazwiska"})
        self.assertEqual(response.status_code, 400)

    def test_update_user_not_found(self):
        response = self.app.patch('/users/3', json={"name": "Nieistniej¹cy"})
        self.assertEqual(response.status_code, 404)

    def test_replace_user_with_invalid_data(self):
        response = self.app.put('/users/1', json={"name": "Tylko Imiê"})
        self.assertEqual(response.status_code, 400)

    def test_delete_user_not_found(self):
        response = self.app.delete('/users/3')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()


#skoñczone 