from csv_file_management import CSVfiles

class Budget():
    """This class creates the original budget.
    """
    def __init__(self, income, expense, days):
        self.income = income
        self.expenses = expense
        self.budgetti = None
        self.budget_days = days

    def create_budget(self):
        new_income = float(self.income)
        new_expenses = float(self.expenses)
        self.budgetti = new_income - new_expenses
        return self.budgetti

class Expenses():
    """This class sends a new expense to be saved in the correct
        csv-file.
    """
    def __init__(self, the_date, amount, where):
        self.the_date = the_date
        self.amount = amount
        self.where = where

    def add_to_budget(self):
        """This function sends the expense to csv_file_management.py 
            to be saved in the correct csv-file.
        """
        month = (self.the_date).month
        year = (self.the_date).year
        csv_filename = f"{month}_{year}_budget"
        add_to_csv = CSVfiles()
        add_to_csv.write_to_file(csv_filename, self.the_date, self.amount, self.where)


#budjetti = BudgetUi()
#budjetti.start_ui()
