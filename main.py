
# Imports tkinter features
from tkinter import *

# Imports the messagebox function from the tkinter library
from tkinter import messagebox

from tkinter import PhotoImage

# The Login page for the GUI program
class Loginpage:
    def __init__(self, parent):

        self.parent = parent

        self.inner_frame = Frame(parent, bg="Blue", padx=40, pady=100)

        self.start_button = Button(self.inner_frame, width = 40, bg="White", fg="Black", font=("Helvetica", "24"), )
        self.start_button.grid(row=1, column=3, pady=10, padx=10, sticky="nsew")

        self.entry_id = Entry(self.inner_frame, width = 40, bg = "White", fg="Black", font=("Helvetica", "24"), )
        self.entry_id.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")

        self.exit_button = Button(self.inner_frame, width = 10, height= 10, bg = "White", fg="Black", font=("Helvetica", "12"), )
        self.exit_button.grid(row=3, column=3, padx=0, pady=0, sticky="nsew")




if __name__ == "__main__":

    root = Tk()
    root.title("Take Credit")
    #root.geometry("1920X1080")
    #root.resizable(False, False)
    Loginpage(root)
    root.mainloop()