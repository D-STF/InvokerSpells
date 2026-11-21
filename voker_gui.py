from tkinter import *
from tkinter import ttk
import functools

"""блок разрешения окна"""
def screen_size(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        screen_info = Tk()
        root.geometry(f"{screen_info.winfo_screenwidth()}x{screen_info.winfo_screenheight()}")
        screen_info.destroy()
        return func(*args, **kwargs)
    return wrapper

class Window():

    @screen_size
    def __init__(self, root):

        root.title("Invoker Game")#название окна
        #root.iconbitmap("") иконка окна
        root.config(background="#696969")#цвет окна
        self.menu()

    def menu(self):

        """текст"""
        choise = Label(root, text="ВЫБЕРИТЕ РЕЖИМ", font=("Times New Roman", 30), bg="#696969")
        choise.grid(row=2, column=9)
        info_new = Label(root, text="9 способностей", font=("Times New Roman", 17), bg="#696969")
        info_new.grid(row=9, column=8)
        info_old = Label(root, text="27 способностей", font=("Times New Roman", 17), bg="#696969")
        info_old.grid(row=9, column=10)

        """выбор режима"""
        for x in range (20):
            root.rowconfigure(x, weight=1)
            root.columnconfigure(x, weight=1)
        dota_1 = Button(root, text="Old Invoker", bg="#A9A9A9", padx=20, pady=30, font=("segoe UI", 16, "bold"), command=self.old_voker_game)
        dota_1.grid(row=8, column=10)
        dota_2 = Button(root, text="Invoker", bg="#A9A9A9", padx=25, pady=30, font=("segoe UI", 16, "bold"),command=self.new_voker_game)
        dota_2.grid(row=8, column=8)
        self.widgets = [choise,
                        info_new,
                        info_old,
                        dota_1,
                        dota_2]
        self.new_widgets=[]
        self.old_widgets=[]


    def old_voker_game(self):
        [x.destroy() for x in self.widgets]
        spher_1 = Label(root, bg="black", padx=40, pady=30)
        spher_1.grid(row=15, column=7)
        spher_2 = Label(root, bg="black", padx=40, pady=30)
        spher_2.grid(row=15, column=9)
        spher_3 = Label(root, bg="black", padx=40, pady=30)
        spher_3.grid(row=15, column=11)

        spell_1 = Label(root, bg="black", padx=40, pady=30)
        spell_1.grid(row=13, column=5)
        spell_2 = Label(root, bg="black", padx=40, pady=30)
        spell_2.grid(row=13, column=7)
        spell_3 = Label(root, bg="black", padx=40, pady=30)
        spell_3.grid(row=13, column=9)
        spell_4 = Label(root, bg="black", padx=40, pady=30)
        spell_4.grid(row=13, column=11)
        spell_5 = Label(root, bg="black", padx=40, pady=30)
        spell_5.grid(row=13, column=13)
        spell_6 = Label(root, bg="black", padx=40, pady=30)
        spell_6.grid(row=13, column=15)

        back_menu = Button(root, text="Назад", bg="#A9A9A9", padx=20, pady=30, font=("segoe UI", 16, "bold"),command=self.BackToMenu)
        back_menu.grid(row=1, column=1)

        self.old_widgets = [spher_1,
                            spher_2,
                            spher_3,
                            spell_1,
                            spell_2,
                            spell_3,
                            spell_4,
                            spell_5,
                            spell_6,
                            back_menu]

    def new_voker_game(self):
        [x.destroy() for x in self.widgets]
        spher_1 = Label(root, bg="black", padx=40, pady=30)
        spher_1.grid(row=15, column=7)
        spher_2 = Label(root, bg="black", padx=40, pady=30)
        spher_2.grid(row=15, column=9)
        spher_3 = Label(root, bg="black", padx=40, pady=30)
        spher_3.grid(row=15, column=11)

        spell_1 = Label(root, bg="black", padx=40, pady=30)
        spell_1.grid(row=13, column=5)
        spell_2 = Label(root, bg="black", padx=40, pady=30)
        spell_2.grid(row=13, column=7)
        spell_3 = Label(root, bg="black", padx=40, pady=30)
        spell_3.grid(row=13, column=9)
        spell_4 = Label(root, bg="black", padx=40, pady=30)
        spell_4.grid(row=13, column=11)
        spell_5 = Label(root, bg="black", padx=40, pady=30)
        spell_5.grid(row=13, column=13)
        spell_6 = Label(root, bg="black", padx=40, pady=30)
        spell_6.grid(row=13, column=15)

        back_menu = Button(root, text="Назад", bg="#A9A9A9", padx=20, pady=30, font=("segoe UI", 16, "bold"), command=self.BackToMenu)
        back_menu.grid(row=1, column=1)

        self.new_widgets = [spher_1,
                            spher_2,
                            spher_3,
                            spell_1,
                            spell_2,
                            spell_3,
                            spell_4,
                            spell_5,
                            spell_6,
                            back_menu]


    def BackToMenu(self):
        [x.destroy() for x in self.new_widgets]
        [x.destroy() for x in self.old_widgets]
        self.menu()



root = Tk()
Window(root)
root.mainloop()
