from tkinter import Tk, ttk
#from tkcalendar import DateEntry
from show_budget import BudgetList

class Budget():
    def __init__(self, income, expense):
        self.income = income
        self.expenses = expense
        self.budgetti = None

    def create_budget(self):
        new_income = int(self.income)
        new_expenses = int(self.expenses)
        self.budgetti = new_income - new_expenses
        return self.budgetti

class BudgetUi:
    def show_budget(self):
        self.budget = Budget(self.income.get(), self.expenses.get())
        budget_now = ttk.Label(self.root, text=f"Budjettisi on "
        f"{self.budget.create_budget()} euroa.")
        budget_now.grid(row=6, column=1)
        self.show_different_budgets()

    def show_weekly_budget(self):
        weekly_budget = self.budget.create_budget()/4
        ttk.Label(self.root, text=f"Viikkobudjettisi on "
        f"{weekly_budget:.2f} euroa").grid(row=13, column=1)

    def show_budget_list(self):
        daily_budget = self.budget.create_budget()/30
        budgetlist = BudgetList()
        budgetlist.budget_table(daily_budget)

    def start_ui(self):

        self.root = Tk()
        self.root.title("Tervetuloa Budjettisovellukseen")
        self.root.geometry('600x500')

        ttk.Label(self.root, text="Nyt voit luoda budjetin itsellesi").grid(row=0, column=1)
        #Label(self.root, text="Mille ajalle haluat laskea budjetin?").grid()
        #calendar_start=DateEntry(self.root,selectmode='day').grid(row=1,column=1,padx=20,pady=30)
        #calendar_end=DateEntry(self.root,selectmode='day').grid(row=1,column=2,padx=20,pady=30)
        #b2=Button(self.root,text='Valitse', command=lambda:create_dates).grid(row=1, column=3)
        ttk.Label(self.root, text='Syötä kuukausitulosi').grid(row=3)
        ttk.Label(self.root, text='Syötä kuukausimenosi').grid(row=4)
        self.income = ttk.Entry(self.root)
        self.expenses = ttk.Entry(self.root)
        self.expenses.grid(row=4, column=1)
        self.income.grid(row=3, column=1)
        button = ttk.Button(self.root, text = "Luo budjetti" ,
            command=self.show_budget)
        button.grid(column=1, row=5)
        self.root.mainloop()

    def show_daily_budget(self):
        daily = self.budget.create_budget()/30
        ttk.Label(self.root, text=f"Päiväbudjettisi on {daily:.2f} euroa").grid(row=12, column=1)

    def show_different_budgets(self):

        ttk.Button(self.root, text="Näytä päiväbudjetti",
            command=self.show_daily_budget).grid(row=8, column=1)
        ttk.Button(self.root, text="Näytä viikkobudjetti",
            command=self.show_weekly_budget).grid(row=9, column=1)
        ttk.Button(self.root, text="Näytä budjettisi taulukkona",
            command=self.show_budget_list).grid(row=10, column=1)

#budjetti = BudgetUi()
#budjetti.start_ui()
