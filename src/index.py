from tkinter import ttk, Tk
from users import NewUser, OldUser

class Start():
    root = Tk()

    def new_user(self):
        new_user = NewUser()
        new_user.user_info()

    def old_user(self):
        old_user = OldUser()
        old_user.user_info()

    def start(self):
        self.root.title("Tervetuloa Budjettisovellukseen!")
        self.root.geometry('500x250')
        #menu = Menu(self.root)
        #item = Menu(menu)
        #item.add_command(label='Uusi käyttäjä', command=self.new_user)
        #item.add_command(label="Kirjaudu", command=self.old_user)
        #menu.add_cascade(label='Käyttäjä', menu=item)
        #self.root.config(menu=menu)
        ttk.Label(self.root, text="Tämä on Ohjelmistotekniikka-kurssin "
            "harjoitustyö Budjettisovellus.").grid(row=2, column=0, 
                    pady=7, padx=30, columnspan=2)
        ttk.Label(self.root, text="Kirjauduttuasi sisään, voit luoda "
            "itsellesi budjetin sekä seurata").grid(row=3, column=0,
                    padx= 20, columnspan=2)
        ttk.Label(self.root, text="budjettisi toteutumista menojen "
            "seurannalla.").grid(row=4, column=0, padx=5, columnspan=2)
        ttk.Label(self.root, text="Onko sinulla jo "
            "käyttjätunnus?").grid(row=6, column=0, pady=7, columnspan=2)
        button_yes = ttk.Button(self.root, text = "Kyllä" ,
             command=self.old_user)
        button_no = ttk.Button(self.root, text = "Ei" ,
             command=self.new_user)
        button_yes.grid(row=8, column=0)
        button_no.grid(row=8, column=1)
        self.root.mainloop()


start = Start()
start.start()
