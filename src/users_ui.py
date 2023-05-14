from tkinter import messagebox, constants
import customtkinter
from CTkMessagebox import CTkMessagebox
from budget_ui import BudgetUi
from database_connection import get_database_connection
from users import UserRepository

class NewUser():
    """This class is the user interface of registering a new user.
    """
    def user_info(self):
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        user_repository = UserRepository(get_database_connection())
        new_user = customtkinter.CTk()
        new_user_frame = customtkinter.CTkFrame(new_user)
        #new_user.geometry("350x100")
        new_user.title("Rekisteröidy")
        def create():
            user_repository.create_user(new_username.get(), new_password.get())
            CTkMessagebox(title="Rekisteröityminen onnistui",
                message="Uusi käyttäjä luotu. \n Voit nyt kirjautua sisään!", icon="check")
            new_user.destroy()
        customtkinter.CTkLabel(new_user_frame, text='Luo käyttäjätunnus',
            font=customtkinter.CTkFont(size=14)).grid(row=0, padx=5, pady=5)
        customtkinter.CTkLabel(new_user_frame, text='Luo salasana',
            font=customtkinter.CTkFont(size=14)).grid(row=1, padx=5, pady=5)
        new_username = customtkinter.CTkEntry(new_user_frame)
        new_password = customtkinter.CTkEntry(new_user_frame)
        new_username.grid(row=0, column=1, padx=5, pady=5)
        new_password.grid(row=1, column=1, padx=5, pady=5)
        #new_username = input("Valitse käyttäjätunnus: ")
        #new_password = input("Valitse salasana: ")
        btn = customtkinter.CTkButton(new_user_frame, text = "Rekisteröidy",
            font=customtkinter.CTkFont(size=14),
                command=create)
        btn.grid(column=0, row=2, columnspan=2, padx=5, pady=5, sticky=constants.EW)
        new_user_frame.grid(padx=10, pady=10)
        new_user.mainloop()

class OldUser():
    """This class is the user interface of logging in by old user.
    """
    def user_info(self):
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        user_repository = UserRepository(get_database_connection())
        old_user = customtkinter.CTk()
        old_user_frame = customtkinter.CTkFrame(old_user)
        #old_user.geometry("350x100")
        old_user.title("Kirjaudu")
        def check():
            if user_repository.find_user(username.get(), password.get()):
                CTkMessagebox(title="Kirjautuminen onnistui",
                    message=f"Olet nyt kirjautunut tunnuksella {username.get()}", icon="check")
                old_user.destroy()
                to_budget = BudgetUi()
                to_budget.start_ui()
            else:
                messagebox.showerror("Virhe", "Käyttäjätunnusta ei löydy")
            #messagebox.showinfo("showinfo", "Uusi käyttäjä luotu. Voit nyt kirjautua sisään!")
            #new_user.destroy()
        customtkinter.CTkLabel(old_user_frame, text='Käyttäjätunnus',
            font=customtkinter.CTkFont(size=14)).grid(row=0, padx=5, pady=5)
        customtkinter.CTkLabel(old_user_frame, text='Salsana',
            font=customtkinter.CTkFont(size=14)).grid(row=1, padx=5, pady=5)
        username = customtkinter.CTkEntry(old_user_frame)
        password = customtkinter.CTkEntry(old_user_frame)
        username.grid(row=0, column=1, padx=5, pady=5)
        password.grid(row=1, column=1, padx=5, pady=5)
        #new_username = input("Valitse käyttäjätunnus: ")
        #new_password = input("Valitse salasana: ")
        btn = customtkinter.CTkButton(old_user_frame, text = "Kirjaudu",
            font=customtkinter.CTkFont(size=14),
                command=check)
        btn.grid(column=0, row=2, padx=5, pady=5, columnspan=2, sticky=constants.EW)
        old_user_frame.grid(padx=10, pady=10)
        old_user.mainloop()
