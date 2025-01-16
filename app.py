import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from random import choice
import time
import json
import webbrowser

#Window

class Application(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Opassword")
        self.minsize(640,320)

        #Frames For Each Type of Window
        #Launch Window

        self.launchframe = LaunchFrame(self)

        #Main Frame
        self.mainframe = MainFrame(self)

        #User Creation Frame
        self.usercreateframe = UserCreateFrame(self)

        #App Credits Frame
        self.appcredits = AppCredits(self)


        #Show initial frame
        self.show_frame(self.launchframe)

    #Show Frame
    def show_frame(self, frame):
        for i in self.winfo_children():
            i.pack_forget()
        frame.pack(fill="both", expand=True)


#Launch Frame

class LaunchFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Variables -  Launch Frame

        #Widgets

        sign_in_label = ttk.Label(self, text="Sign In", font=("Arial", 36), background="black", anchor="center")
        users_list = tk.Listbox(self)
        app_creds = ttk.Button(master=self, text="App Credits", command= lambda: parent.show_frame(parent.appcredits))
        create_account_label = ttk.Button(self, text="Create Account", command=lambda: parent.show_frame(parent.usercreateframe))

        #Grid Configure
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1,weight=8)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Grid
        sign_in_label.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
        users_list.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
        app_creds.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)
        create_account_label.grid(row=0, column=1, sticky="nsew", padx=1, pady=1)

#User Creation Frame
class UserCreateFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #Variables

        #Functions

        def check_password():
            passone = password_entry.get()
            passtwo = password_entry2.get()

            if passone != passtwo:
                confirm_label.config(text="THE PASSWORDS ARE DIFFERENT")
            else:
                confirm_label.config(text="Passwords Are Set")

        #Widgets
        create_user_label = ttk.Label(self, text="Create A New User", font=("Arial", 36), background="black", anchor="center")
        username_label = ttk.Label(self, text="Username: ")
        username_entry = ttk.Entry(self)
        password_label = ttk.Label(self, text="Password: ")
        password_entry = ttk.Entry(self)
        password2_label = ttk.Label(self, text="Confirm Password: ")
        password_entry2 = ttk.Entry(self)
        confirm_user = ttk.Button(self, text="Create User", command=check_password)
        confirm_label = ttk.Label(self, text="", font=("Arial", 36), background="red", anchor="center")
        back_launch = ttk.Button(self, text="Back To Main Page", command= lambda: parent.show_frame(parent.launchframe)) 

        #Grid Config
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=2)
        self.grid_rowconfigure(5, weight=3)

        #Grid
        create_user_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)
        username_label.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
        username_entry.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)
        password_label.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)
        password_entry.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
        password2_label.grid(row=3, column=0, sticky="nsew", padx=1, pady=1)
        password_entry2.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)
        confirm_user.grid(row=4, column=0, sticky="nsew", padx=1, pady=1)
        back_launch.grid(row=4, column=1, sticky="nsew", padx=1, pady=1)
        confirm_label.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)



#Main Frame
class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #Variables

        #Menu Bar
        menubar = ttk.Menu(master=self)

#Password Creation Frame

#Password Modification Frame

#Password Deletion Messagebox

#App Credits Frame

class AppCredits(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Variables
        repo_url = "https://github.com/ch0fas/Opassword"

        #Functions
        def open_web():
            webbrowser.open(url=repo_url, new=1)

        #Variables - App Credits
        disclaimer_text = "This is NOT a safe password manager, just a demo. I am not responsible for any lost information or damages. Please use at your own risk."

        #Widgets
        me = ttk.Label(self, text="Made With 💌 by Sofi :)")
        disclaimer_label = ttk.Label(self, text=disclaimer_text, font=("Arial", 14), background="red", justify="center")
        disclaimer_label.bind('<Configure>', lambda e: disclaimer_label.config(wraplength=disclaimer_label.winfo_width()))
        repo_button = ttk.Button(self, text="Repository on Github", command=open_web)

        #Grid
        me.pack()
        disclaimer_label.pack()
        repo_button.pack()
        


#Run Loop

if __name__ == "__main__":
    program = Application()
    program.mainloop()