
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


# The 'Loginpage' class holds all functions, methods and attributes related to the first opening page
class Loginpage:
    def __init__(self, parent):

        def message_exit():

            self.popup_frame = Frame(parent, height=500, width=1200, bg="Grey")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.text_label = Label(self.popup_frame, height=50, width=50, text="WOULD YOU LIKE TO EXIT?", font=("Helvitica", 30), fg="White")
            self.text_label.place(x=0, y=0, relx=0.5, rely=1, anchor='n')

            self.yes_button = Button(self.popup_frame, height=5, width=20, text="YES", font=("Helvitica", 20), bg="Dark Green", fg="White", command=proceed_destroy)
            self.yes_button.place(x=0, y=0, relx=0.1, rely=0.5)

            self.no_button = Button(self.popup_frame, height=5, width=20, text="NO", font=("Helvitica", 20), bg="Red", fg="White", command=cancel_popup)
            self.no_button.place(x=0, y=0, relx=0.65, rely=0.5)

        def proceed_destroy():
            root.destroy()

        def cancel_popup():
            self.popup_frame.destroy()
            self.yes_button.destroy()
            self.no_button.destroy()
            return



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

        self.button_go = Button(self.my_frame, text="START HERE", height=2, width=16, font=("Helvitica", 20),
                                activebackground="#a3a3a3", command=id_collection)
        self.button_go.grid(row=2, column=2, pady=20, columnspan=2)

        self.button_exit = Button(parent, text="EXIT", height=2, width=15, font=("Helvitica", 20),
                                  activebackground="#a3a3a3", command=message_exit)
        self.button_exit.place(relx=1, rely=1, x=-20, y=-5, anchor="se")





class Rankcalculator:
    def __init__(self, parent):

        def message_exit():
            self.popup_frame = Frame(parent, height=500, width=1200, bg="Grey")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.yes_button = Button(self.popup_frame, height=5, width=20, text="YES", font=("Helvitica", 20),
                                     bg="Dark Green", fg="White", command=proceed_destroy)
            self.yes_button.place(x=0, y=0, relx=0.1, rely=0.5)

            self.no_button = Button(self.popup_frame, height=5, width=20, text="NO", font=("Helvitica", 20), bg="Red",
                                    fg="White", command=cancel_popup)
            self.no_button.place(x=0, y=0, relx=0.65, rely=0.5)

        def proceed_destroy():
            root.destroy()

        def cancel_popup():
            self.popup_frame.destroy()
            self.yes_button.destroy()
            self.no_button.destroy()

        def home_back():

            self.home_button.destroy()
            self.rank_calc_button.destroy()
            self.information_button.destroy()
            self.help_button.destroy()
            self.my_label.destroy()
            self.exit_button.destroy()
            self.inner_frame.destroy()
            self.outer_frame.destroy()
            self.done_button.destroy()
            self.summary_button.destroy()
            Loginpage(root)

        self.main_bg = Image.open("rank_calc.png")
        self.resized_image = self.main_bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)
        self.my_label = Label(parent, image=self.bg)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1,relheight=1)

        self.exit_button = Button(parent, text="EXIT", height=2, width=10, font=("Helvitica", 15),
                                  activebackground="#a3a3a3", command=message_exit)
        self.exit_button.place(relx=1, rely=1, x=-20, y=-5, anchor="se")

        self.home_button = Button(parent, text="Home", height=2, width=17, font=("Helvitica", 20),
                                  activebackground="#a3a3a3", command=home_back)
        self.home_button.place(x=0, y=0, relx=0.189, rely=0.15, anchor='w')

        self.rank_calc_button = Button(parent, text="Rank Score Calculator", height=2, width=17, font=("Helvitica", 20),
                                activebackground="#a3a3a3")
        self.rank_calc_button.place(x=0, y=0, relx=0.364, rely=0.15, anchor='w')

        self.information_button = Button(parent, text="Subject Information", height=2, width=17, font=("Helvitica", 20),
                                         activebackground="#a3a3a3")
        self.information_button.place(x=0, y=0, relx=0.608, rely=0.15, anchor=CENTER)

        self.help_button = Button(parent, text="Help", height=2, width=17, font=("Helvitica", 20),
                                         activebackground="#a3a3a3")
        self.help_button.place(x=0, y=0, relx=0.850, rely=0.15, anchor='e')

        self.inner_frame = Frame(parent, height=400, width=1350, bg="White")
        self.inner_frame.pack_propagate(False)
        self.inner_frame.place(x=0, y=20, relx=0.5, rely=0.5, anchor=CENTER)


        self.outer_frame = Frame(height=130, width=1300, bg="#52005b")
        self.outer_frame.pack_propagate(False)
        self.outer_frame.place(x=0, y=5, relx=0.5, rely=0.96, anchor='s')

        self.done_button = Button(self.outer_frame, text="DONE", height=4, width=20, font=("Helvitica", 20),
                                  activebackground="#a3a3a3")
        self.done_button.place(x=10, y=-10, relx=0, rely=0.5, anchor="w")

        self.summary_button = Button(self.outer_frame, text="SUMMARY", height=4, width=20, font=("Helvitica", 20),
                                     activebackground="#a3a3a3")
        self.summary_button.place(x=10, y=-10, relx=1.0, rely=0.5, anchor="e")





        #self.navi_bar = Frame(parent, height=160, width=1400, bg="White")
        #self.navi_bar.pack_propagate(False)
        #self.navi_bar.place(x=0, y=5, relx=0.5, rely=0.10, anchor='n')


        #self.home_butt = Button(self.navi_bar, text="HOME", height=4, width=20, font=("Helvitica", 20))
        #self.home_butt.place(x=10, y=-10, relx=1.0, rely=0.5, anchor="w")





app = Loginpage(root)

root.mainloop()
