from tkinter import Tk, ttk, constants
from tkcalendar import DateEntry
from show_budget import BudgetList
from budget import Budget, Expenses

class BudgetUi:
    """The interface for creating a budget.
    """
    def __init__(self):
        self.calendar_expense = None
        self.amount = 0
        self.expense_where = None
        self.budget = None
        self.start_date = None
        self.end_date = None
        self.number_of_days = 0
        self.income = 0
        self.expenses = 0
        self.root = None
        self.calendar_start = None
        self.calendar_end = None

    def add_expense(self):
        """This function allows user to add new expenses to budget.
        """
        ttk.Label(self.root, text="Päivämäärä").grid()
        self.calendar_expense=DateEntry(self.root,selectmode='day')
        self.calendar_expense.grid()
        ttk.Label(self.root, text="Käytetty summa").grid()
        self.amount = ttk.Entry(self.root)
        self.amount.grid()
        ttk.Label(self.root, text="Mihin käytetty").grid()
        self.expense_where = ttk.Entry(self.root)
        self.expense_where.grid()
        ttk.Button(self.root, text="Lisää budjettiin",
            command=self.add_expense_next_step).grid()

    def add_expense_next_step(self):
        expense_date = self.calendar_expense.get_date()
        expense_amount = self.amount.get()
        expense_where = self.expense_where.get()
        expense = Expenses(expense_date, expense_amount, expense_where)
        expense.add_to_budget()

    def show_budget(self):
        self.budget = Budget(self.income.get(), self.expenses.get(), self.number_of_days)
        budget_now = ttk.Label(self.root, text=f"Budjettisi on "
        f"{self.budget.create_budget()} euroa.")
        budget_now.grid(row=8)
        self.show_different_budgets()

    def show_weekly_budget(self):
        weekly_budget = self.budget.create_budget()/4
        ttk.Label(self.root, text=f"Viikkobudjettisi on "
        f"{weekly_budget:.2f} euroa").grid(row=14, column=1)

    def show_budget_list(self):
        daily_budget = self.budget.create_budget()/self.number_of_days
        budgetlist = BudgetList()
        budgetlist.budget_table(daily_budget, self.number_of_days, self.start_date, self.end_date)

    def create_dates(self):
        self.start_date = self.calendar_start.get_date()
        self.end_date = self.calendar_end.get_date()
        self.number_of_days = ((self.end_date - self.start_date).days)+1
        ttk.Label(self.root, text=f"Budjetti luodaan aikavälille {self.start_date} - "
            f"{self.end_date}, eli {self.number_of_days} päiväksi.").grid(row=5, columnspan=3)
        self.add_monthly_income_expense()

    def add_monthly_income_expense(self):
        ttk.Label(self.root, text='Syötä kuukausitulosi').grid(row=6)
        ttk.Label(self.root, text='Syötä kuukausimenosi').grid(row=7)
        self.income = ttk.Entry(self.root)
        self.expenses = ttk.Entry(self.root)
        self.expenses.grid(row=7, column=1)
        self.income.grid(row=6, column=1)
        button = ttk.Button(self.root, text = "Luo budjetti" ,
            command=self.show_budget)
        button.grid(column=1, row=8)

    def start_ui(self):
        """Start window for creating budget.
        """

        self.root = Tk()
        self.root.title("Tervetuloa Budjettisovellukseen")
        self.root.geometry('700x500')

        ttk.Label(self.root, text="Nyt voit luoda budjetin itsellesi").grid(row=0,
            column=0, pady=15, padx=20, columnspan=2)
        ttk.Label(self.root, text="Mille ajalle haluat laskea budjetin?").grid(row=1,
            column=0, pady=5, padx=20, columnspan=2)
        ttk.Label(self.root, text="Alkaen:").grid(row=2, column=0, padx=20)
        self.calendar_start=DateEntry(self.root,selectmode='day')
        self.calendar_start.grid(row=2,column=1, sticky=constants.W)
        ttk.Label(self.root, text="Päättyen:").grid(row=3, column=0, padx=20)
        self.calendar_end=DateEntry(self.root,selectmode='day')
        self.calendar_end.grid(row=3,column=1, sticky=constants.W)
        choose_dates=ttk.Button(self.root,text='Valitse', command=self.create_dates)
        choose_dates.grid(row=4, column=1)
        self.root.mainloop()

    def show_daily_budget(self):
        daily = self.budget.create_budget()/self.number_of_days
        ttk.Label(self.root, text=f"Päiväbudjettisi on {daily:.2f} euroa").grid(row=13, column=1)

    def show_different_budgets(self):

        ttk.Button(self.root, text="Näytä päiväbudjetti",
            command=self.show_daily_budget).grid(row=9, column=1)
        ttk.Button(self.root, text="Näytä viikkobudjetti",
            command=self.show_weekly_budget).grid(row=10, column=1)
        ttk.Button(self.root, text="Näytä budjettisi taulukkona",
            command=self.show_budget_list).grid(row=11, column=1)
        ttk.Button(self.root, text="Lisää meno budjettiin",
            command=self.add_expense).grid(row=12, column=1)
