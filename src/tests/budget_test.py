import unittest
from budgetapp import Budget

class TestBudget(unittest.TestCase):
    def setUp(self):
        pass

    def test_income_and_expenses(self):
        budget = Budget()
        budget.add_income(1500, "salary")
        budget.add_monthly_expense(500, "rent")
        
        self.assertEqual(str(budget), "Kuukauden budjettisi on 1000 euroa")
    
    def test_daily_budget(self):
        budget = Budget()
        budget.add_income(2000, "salary")
        budget.add_monthly_expense(500, "rent")
        budget.buddget_defining()

        self.assertEqual(str(budget.monthly_budget(1)), "Päivittäinen budjettisi on 50.0 euroa")
    
    def test_weekly_budget(self):
        budget = Budget()
        budget.add_income(1500, "salary")
        budget.add_monthly_expense(500, "rent")
        budget.buddget_defining()

        self.assertEqual(str(budget.monthly_budget(2)), "Viikottainen budjettisi on 250.0 euroa")