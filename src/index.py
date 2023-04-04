
def main():
    start = Start()
    start.start_budget()

class Start:
    def start_budget(self):
        print("Tervetuloa budjettilaskuriin")
        print("Syötä alle kuukausittaiset tulosi ja menosi, jotta saat tietää budjettisi tulevalle kuukaudelle.")
        add_income_amount = int(input("Syötä kuukausitulosi: "))
        add_income_name = input("Mikä on tulon lähde: ") 
        self.budget = Budget()
        self.budget.add_income(add_income_amount, add_income_name)
        add_monthly_expenses_amount = int(input("Lisää kuukausittainen meno (kokonaisluku): "))
        add_monthly_expenses_name = input("Menon nimi (esim. vuokra, lasku): ")
        self.budget.add_monthly_expense(add_monthly_expenses_amount, add_monthly_expenses_name)
        add_more = input("Haluatko lisätä lisää kuukausittaisia menoja? (k/e)")
        while add_more == "k":
            add_monthly_expenses_amount = int(input("Lisää kuukausittainen meno: "))
            add_monthly_expenses_name = input("Menon nimi (esim. vuokra, lasku): ")
            self.budget.add_monthly_expense(add_monthly_expenses_amount, add_monthly_expenses_name)
            add_more = input("Haluatko lisätä lisää kuukausittaisia menoja? (k/e)")
        
        print(self.budget)
        self.choices()
    
    def choices(self):

        print("Mitä seuraavaksi?")
        print("1. näytä viikkobudjetti")
        print("2. näytä päiväbudjetti")
        print("3. näytä budjetin kuukausiseuranta")
        print("4. lisää meno kuukausiseurantaan")
        #print("5. anna neuvoja budjetin suhteen")
        print("6. poistu sovelluksesta")
        self.next = int(input("Valitse numero: "))
        self.numbers()

    def numbers(self):

        if self.next == 1:
            print(self.budget.monthly_budget(2))
            self.choices()

        if self.next == 2:
            print(self.budget.monthly_budget(1))
            self.choices()
        
        if self.next == 3:
            self.budget.show_budget1()
            self.choices()

        if self.next == 4:
            add_expense_day = int(input("Miltä kuukauden päivältä (1-30) meno on: "))
            add_expense_amount = int(input("Lisää menon määrä: "))
            add_expense_name = input("Mikä on menon lähde (esim. lasku tai kauppa): ")
            self.budget.add_expense(add_expense_amount, add_expense_name, add_expense_day)
            self.choices()

        if self.next == 6:
            exit()

class Budget:
    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.monthly_expenses = {}

    
    def add_income(self, amount, name):
        self.income[name] = amount
    
    def add_monthly_expense(self, amount, name):
        self.monthly_expenses[name] = amount
    
    def add_expense(self, amount, name, day):
        self.expenses[day] = [amount, name]
        
    
    def buddget_defining(self):
        self.budget = sum(self.income.values()) - sum(self.monthly_expenses.values())
        return self.budget
    
    def monthly_budget(self, choice):
        self.daily = self.budget/30
        self.weekly = self.budget/4

        if choice == 1:
            return (f"Päivittäinen budjettisi on {self.daily:.2f} euroa")
        
        else:
            return (f"Viikottainen budjettisi on {self.weekly:.2f} euroa")
    
    def show_budget1(self):
        for day in range(1, 31):
            if day in self.expenses.keys():
                print(f"Day {day} | {self.expenses[day][0]} | {((self.budget/30)-self.expenses[day][0]):.2f} |")
            else:
                print(f"Day {day} | 0 | {(self.buddget_defining()/30):.2f}|")
    
    def __str__(self):
        return (f"Kuukauden budjettisi on {self.buddget_defining():.2f} euroa")





if __name__=="__main__":
    main()
    #budjetti = Budget()
#budjetti.add_expense(500, "vuokra", 1)
#budjetti.add_expense(100, "lasku", 10)
#budjetti.add_expense(50, "toinen lasku", 20)
    #budjetti.show_budget1()

