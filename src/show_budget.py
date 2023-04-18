from tkinter import ttk, Tk

class BudgetList():
    def budget_table(self, budget):
        root = Tk()
        root.geometry('400x600')

#lista = {1: [20, "ruokakauppa"], 5: (10, "apteekki")}

        for i in range(0,31):
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
               # elif i in lista.keys():
                #    if j == 1:
                 #       Label(root, text=i).grid(row=i, column=j)
                  #  if j == 2:
                   #     Label(root, text=lista[i][0]).grid(row=i, column=j)
                   # if j == 3:
                     #   Label(root, text=lista[i][1]).grid(row=i, column=j)
                   # if j == 4:
                    #    Label(root, text=f"{50-lista[i][0]}").grid(row=i, column=j)
                else:
                    if j == 1:
                        ttk.Label(root, text=i).grid(row=i, column=j)
                    if j == 2:
                        ttk.Label(root, text="0").grid(row=i, column=j)
                    if j == 3:
                        ttk.Label(root, text="").grid(row=i, column=j)
                    if j == 4:
                        ttk.Label(root, text=f"{budget:.2f}").grid(row=i, column=j)
        root.mainloop()

#budgetlist = BudgetList()
#budgetlist.budget_table(20)
