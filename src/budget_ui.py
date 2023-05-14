from tkinter import constants
import customtkinter
from tkcalendar import DateEntry
from CTkMessagebox import CTkMessagebox
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

    def indicate_frame(self, frame):
        self.delete_frame()
        frame()

    def _delete_frame(self):
        """This function deletes current and previous frames.
        """
        for frame in self.root.winfo_children():
            frame.destroy()

    def _add_expense(self):
        """This function allows user to add new expenses to budget.
        """
        self.add_expense_window = customtkinter.CTk()
        self.add_expense_window.title("Lisää meno")
        self.expense_frame = customtkinter.CTkFrame(self.add_expense_window)
        customtkinter.CTkLabel(self.expense_frame,
                text="Päivämäärä").grid(pady=5, padx=5, sticky=constants.W)
        self.calendar_expense=DateEntry(self.expense_frame,selectmode='day')
        self.calendar_expense.grid(padx=5, pady=3, sticky=constants.W)
        customtkinter.CTkLabel(self.expense_frame,
                text="Käytetty summa").grid(pady=5, padx=5, sticky=constants.W)
        self.amount = customtkinter.CTkEntry(self.expense_frame)
        self.amount.grid(padx=5, pady=3, sticky=constants.W)
        customtkinter.CTkLabel(self.expense_frame,
                text="Mihin käytetty").grid(pady=5, padx=5, sticky=constants.W)
        self.expense_where = customtkinter.CTkEntry(self.expense_frame)
        self.expense_where.grid(pady=5, padx=5, sticky=constants.W)
        customtkinter.CTkButton(self.expense_frame, text="Lisää budjettiin",
            command=self._add_expense_next_step).grid(pady=5, padx=10, sticky=constants.EW)
        self.expense_frame.grid(padx=20, pady=10)
        self.add_expense_window.mainloop()

    def _add_expense_next_step(self):
        """This function gathers info to create a new Expense-object
        """
        expense_date = self.calendar_expense.get_date()
        expense_amount = self.amount.get()
        expense_where = self.expense_where.get()
        expense = Expenses(expense_date, expense_amount, expense_where)
        expense.add_to_budget()
        self.add_expense_window.destroy()
        CTkMessagebox(title="Lisäys onnistui!",
                    message="Meno lisätty budjettiin", icon="check")



    def _show_budget(self):
        """This function shows the new budget to the user
        """

        self.budget = Budget(self.income.get(), self.expenses.get(), self.number_of_days)
        self._delete_frame()
        self.budget_frame = customtkinter.CTkFrame(self.root)
        #self.budget_frame_right = ttk.Frame(self.root)
        budget_now = customtkinter.CTkLabel(self.budget_frame, text="Budjettisi on :")
        budget_now1 = customtkinter.CTkLabel(self.budget_frame,
                text=f"{self.budget.create_budget():.2f} euroa.")
        budget_now.grid(column=0, row=0, padx=5, pady=10)
        budget_now1.grid(column=1, row=0, padx=5, pady=10)
        self._show_different_budgets()
        self.budget_frame.grid(padx=10, pady=10)
        #self.budget_frame_right.grid(padx=10, pady=10, column=1)

    def _show_different_budgets(self):
        """This function shows buttons for different budget-views
        """

        customtkinter.CTkButton(self.budget_frame, text="Näytä päiväbudjetti",
            command=self._show_daily_budget).grid(row=1,
                column=0, pady=5, padx=5, sticky=constants.W)
        customtkinter.CTkButton(self.budget_frame, text="Näytä viikkobudjetti",
            command=self._show_weekly_budget).grid(row=2,
                column=0, pady=5, padx=5, sticky=constants.W)
        customtkinter.CTkButton(self.budget_frame, text="Näytä budjettisi taulukkona",
            command=self._show_budget_list).grid(row=3,
                column=0, pady=5, padx=5, sticky=constants.W)
        customtkinter.CTkButton(self.budget_frame, text="Lisää meno budjettiin",
            command=self._add_expense).grid(row=4,
                column=0, pady=5, padx= 5, sticky=constants.W)

    def _show_weekly_budget(self):
        """This function divides the budget to get a weekly budget.
        """
        weekly_budget = self.budget.create_budget()/4
        customtkinter.CTkLabel(self.budget_frame, text=f"Viikkobudjettisi on "
        f"{weekly_budget:.2f} euroa").grid(row=2, column=1)

    def _show_budget_list(self):
        """This function calls for the BudgetList class to show the user the budget as a list
        """
        daily_budget = self.budget.create_budget()/self.number_of_days
        budgetlist = BudgetList()
        budgetlist.budget_table(daily_budget, self.number_of_days, self.start_date, self.end_date)

    def _create_dates(self):
        """This function subtracts the chosen dates from each other to 
            get the number of days the budget is going to divided by.
        """
        self.start_date = self.calendar_start.get_date()
        self.end_date = self.calendar_end.get_date()
        self.number_of_days = ((self.end_date - self.start_date).days)+1
        self._delete_frame()
        self.income_frame = customtkinter.CTkFrame(self.root)
        customtkinter.CTkLabel(self.income_frame,
            text=f"Budjetti luodaan aikavälille {self.start_date} - "
                f"{self.end_date}, eli {self.number_of_days} päiväksi.").grid(pady=10,
                        padx=5, columnspan=2)
        self._add_monthly_income_expense()

    def _add_monthly_income_expense(self):
        """This function is the interface for the user in which the 
            user can add their monthly income and expenses
        """
        customtkinter.CTkLabel(self.income_frame,
            text='Syötä kuukausitulosi').grid(column=0, row=1, pady=3)
        customtkinter.CTkLabel(self.income_frame,
            text='Syötä kuukausimenosi').grid(column=0, row=2, pady=3)
        self.income = customtkinter.CTkEntry(self.income_frame)
        self.expenses = customtkinter.CTkEntry(self.income_frame)
        self.expenses.grid(column=1, row=2, sticky=constants.W)
        self.income.grid(column=1, row=1, sticky=constants.W)
        button = customtkinter.CTkButton(self.income_frame, text = "Luo budjetti" ,
            command=self._show_budget)
        button.grid(column=0, row=3, columnspan=2, sticky=constants.EW, padx=10, pady=5)
        self.income_frame.grid(pady=20, padx=20)

    def _dates(self):
        """This function is the interface for asking the user of the days which 
            the user want to include in the current budget.
        """
        dates_frame = customtkinter.CTkFrame(master=self.root)
        customtkinter.CTkLabel(dates_frame, text="Nyt voit luoda budjetin itsellesi").grid(row=0,
            column=1, pady=15, padx=20, columnspan=2)
        customtkinter.CTkLabel(dates_frame,
            text="Mille ajalle haluat laskea budjetin?\n").grid(row=1,
                column=1, pady=5, padx=20, columnspan=2)
        customtkinter.CTkLabel(dates_frame, text="Alkaen:").grid(row=2, column=1, padx=20, pady=3)
        self.calendar_start=DateEntry(dates_frame,selectmode='day')
        self.calendar_start.grid(row=2,column=2, sticky=constants.W, pady=3)
        customtkinter.CTkLabel(dates_frame, text="Päättyen:").grid(row=3, column=1, padx=20, pady=3)
        self.calendar_end=DateEntry(dates_frame,selectmode='day')
        self.calendar_end.grid(row=3,column=2, sticky=constants.W, pady=3)
        choose_dates=customtkinter.CTkButton(dates_frame,text='Valitse', command=self._create_dates)
        choose_dates.grid(row=4, column=1, columnspan=2, pady=10, padx=5, sticky=constants.EW)
        dates_frame.grid(pady=10, padx=10)

    def start_ui(self):
        """Start window for creating budget.
        """
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        self.root = customtkinter.CTk()
        self.root.title("Tervetuloa Budjettisovellukseen")
        #self.root.geometry('400x400')
        self._dates()

        self.root.mainloop()

    def _show_daily_budget(self):
        """Shows daily budget to user
        """
        daily = self.budget.create_budget()/self.number_of_days
        customtkinter.CTkLabel(self.budget_frame,
            text=f"Päiväbudjettisi on {daily:.2f} euroa").grid(row=1, column=1)




