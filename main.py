
# Imports tkinter features
from tkinter import *

from tkinter import messagebox, ttk

# Imports PIL Image and Image Tk; helps diplays images in GUI
from PIL import Image, ImageTk

from tkinter import PhotoImage

root = Tk()
root.title("Take Credit") #Title of the program window
root.geometry("1920x1080") # Sets the width and height of the window

id_list = []

branch_list = []

def exit_gui():
    root.destroy()



# The 'Loginpage' class holds all functions, methods and attributes related to the first opening page
class Loginpage:
    def __init__(self, parent):

        def name_collection():

            name = self.entry_id.get().strip()

            if not name:
                messagebox.showerror("ERROR",
                                     "Please enter a username")
                return

            if len(name) > 10:
                messagebox.showerror("ERROR",
                                     "Username must be 10 characters or less")
                return

            else:
                id_list.append(name)



        self.bg = Image.open("login_page_NO_buttons.png")

        self.resized_image = self.bg.resize((1920, 1080), Image.LANCZOS)

        self.bg = ImageTk.PhotoImage(self.resized_image)

        self.my_label = Label(parent, image=self.bg)

        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.my_frame = Frame(parent, height=300, width=1000, bg="#52005b")
        self.my_frame.place(x=0, y=0, relx=0.5, rely=0.6, anchor=CENTER)

        self.entry_id = Entry(self.my_frame, font=("Helvitica", 28))
        self.entry_id.grid(row=1, column=1, padx=20, pady=20, columnspan=2)

        choices = ['1', '2', '3']
        self.branch_dropdown = ttk.Combobox(self.my_frame, font=("Helvitica", 28), values=choices)
        self.branch_dropdown.grid(row=1, column=3, padx= 20, pady=20, columnspan=2)

        self.button_go = Button(self.my_frame, text="START HERE", height=2, width=16, font=("Helvitica", 20))
        self.button_go.grid(row=2, column=2, pady=20, columnspan=2)

        self.button_exit = Button(parent, text="EXIT", height=2, width=7, font=("Helvitica", 20), command=exit_gui)
        self.button_exit.place(relx=1, rely=1, x=-20, y=-20, anchor="se")





app = Loginpage(root)

root.mainloop()







