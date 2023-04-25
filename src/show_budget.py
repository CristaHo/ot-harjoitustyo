from tkinter import ttk, Tk
from datetime import timedelta
from csv_file_management import CSVfiles

class BudgetList():
    def budget_table(self, budget, days, start_date, end_date):
        root = Tk()
        root.geometry('400x600')

        if start_date.month == end_date.month:
            month = start_date.month
            year = start_date.year
            csv_filename = f"{month}_{year}_budget"
            csv_search = CSVfiles()
            expenses_list = csv_search.read_file(csv_filename)
            if not expenses_list:
                expenses_list = {0: 0}
            #print(expenses_list)
            #print(start_date)

        for i in range(0,days+1):
            for j in range(1,5):
                if i == 0:
                    if j == 1:
                        ttk.Label(root, text="Päivä").grid(row=i, column=j)
                    if j == 2:
                        ttk.Label(root, text="Summa").grid(row=i, column=j)
                    if j == 3:
                        ttk.Label(root, text="Mihin").grid(row=i, column=j)
                    if j == 4:
                        ttk.Label(root, text="Jäljellä").grid(row=i, column=j)
                elif str(start_date) in expenses_list:
                    if j == 1:
                        ttk.Label(root, text=start_date).grid(row=i, column=j)
                    if j == 2:
                        ttk.Label(root, text=expenses_list[str(start_date)][0]).grid(row=i,
                                                                                column=j)
                    if j == 3:
                        ttk.Label(root, text=expenses_list[str(start_date)][1]).grid(row=i,
                                                                                column=j)
                    if j == 4:
                        label4 = ttk.Label(root, text=f"{(budget-float(expenses_list[str(start_date)][0])):.2f}")
                        label4.grid(row=i, column=j)
                else:
                    if j == 1:
                        ttk.Label(root, text=start_date).grid(row=i, column=j)
                    if j == 2:
                        ttk.Label(root, text="0").grid(row=i, column=j)
                    if j == 3:
                        ttk.Label(root, text="").grid(row=i, column=j)
                    if j == 4:
                        ttk.Label(root, text=f"{budget:.2f}").grid(row=i, column=j)

            if i != 0:
                start_date += timedelta(days=1)
        root.mainloop()

#budgetlist = BudgetList()
#budgetlist.budget_table(20, 31, datetime(2023, 4, 1), datetime(2023, 4, 30))
