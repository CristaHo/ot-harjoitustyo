import unittest
from users import UserRepository
from database_connection import get_database_connection

class TestUser(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_user(self):
        user = UserRepository(get_database_connection())
        user.create_user("test", "password")
        
        self.assertEqual((user.find_user("test", "password")[0], user.find_user("test", "password")[1]), ("test", "password"))
        