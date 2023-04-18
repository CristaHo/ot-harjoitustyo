import unittest
from budget import Budget


class TestUser(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_budget(self):
        budget = Budget("1500", "500")
        
        
        self.assertEqual(budget.create_budget(), 1000)