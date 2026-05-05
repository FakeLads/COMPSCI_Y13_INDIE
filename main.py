
# Imports tkinter features
from tkinter import *

from tkinter import PhotoImage

root = Tk()
root.title("Take Credit")
root.geometry("800x500")

class Loginpage:
    def __init__(self, parent):

        self.bg = PhotoImage(file="images/login_page_buttons.png")

        self.my_canvas = Canvas(root, width=800, height=500)
        self.my_canvas.pack(fill="both", expand=True)

        self.my_canvas.create_image(0,0, image=self.bg, anchor="nw")

        self.my_canvas.create_text(400,250, text="")

        self.inner_frame = Frame(root, bg="Black", )

        self.label = Label(root, text="Hello, Tkinter!")
        self.label.pack()

        self.enter_button = Button()

root.mainloop()





# The Login page for the GUI program
#class Loginpage:
 #   def __init__(self, parent):
#
 #       self.parent = parent
#
 #       self.inner_frame = Frame(parent, bg="Blue", padx=40, pady=100)
  #      self.inner_frame.pack()
#
#
 #       self.start_button = Button(self.inner_frame, width = 40, bg="White", fg="Black", font=("Helvetica", "24"), )
#        self.start_button.grid(row=1, column=3, pady=10, padx=10, sticky="nsew")

 #       self.entry_id = Entry(self.inner_frame, width = 40, bg = "White", fg="Black", font=("Helvetica", "24"), )
  #      self.entry_id.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
#
 #       self.exit_button = Button(self.inner_frame, width = 10, height= 10, bg = "White", fg="Black", font=("Helvetica", "12"), )
  #      self.exit_button.grid(row=3, column=3, padx=0, pady=0, sticky="nsew")
#
#
#
#
#

