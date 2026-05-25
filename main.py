
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

        def id_collection():

            name = self.entry_id.get().strip()

            branch = self.branch_dropdown.get().strip()

            if not name:
                messagebox.showerror("ERROR",
                                     "Please enter an I.D")
                return

            if len(name) > 5:
                messagebox.showerror("ERROR TOO MUCH CHARACTERS",
                                     "Student ID must be 5 characters")
                return

            if len(name) < 5:
                messagebox.showerror("ERROR: INSUFFICIENT AMOUNT OF CHARACTERS",
                                     "Student ID must be 5 characters")
                return

            if not branch:
                messagebox.showerror("ERROR", "Drop Down Menu Empty")
                return

            if len(branch) > 1:
                messagebox.showerror("ERROR: TOO MANY CHARACTERS", "Year level should be a single digit")
                return

            else:
                id_list.append(name)
                self.my_frame.destroy()
                self.my_label.destroy()
                self.button_exit.destroy()
                Rankcalculator(root)



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
        self.branch_dropdown.grid(row=1, column=3, padx=20, pady=20, columnspan=2)

        self.button_go = Button(self.my_frame, text="START HERE", height=2, width=16, font=("Helvitica", 20), activebackground="#a3a3a3", command=id_collection)
        self.button_go.grid(row=2, column=2, pady=20, columnspan=2)

        self.button_exit = Button(parent, text="EXIT", height=2, width=15, font=("Helvitica", 20), activebackground="#a3a3a3", command=exit_gui)
        self.button_exit.place(relx=1, rely=1, x=-20, y=-5, anchor="se")





class Rankcalculator:
    def __init__(self, parent):

        self.main_bg = Image.open("calc.png")
        self.resized_image = self.main_bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)
        self.my_label = Label(parent, image=self.bg)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1,relheight=1)



        self.inner_frame = Frame(parent, height=400, width=1350, bg="White")
        self.inner_frame.pack_propagate(False)
        self.inner_frame.place(x=0, y=20, relx=0.5, rely=0.5, anchor=CENTER)

        self.small_bg = Image.open("rank.png")
        self.resized_small = self.small_bg.resize((400, 1350), Image.LANCZOS)
        self.small_tk_img = ImageTk.PhotoImage(self.resized_small)

        self.cal_label = Label(self.inner_frame, image=self.small_bg)
        self.cal_label.image = self.small_tk_img
        self.cal_label.pack()



        self.outer_frame = Frame(height=130, width=1300, bg="#52005b")
        self.outer_frame.pack_propagate(False)
        self.outer_frame.place(x=0, y=5, relx=0.5, rely=0.96, anchor='s')

        self.done_button = Button(self.outer_frame, text="DONE", height=4, width=20, font=("Helvitica", 20), activebackground="#a3a3a3")
        self.done_button.place(x=10, y=-10, relx=0, rely=0.5, anchor="w")

        self.summary_button = Button(self.outer_frame, text="SUMMARY", height=4, width=20, font=("Helvitica", 20), activebackground="#a3a3a3")
        self.summary_button.place(x=10, y=-10, relx=1.0, rely=0.5, anchor="e")



        self.navi_bar = Frame(parent, height=130, width=1300, bg="White")
        self.navi_bar.pack_propagate(False)
        self.navi_bar.place(x=0, y=5, relx=0.5, rely=0.15, anchor='n')

        self.navbar_image = Image.open("fanta_colour.png")
        self.resized_image = self.navbar_image.resize((130, 1300), Image.LANCZOS)
        self.bg_3 = ImageTk.PhotoImage(self.resized_image)

        self.second_label = Label(self.navi_bar, image=self.bg_3)
        self.second_label.image = self.bg_3
        self.second_label.pack()

        self.home_butt = Button(self.navi_bar, text="HOME", height=4, width=20, font=("Helvitica", 20))
        self.home_butt.place(x=10, y=-10, relx=1.0, rely=0.5, anchor="w")
















app = Loginpage(root)

root.mainloop()







