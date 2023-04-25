from tkinter import ttk, messagebox, Tk, constants
import sqlite3
from budget import BudgetUi
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, username, password):
        new_user = (username, password)
        self._connection.row_factory = sqlite3.Row
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?);", new_user)
        self._connection.commit()

    def find_user(self, username, password):
        #find = (username, password)
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT username, password FROM users "
            f"WHERE username='{username}' AND password='{password}';")
        row = cursor.fetchone()
        #if row:
         #   print(row[0], row[1])
        #else:
         #   print("Käyttäjää ei löytynyt")
        return row

class NewUser():
    def user_info(self):
        user_repository = UserRepository(get_database_connection())
        new_user = Tk()
        new_user.geometry("350x100")
        new_user.title("Rekisteröidy")
        def create():
            user_repository.create_user(new_username.get(), new_password.get())
            messagebox.showinfo("Rekisteröityminen onnistui",
            "Uusi käyttäjä luotu. \n Voit nyt kirjautua sisään!")
            new_user.destroy()
        ttk.Label(new_user, text='Luo käyttäjätunnus').grid(row=0, padx=5, pady=5)
        ttk.Label(new_user, text='Luo salasana').grid(row=1, padx=5, pady=5)
        new_username = ttk.Entry(new_user)
        new_password = ttk.Entry(new_user)
        new_username.grid(row=0, column=1, padx=5, pady=5)
        new_password.grid(row=1, column=1, padx=5, pady=5)
        #new_username = input("Valitse käyttäjätunnus: ")
        #new_password = input("Valitse salasana: ")
        btn = ttk.Button(new_user, text = "Rekisteröidy" ,
                command=create)
        btn.grid(column=0, row=2, columnspan=2, padx=5, pady=5, sticky=constants.EW)
        new_user.mainloop()

class OldUser():
    def user_info(self):
        user_repository = UserRepository(get_database_connection())
        old_user = Tk()
        old_user.geometry("350x100")
        old_user.title("Kirjaudu")
        def check():
            if user_repository.find_user(username.get(), password.get()):
                messagebox.showinfo("Kirjautuminen onnistui",
                f"Olet nyt kirjautunut tunnuksella {username.get()}")
                old_user.destroy()
                to_budget = BudgetUi()
                to_budget.start_ui()
            else:
                messagebox.showerror("Virhe", "Käyttäjätunnusta ei löydy")
            #messagebox.showinfo("showinfo", "Uusi käyttäjä luotu. Voit nyt kirjautua sisään!")
            #new_user.destroy()
        ttk.Label(old_user, text='Käyttäjätunnus').grid(row=0, padx=5, pady=5)
        ttk.Label(old_user, text='Salsana').grid(row=1, padx=5, pady=5)
        username = ttk.Entry(old_user)
        password = ttk.Entry(old_user)
        username.grid(row=0, column=1, padx=5, pady=5)
        password.grid(row=1, column=1, padx=5, pady=5)
        #new_username = input("Valitse käyttäjätunnus: ")
        #new_password = input("Valitse salasana: ")
        btn = ttk.Button(old_user, text = "Kirjaudu" ,
             command=check)
        btn.grid(column=0, row=2, padx=5, pady=5, columnspan=2, sticky=constants.EW)
        old_user.mainloop()
#test = UserRepository(get_database_connection())
#test.find_all()
#print(test.find_user("a", "b")[0], test.find_user("a", "b")[1])
#users = NewUser()

#users.user_info()

#users = OldUser()
#users.user_info()
