from tkinter import *
from tkinter import ttk

class Window():

    def __init__(self, root):

        root.title("Invoker Game")#название окна
        #root.iconbitmap("") иконка окна
        root.config(background="#696969")#цвет окна

        """текст"""
        choes = Label(root, text="ВЫБЕРИТЕ РЕЖИМ", font=("Times New Roman", 30), bg="#696969").grid(row=2, column=9)
        info_new = Label(root, text="9 способностей", font=("Times New Roman", 17), bg="#696969").grid(row=9, column=8)
        info_old = Label(root, text="27 способностей", font=("Times New Roman", 17), bg="#696969").grid(row=9, column=10)

        """выбор режима"""
        for x in range (20):
            root.rowconfigure(x, weight=1)
            root.columnconfigure(x, weight=1)
        dota_1 = Button(root, text="Old Invoker", bg="#A9A9A9", padx=20, pady=30, font=("segoe UI", 16, "bold"), command=self.old_voker_game).grid(row=8, column=10)
        dota_2 = Button(root, text="Invoker", bg="#A9A9A9", padx=25, pady=30, font=("segoe UI", 16, "bold"),command=self.new_voker_game).grid(row=8, column=8)

        """блок разрешения окна"""
        root.geometry("1280x720")

        screen_info = Tk()
        if ((screen_info.winfo_screenwidth() != 1280) or
                screen_info.winfo_height() != 720):
            root.geometry(f"{screen_info.winfo_screenwidth()}x{screen_info.winfo_screenheight()}")
        screen_info.destroy()
        self.geometry = root.geometry




    def old_voker_game(self):
        old_game = Toplevel()
        root.geometry = self.geometry

    def new_voker_game(self):
        new_game = Toplevel()
        root.geometry = self.geometry



root = Tk()
Window(root)
root.mainloop()
