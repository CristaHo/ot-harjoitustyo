from datetime import timedelta
import customtkinter
from csv_file_management import CSVfiles



class BudgetList():
    def budget_table(self, budget, days, start_date, end_date):
        if start_date.month == end_date.month:
            month = start_date.month
            year = start_date.year
            csv_filename = f"{month}_{year}_budget"
            csv_search = CSVfiles()
            expenses_list = csv_search.read_file(csv_filename)
            if len(expenses_list) == 0:
                expenses_list = {0: 0}
            print(expenses_list)
            #print(start_date)

        else:
            first_month = start_date.month
            first_year = start_date.year
            second_month = end_date.month
            second_year = end_date.year
            csv_filename_one = f"{first_month}_{first_year}_budget"
            csv_filename_two = f"{second_month}_{second_year}_budget"
            csv_search = CSVfiles()
            expenses_list = {**csv_search.read_file(csv_filename_one),
                **csv_search.read_file(csv_filename_two)}
            if len(expenses_list) == 0:
                expenses_list = {0: 0}
            print(expenses_list)

        list_ui = BudgetListUi()
        list_ui.budget_table_creation(start_date, days, budget, expenses_list)

class BudgetListUi():
    def budget_table_creation(self, start_date, days, budget, expenses_list):
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        root = customtkinter.CTk()
        root.title("Budjettisi listana")
        #root.geometry('400x600')
        frame = customtkinter.CTkFrame(root)

        for i in range(0,days+1):
            for j in range(1,5):
                if i == 0:
                    if j == 1:
                        customtkinter.CTkLabel(frame,
                            text="Päivä").grid(row=i,
                                column=j, padx=5, pady=5)
                    if j == 2:
                        customtkinter.CTkLabel(frame,
                            text="Summa").grid(row=i,
                                column=j, padx=5, pady=5)
                    if j == 3:
                        customtkinter.CTkLabel(frame,
                            text="Mihin").grid(row=i,
                                column=j, padx=5, pady=5)
                    if j == 4:
                        customtkinter.CTkLabel(frame,
                            text="Jäljellä").grid(row=i,
                                column=j, padx=5, pady=5)
                elif str(start_date) in expenses_list:
                    if j == 1:
                        customtkinter.CTkLabel(frame,
                            text=start_date).grid(row=i,
                                column=j)
                    if j == 2:
                        customtkinter.CTkLabel(frame,
                            text=expenses_list[str(start_date)][0]).grid(row=i,
                                                                        column=j)
                    if j == 3:
                        customtkinter.CTkLabel(frame,
                            text=expenses_list[str(start_date)][1]).grid(row=i,
                                                                        column=j)
                    if j == 4:
                        label4 = customtkinter.CTkLabel(frame,
                            text=f"{(budget-float(expenses_list[str(start_date)][0])):.2f}")
                        label4.grid(row=i, column=j)
                else:
                    if j == 1:
                        customtkinter.CTkLabel(frame, text=start_date).grid(row=i, column=j)
                    if j == 2:
                        customtkinter.CTkLabel(frame, text="0").grid(row=i, column=j)
                    if j == 3:
                        customtkinter.CTkLabel(frame, text="").grid(row=i, column=j)
                    if j == 4:
                        customtkinter.CTkLabel(frame, text=f"{budget:.2f}").grid(row=i, column=j)

            if i != 0:
                start_date += timedelta(days=1)
        frame.grid(pady=10, padx=10)
        root.mainloop()
 


