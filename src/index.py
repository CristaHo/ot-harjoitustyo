from tkinter import ttk, Tk, Menu
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
        self.root.geometry('700x700')
        menu = Menu(self.root)
        item = Menu(menu)
        item.add_command(label='Uusi käyttäjä', command=self.new_user)
        item.add_command(label="Kirjaudu", command=self.old_user)
        menu.add_cascade(label='Käyttäjä', menu=item)
        self.root.config(menu=menu)
        title = ttk.Label(self.root, text="Tervetuloa budjettisovellukseen, painamalla käyttäjä-"
                                    "nappia voit luoda uuden käyttäjän tai kirjautua sisään")
        title.grid()
        user_question = ttk.Label(self.root, text="Onko sinulla jo käyttjätunnus?")
        user_question.grid()
        button_yes = ttk.Button(self.root, text = "Kyllä" ,
             command=self.old_user)
        button_no = ttk.Button(self.root, text = "Ei" ,
             command=self.new_user)
        button_yes.grid()
        button_no.grid()
        self.root.mainloop()


start = Start()
start.start()
