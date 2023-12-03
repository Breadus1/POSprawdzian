import unittest
from app import create_app

class UsersTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
#Musze skonczyc okok

if __name__ == '__main__':
    unittest.main()
