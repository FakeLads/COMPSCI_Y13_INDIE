
# Imports tkinter features
from tkinter import *

# Imports PIL Image and Image Tk; helps diplays images in GUI
from PIL import Image, ImageTk

from tkinter import PhotoImage

root = Tk()
root.title("Take Credit") #Title of the program window
root.geometry("1920x1080") # Sets the width and height of the window

# The 'Loginpage' class holds all functions, methods and attributes related to the first opening page
class Loginpage:
    def __init__(self, parent):

        self.bg = Image.open("login_page_NO_buttons.png")

        self.resized_image = self.bg.resize((1920, 1080), Image.LANCZOS)

        self.bg = ImageTk.PhotoImage(self.resized_image)

        self.my_label = Label(parent, image=self.bg)

        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.my_frame = Frame(parent, height=100, width=100, bg="Red")
        self.my_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.entry_id = Entry(self.my_frame)
        self.entry_id.place(relx = 0.5, rely= 0.5, anchor = CENTER)

        self.button_go = Button(self.my_frame, text="START HERE")
        self.button_go.place(relx=0.5, rely=0.5, anchor = CENTER)


app = Loginpage(root)

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

