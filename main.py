
# Imports tkinter features
from tkinter import *

# Imports the messagebox function from the tkinter library
from tkinter import messagebox

from tkinter import PhotoImage

main = Tk()

# The Login page for the GUI program
class Loginpage:
    def __init__(self, main_canvas,bg_image_canvas_id):

        self.main_canvas = main_canvas

        self.bg_image_canvas_id =  bg_image_canvas_id

        self.canvas_width = main_canvas.winfo_width()
        self.canvas_height = main_canvas.winfo_height()

        # If the width and height of an image equates to 1, the size will be changed to the following values below it.
        if self.canvas_width == 1:
            self.canvas_width = 1400
        if self.canvas_height == 1:
            self.canvas_height == 800


        self.inner_frame = Frame(main_canvas, bg="Grey", padx=40, pady=100)

        self.center_x = self.canvas_width / 2
        self.center_y = self.canvas_height / 2

        self.frame_window = main_canvas.create_window(self.center_x, self.center_y, window=self.inner_frame,
                                                      anchor="center")

        self.inner_frame.columnconfigure(0, weight=1)
        self.inner_frame.columnconfigure(1, weight=3)
        self.inner_frame.columnconfigure(2, weight=1)

        for i in range(4):
            self.inner_frame.rowconfigure(i, weight=1)


root = Tk()
root.title("Take Credit")
root.mainloop()