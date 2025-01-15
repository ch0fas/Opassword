import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from random import choice
import time

#Window

class Application(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Opassword Manager")
        self.minsize(640,320)

        #Frames For Each Type of Window


        #Show Frame
        def show_frame(self, frame):
            for i in self.winfo_children():
                i.pack_forget()
            frame.pack(fill="both", expand=True)


#Main Window
class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #Variables

        #Menu Bar
        menubar = tk.Listbox()

#Run Loop

if __name__ == "__main__":
    program = Application()
    program.mainloop()