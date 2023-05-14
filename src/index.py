import customtkinter
from users_ui import NewUser, OldUser

class Start():
    """This is where the program starts by opening the first TkInter-window
    """
    def _new_user(self):
        """This function calls the NewUser class to register a new username.
        """
        new_user = NewUser()
        new_user.user_info()

    def _old_user(self):
        """This function calls the OldUser class to login user.
        """
        old_user = OldUser()
        old_user.user_info()

    def start(self):
        """This function generates the first view of the application and asks the 
            user if they have registered or not.
        """
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        root = customtkinter.CTk()
        root.title("Tervetuloa Budjettisovellukseen!")
        frame = customtkinter.CTkFrame(root)
        customtkinter.CTkLabel(frame, text="Tämä on Ohjelmistotekniikka-kurssin "
            "harjoitustyö Budjettisovellus.").grid(row=2, column=0, 
                    pady=7, padx=30, columnspan=2)
        customtkinter.CTkLabel(frame, text="Kirjauduttuasi sisään, voit luoda "
            "itsellesi budjetin sekä seurata").grid(row=3, column=0,
                    padx= 20, columnspan=2)
        customtkinter.CTkLabel(frame, text="budjettisi toteutumista menojen "
            "seurannalla.").grid(row=4, column=0, padx=5, columnspan=2)
        customtkinter.CTkLabel(frame, text="Onko sinulla jo "
            "käyttjätunnus?").grid(row=6, column=0, pady=7, columnspan=2)
        button_yes = customtkinter.CTkButton(frame, text = "Kyllä" ,
             command=self._old_user)
        button_no = customtkinter.CTkButton(frame, text = "Ei" ,
             command=self._new_user)
        button_yes.grid(row=8, column=0, pady=5)
        button_no.grid(row=8, column=1, pady=5)
        frame.grid(padx=10, pady=10)
        root.mainloop()


start = Start()
start.start()
