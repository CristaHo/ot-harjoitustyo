from csv_file_management import CSVfiles

class Budget():
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
    def __init__(self, the_date, amount, where):
        self.the_date = the_date
        self.amount = amount
        self.where = where

    def add_to_budget(self):
        month = (self.the_date).month
        year = (self.the_date).year
        csv_filename = f"{month}_{year}_budget"
        add_to_csv = CSVfiles()
        add_to_csv.write_to_file(csv_filename, self.the_date, self.amount, self.where)


#budjetti = BudgetUi()
#budjetti.start_ui()
