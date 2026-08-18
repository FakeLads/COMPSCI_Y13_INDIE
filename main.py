
# Imports tkinter features
from tkinter import *

from tkinter import messagebox, ttk

# Imports PIL Image and Image Tk; helps displays images in GUI
from PIL import Image, ImageTk

from tkinter import PhotoImage

root = Tk()
root.title("Take Credit") #Title of the program window
root.geometry("1920x1080") # Sets the width and height of the window



# The 'login_page' class holds all functions, methods and attributes related to the first opening page
class login_page:
    def __init__(self, parent):

        # The defined function that allows users to exit the program
        def message_exit():

            # Disables the exit button
            self.button_exit.config(state="disabled")

            # Creates the frame popup
            self.popup_frame = Frame(parent, borderwidth=3, relief="solid", height=500, width=1200, bg="Grey")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            # Displays the text asking the user
            self.text_label = Label(self.popup_frame, text="PLEASE CONFIRM YOUR EXIT", font=("Helvetica", 50),
                                    bg="Grey",fg="White")
            self.text_label.place(relx=0.5, rely=0.25, anchor=CENTER)

            # The Yes Button. If the user wants to leave they press this
            self.yes_button = Button(self.popup_frame, height=5, width=20, text="YES", font=("Helvetica", 20),
                                     bg="Dark Green", fg="White", command=proceed_destroy)
            self.yes_button.place(x=0, y=0, relx=0.1, rely=0.5)

            # The No Button. If the user does not wish to leave, they press this and return to the program
            self.no_button = Button(self.popup_frame, height=5, width=20, text="NO", font=("Helvetica", 20),
                                    bg="Red", fg="White", command=cancel_popup)
            self.no_button.place(x=0, y=0, relx=0.65, rely=0.5)

        # Stops the whole program/destroys it
        def proceed_destroy():
            root.destroy()

        # Defined function that is activated when the user selects 'No'
        def cancel_popup():
            self.popup_frame.destroy()  # Destroys the pop-up frame
            self.yes_button.destroy()  # Destroys the Yes button
            self.no_button.destroy()  # Destroys the No Button
            self.button_exit.config(state="normal")  # Reverts the exit button back to normal making it usable
            return  # Reverts back to state it was before

        # When the user selects the start button
        def go_button():
            self.my_label.destroy()
            self.my_frame.destroy()
            self.button_go.destroy()
            self.button_exit.destroy()
            rank_calculator(root) # Displays the rank score calculator page while the code before destroys all the elements before

        def subject_button():
            self.my_label.destroy()
            self.my_frame.destroy()
            self.button_go.destroy()
            self.button_exit.destroy()
            subject_information(root)  # Displays the rank score calculator page while the code before destroys all the elements before


        self.bg = Image.open("1.png") # self.bg is equal to bright_home.png
        self.resized_image = self.bg.resize((1920, 1080), Image.LANCZOS) # self.resized_image means if this variable is called the image must resize to the following measurements and display at a high quality
        self.bg = ImageTk.PhotoImage(self.resized_image)

        self.my_label = Label(parent, image=self.bg) # The label hosts the image, allowing it to be displayed
        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.my_frame = Frame(parent, height=300, width=1000, bg="#792782")
        self.my_frame.place(x=0, y=0, relx=0.5, rely=0.6, anchor=CENTER)

        # Button that takes user to rank score calculator page
        self.button_go = Button(self.my_frame, text="Calculator", height=2, width=20, font=("Helvetica", 20),
                                activebackground="#792782", command=go_button)
        self.button_go.grid(row=2, column=1, pady=20, padx=20, columnspan=1)

        self.subject_button = Button(self.my_frame, text="Subject Information", height=2, width=20,
                                     font=("Helvetica", 20), activebackground="#792782", command=subject_button)
        self.subject_button.grid(row=2, column=3, pady=20, padx=20, columnspan=1)

        # Exit button that allows the user to leave if they wish
        self.button_exit = Button(parent, text="EXIT", height=2, width=15, font=("Helvetica", 20),
                                  activebackground="#792782", command=message_exit)
        self.button_exit.place(relx=1, rely=1, x=-20, y=-5, anchor="se")


# The rank score calculator page
class rank_calculator:
    def __init__(self, parent):

        # The same defined function that is called when the user presses the exit button, displaying a exit popup
        def message_exit():

            self.exit_button.config(state="disabled")

            self.popup_frame = Frame(parent, borderwidth=3, relief="solid", height=500, width=1200, bg="Grey")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.text_label = Label(self.popup_frame, text="PLEASE CONFIRM YOUR EXIT", font=("Helvetica", 50),
                                    bg="Grey", fg="White")
            self.text_label.place(relx=0.5, rely=0.25, anchor=CENTER)

            self.yes_button = Button(self.popup_frame, height=5, width=20, text="YES", font=("Helvetica", 20),
                                     bg="Dark Green", fg="White", command=proceed_destroy)
            self.yes_button.place(x=0, y=0, relx=0.1, rely=0.5)

            self.no_button = Button(self.popup_frame, height=5, width=20, text="NO", font=("Helvetica", 20), bg="Red",
                                    fg="White", command=cancel_popup)
            self.no_button.place(x=0, y=0, relx=0.65, rely=0.5)

        def proceed_destroy():
            root.destroy()

        def cancel_popup():
            self.popup_frame.destroy()
            self.yes_button.destroy()
            self.no_button.destroy()
            self.exit_button.config(state="normal")
            return

        # Takes user to Subject Information page
        def to_subject():

            # Destroys all widgets and elements within the rank score calculator page
            self.rank_calc_button.destroy()
            self.information_button.destroy()
            self.help_button.destroy()
            self.my_label.destroy()
            self.exit_button.destroy()
            self.outer_frame.destroy()
            self.summary_button.destroy()
            self.subject_one.destroy()
            self.subject_two.destroy()
            self.subject_three.destroy()
            self.subject_four.destroy()
            self.subject_five.destroy()
            self.subject_1_achieved.destroy()
            self.subject_2_achieved.destroy()
            self.subject_3_achieved.destroy()
            self.subject_4_achieved.destroy()
            self.subject_5_achieved.destroy()
            self.subject_1_merit.destroy()
            self.subject_2_merit.destroy()
            self.subject_3_merit.destroy()
            self.subject_4_merit.destroy()
            self.subject_5_merit.destroy()
            self.subject_1_excellence.destroy()
            self.subject_2_excellence.destroy()
            self.subject_3_excellence.destroy()
            self.subject_4_excellence.destroy()
            self.subject_5_excellence.destroy()
            subject_information(root) # Calls upon the subject information page to appear


        # Calculates the total rank score from total amounts of credits entered into the table
        def calculate_summary():

            sub_1 = self.subject_one.get().strip()
            sub_2 = self.subject_two.get().strip()
            sub_3 = self.subject_three.get().strip()
            sub_4 = self.subject_four.get().strip()
            sub_5 = self.subject_five.get().strip()

            # If the does not have subjects 1 to 5 one of five error messages will appear asking the user to repair their issues
            if not sub_1:
                messagebox.showerror("ERROR", "You Are Missing Subject 1")
                return  # Reverts back to original state

            if not sub_2:
                messagebox.showerror("ERROR", "You Are Missing Subject 2")
                return

            if not sub_3:
                messagebox.showerror("ERROR", "You Are Missing Subject 3")
                return

            if not sub_4:
                messagebox.showerror("ERROR", "You Are Missing Subject 4")
                return

            if not sub_5:
                messagebox.showerror("ERROR", "You Are Missing Subject 5")
                return

            else:
                # Splits each subject into rows
                subject_rows = [
                    (self.subject_1_excellence, self.subject_1_merit, self.subject_1_achieved),
                    (self.subject_2_excellence, self.subject_2_merit, self.subject_2_achieved),
                    (self.subject_3_excellence, self.subject_3_merit, self.subject_3_achieved),
                    (self.subject_4_excellence, self.subject_4_merit, self.subject_4_achieved),
                    (self.subject_5_excellence, self.subject_5_merit, self.subject_5_achieved),

                ]

                # Sets the user's starting score to 0, from where it can be increased
                total_score = 0

                # Cycles through the list of subject rows
                for exc_cb, mer_cb, ach_cb in subject_rows:
                    exc_val = int(exc_cb.get() if exc_cb.get() else 0) # Reads the selected values from the dropdown menus. If the widget is empty, the system will return value as 0 in order to prevent the program from crashing
                    mer_val = int(mer_cb.get() if mer_cb.get() else 0) # The int() converts the string from the dropdown menu into a mathematical value to it can be calculated
                    ach_val = int(ach_cb.get() if ach_cb.get() else 0)

                    # Calculates the total amount of points earned according to how much a credit is multiplied for NCEA, and adds that to the total score
                    total_score += (exc_val * 4) + (mer_val * 3) + (ach_val * 2)

                self.subject_one.config(state="disabled")
                self.subject_two.config(state="disabled")
                self.subject_three.config(state="disabled")
                self.subject_four.config(state="disabled")
                self.subject_five.config(state="disabled")

                self.subject_1_excellence.config(state="disabled")
                self.subject_1_merit.config(state="disabled")
                self.subject_1_achieved.config(state="disabled")

                self.subject_2_excellence.config(state="disabled")
                self.subject_2_merit.config(state="disabled")
                self.subject_2_achieved.config(state="disabled")

                self.subject_3_excellence.config(state="disabled")
                self.subject_3_merit.config(state="disabled")
                self.subject_3_achieved.config(state="disabled")

                self.subject_3_excellence.config(state="disabled")
                self.subject_3_merit.config(state="disabled")
                self.subject_3_achieved.config(state="disabled")

                self.subject_4_excellence.config(state="disabled")
                self.subject_4_merit.config(state="disabled")
                self.subject_4_achieved.config(state="disabled")

                self.subject_5_excellence.config(state="disabled")
                self.subject_5_merit.config(state="disabled")
                self.subject_5_achieved.config(state="disabled")

                self.summary_button.config(state="disabled")

            # Deletes the summary popup
            def delete_summary():
                self.summary_frame.destroy()
                self.summary_label.destroy()
                self.delete_button.destroy()

                self.summary_button.config(state="normal")

                self.subject_one.config(state="readonly")
                self.subject_two.config(state="readonly")
                self.subject_three.config(state="readonly")
                self.subject_four.config(state="readonly")
                self.subject_five.config(state="readonly")

                self.subject_1_excellence.config(state="readonly")
                self.subject_1_merit.config(state="readonly")
                self.subject_1_achieved.config(state="readonly")

                self.subject_2_excellence.config(state="readonly")
                self.subject_2_merit.config(state="readonly")
                self.subject_2_achieved.config(state="readonly")

                self.subject_3_excellence.config(state="readonly")
                self.subject_3_merit.config(state="readonly")
                self.subject_3_achieved.config(state="readonly")

                self.subject_3_excellence.config(state="readonly")
                self.subject_3_merit.config(state="readonly")
                self.subject_3_achieved.config(state="readonly")

                self.subject_4_excellence.config(state="readonly")
                self.subject_4_merit.config(state="readonly")
                self.subject_4_achieved.config(state="readonly")

                self.subject_5_excellence.config(state="readonly")
                self.subject_5_merit.config(state="readonly")
                self.subject_5_achieved.config(state="readonly")

                self.exit_button.config(state="normal")

            # The exit button is disabled until the 'X' button is selected
            self.exit_button.config(state="disabled")

            # Creates a small frame popup, for all the elements to placed upon
            self.summary_frame = Frame(parent, borderwidth=3, relief="solid", height=650, width=1000, bg="Grey")
            self.summary_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            # Label that holds text telling the user their rank score is...
            self.summary_label = Label(self.summary_frame, text=f"Your Rank Score is:",
                                       font=("Helvetica", 50), bg="Grey", fg="White")
            self.summary_label.place(relx=0.5, rely=0.35, anchor=CENTER)

            # The label will print a large value of what the user got for their total rank score
            self.value_label = Label(self.summary_frame, text=f"{total_score}", font=("Helvetica", 80, "bold"),
                                     bg="Grey", fg="White")
            self.value_label.place(relx=0.5, rely=0.6, anchor=CENTER)

            exit_image = Image.open("red_x.png")  # The exit_image variable equates to the red x png
            exit_image = exit_image.resize((115, 128))  # Forces the image to resize according to the following measurements
            self.exit_image_tk = ImageTk.PhotoImage(exit_image)

            # A button that hosts the red X image
            self.delete_button = Button(self.summary_frame,
                                        command=delete_summary, image=self.exit_image_tk, cursor="hand2",
                                        background="Grey", relief="flat")
            self.delete_button.place(x=0, y=0, rely=0.13, relx=0.93, anchor=CENTER)
            self.delete_button.image = self.exit_image_tk

        # A defined function that displays a brief help popup frame
        def help_button():

            def delete_popup():
                self.popup_frame.destroy()
                self.help_text.destroy()
                self.delete_button.destroy()
                self.exit_button.config(state="normal")


            self.exit_button.config(state="disabled") # The exit button becomes unavailable as a means to not cause any errors

            self.popup_frame = Frame(parent, borderwidth=5, relief="solid", height=650, width=1300, bg="#792782")  # A popup frame used to host all elements needed for the help section
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            # A label that hosts all the text that explains the rank score calculator
            self.help_text = Label(self.popup_frame, text="\nCurious to discover the progress towards entry into University?"
                                                          " \nBy using the rank score calculator you are able to efficiently and effectively calculate your total rank score"
                                                          " \nfrom your total accumulated credits throughout your five subjects."
                                                          "\n\nTo operate the calculator, please select all five subjects you have taken throughout the year"
                                                          "\nbefore entering all achieved, merit and excellence credits."
                                                          "\nYou must enter in each subject, even if you have not acquired any credits throughout the year."
                                                          "\n\nOnce you have entered in all necessary values, select the 'SUMMARY' button. "
                                                          "\nIf you have entered in all five subjects, you will be greeted with your total rank score."
                                                          "\nYou will not receive your score if you do not enter in all five of your subjects."
                                                          "\n\nOnce you finished, select the ‘X’ button where you will be taken back to the original screen.", font=("Helvetica", 16), bg="#792782", fg="white",
                                   bd=0, highlightthickness=0) # The \n is used to create a new line that allows the text to move to the next space as a means to not go beyond the grid
            self.help_text.place(relx=0.5, rely=0.4, anchor=CENTER)

            # A repeat of the same code used to create the red X image before
            exit_image = Image.open("red_x.png")
            exit_image = exit_image.resize((115, 128))
            self.exit_image_tk = ImageTk.PhotoImage(exit_image)

            self.delete_button = Button(self.popup_frame,
                                        command=delete_popup, image=self.exit_image_tk, cursor="hand2",
                                        background="#792782", relief="flat")
            self.delete_button.place(x=0, y=0, rely=0.13, relx=0.93, anchor=CENTER)
            self.delete_button.image = self.exit_image_tk

        # Assigns the background for the rank score calculator to the self.main_bg variable. Similar to the class before which uses the same code
        self.main_bg = Image.open("bright_cal.png")
        self.resized_image = self.main_bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)
        self.my_label = Label(parent, image=self.bg)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1,relheight=1)

        self.exit_button = Button(parent, text="EXIT", height=2, width=15, font=("Helvetica", 20),
                                  activebackground="Grey", bg="White", command=message_exit)
        self.exit_button.place(relx=1, rely=1, x=-20, y=-5, anchor="se")

        self.rank_calc_button = Button(parent, text="Rank Score Calculator", height=2, width=17, font=("Helvetica", 20),
                                activebackground="#792782", bg="#a8a8a8", state="disabled")
        self.rank_calc_button.place(x=0, y=0, relx=0.330, rely=0.17, anchor='w')

        self.information_button = Button(parent, text="Subject Information", height=2, width=17, font=("Helvetica", 20),
                                         activebackground="#792782", bg="White", command=to_subject)
        self.information_button.place(x=0, y=0, relx=0.620, rely=0.17, anchor=CENTER)



        help_image = Image.open("Your4.png")
        help_image = help_image.resize((140, 140), Image.LANCZOS)
        self.help_image_tk = ImageTk.PhotoImage(help_image)

        self.help_button = Button(parent, image=self.help_image_tk, command=help_button, cursor="hand2",
                                  background="#792782", relief="flat")
        self.help_button.place(x=0, y=0, relx=0.940, rely=0.11, anchor=CENTER)


        # A frame that hosts the bottom two buttons being the Done button and the Summary button
        self.outer_frame = Frame(parent, height=130, width=1300, bg="#792782")
        self.outer_frame.pack_propagate(False)
        self.outer_frame.place(x=0, y=5, relx=0.5, rely=0.96, anchor='s')

        # Made available after the user selects the Done button. Once selected the user will be shown their rank score
        self.summary_button = Button(self.outer_frame, text="SUMMARY", height=4, width=20, font=("Helvetica", 20),
                                     activebackground="#792782", command=calculate_summary)
        self.summary_button.place(y=-10, relx=0.5, rely=0.5, anchor=CENTER)



        #Subject drop-down menus list:
        subjects = ['Visual English', 'Written English', 'Biology', 'Chemistry', 'Physics', 'Statistics', 'Calculus',
                    'History', 'Classics', 'Music Studies', 'Geography', 'Art', 'Computer Science', 'Media Studies',
                    'Economics', 'Food', 'Dance', 'Theatre Tech', 'Making Music', 'Photography']
        self.subject_one = ttk.Combobox(parent, font=("Helvetica", 20), values=subjects, state='readonly', justify="center") # Each of the comboboxes is a dropdrop down menu used by users to select their subjects
        self.subject_one.place(x=0, y=0, rely=0.440, relx=0.335, anchor=CENTER)

        # Values of the comboboxes equal to the subjects ist above
        self.subject_two = ttk.Combobox(parent, font=("Helvetica", 20), values=subjects,
                                        state='readonly', justify="center")
        self.subject_two.place(x=0, y=0, rely=0.505, relx=0.335, anchor=CENTER)

        self.subject_three = ttk.Combobox(parent, font=("Helvetica", 20), values=subjects,
                                          state='readonly', justify="center")
        self.subject_three.place(x=0, y=0, rely=0.565, relx=0.335, anchor=CENTER)

        self.subject_four = ttk.Combobox(parent, font=("Helvetica", 20), values=subjects,
                                         state='readonly', justify="center")
        self.subject_four.place(x=0, y=0, rely=0.625, relx=0.335, anchor=CENTER)

        self.subject_five = ttk.Combobox(parent, font=("Helvetica", 20), values=subjects,
                                         state='readonly', justify="center")
        self.subject_five.place(x=0, y=0, rely=0.690, relx=0.335, anchor=CENTER)


        #Values for credits from 0 to 24. These are the options users can select from
        credits_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                            '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                            '20', '21', '22', '23', '24']
        # Subject 1 credit boxes:
        self.subject_1_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20), values=credits_num,
                                               state='readonly', justify="center") # The comboboxes here hold all the numbers 0 to 24 for the total amount of credits an individual score.
        self.subject_1_excellence.place(x=0, y=0, rely=0.440, relx=0.490, anchor=CENTER) # Every combobox for subject 1 has the relative Y-axis value of 0.440 as they all have the same height

        self.subject_1_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_1_merit.place(x=0, y=0, rely=0.440, relx=0.605, anchor=CENTER)

        self.subject_1_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_1_achieved.place(x=0, y=0, rely=0.440, relx=0.712, anchor=CENTER)


        #Subject 2 credit boxes:
        self.subject_2_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20), values=credits_num,
                                            state='readonly', justify="center") # Like the comboboxes before subject 2 and beyond follow the same structuring, with slight differences made to the placement.
        self.subject_2_excellence.place(x=0, y=0, rely=0.505, relx=0.490, anchor=CENTER) # The placement of each box to the Y-axis is the same, but as can be seen the relative X-axis follows the same values as the subject 1 boxes.

        self.subject_2_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_2_merit.place(x=0, y=0, rely=0.505, relx=0.605, anchor=CENTER)

        self.subject_2_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_2_achieved.place(x=0, y=0, rely=0.505, relx=0.712, anchor=CENTER)


        #Subject 3 credit boxes:
        self.subject_3_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_3_excellence.place(x=0, y=0, rely=0.565, relx=0.490, anchor=CENTER)

        self.subject_3_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_3_merit.place(x=0, y=0, rely=0.565, relx=0.605, anchor=CENTER)

        self.subject_3_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_3_achieved.place(x=0, y=0, rely=0.565, relx=0.712, anchor=CENTER)

        #Subject 4 credit boxes:
        self.subject_4_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_4_excellence.place(x=0, y=0, rely=0.630, relx=0.490, anchor=CENTER)

        self.subject_4_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20),
                                            values=credits_num,
                                            state='readonly', justify="center")
        self.subject_4_merit.place(x=0, y=0, rely=0.630, relx=0.605, anchor=CENTER)

        self.subject_4_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20),
                                               values=credits_num,
                                               state='readonly', justify="center")
        self.subject_4_achieved.place(x=0, y=0, rely=0.630, relx=0.712, anchor=CENTER)


        #Subject 5 credit boxes:
        self.subject_5_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_5_excellence.place(x=0, y=0, rely=0.693, relx=0.490, anchor=CENTER)

        self.subject_5_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20),
                                            values=credits_num,
                                            state='readonly', justify="center")
        self.subject_5_merit.place(x=0, y=0, rely=0.693, relx=0.605, anchor=CENTER)

        self.subject_5_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvetica", 20),
                                               values=credits_num,
                                               state='readonly',
                                               justify="center")
        self.subject_5_achieved.place(x=0, y=0, rely=0.693, relx=0.712, anchor=CENTER)

# The Subject Information page/class
class subject_information:
   def __init__(self, parent):

        # Defines the exit buttons function
        def message_exit():

            self.exit_button.config(state="disabled")

            self.popup_frame = Frame(parent, borderwidth=3, relief="solid", height=500, width=1200, bg="Grey")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.text_label = Label(self.popup_frame, text="PLEASE CONFIRM YOUR EXIT", font=("Helvetica", 50),
                                    bg="Grey", fg="White")
            self.text_label.place(relx=0.5, rely=0.25, anchor=CENTER)

            self.yes_button = Button(self.popup_frame, height=5, width=20, text="YES", font=("Helvetica", 20),
                                     bg="Dark Green", fg="White", command=proceed_destroy)
            self.yes_button.place(x=0, y=0, relx=0.1, rely=0.5)

            self.no_button = Button(self.popup_frame, height=5, width=20, text="NO", font=("Helvetica", 20), bg="Red",
                                    fg="White", command=cancel_popup)
            self.no_button.place(x=0, y=0, relx=0.65, rely=0.5)


        def proceed_destroy():
            root.destroy()

        def cancel_popup():
            self.popup_frame.destroy()
            self.yes_button.destroy()
            self.no_button.destroy()
            self.exit_button.config(state="normal")
            return

        def to_rank():
            self.rank_calc_button.destroy()
            self.information_button.destroy()
            self.help_button.destroy()
            self.my_label.destroy()
            self.exit_button.destroy()
            rank_calculator(root)

        # Defined function for the subject selection combobox
        def subject_selected():

            # Retrives the variable selected from the combobox
            selected_subject = self.subject.get().strip()

            exit_image = Image.open("red_x.png")
            exit_image = exit_image.resize((115, 128))
            self.exit_image_tk = ImageTk.PhotoImage(exit_image)

            # Because the combobox holds the default text: "Select A Subject", if the user chooses to proceed they will be stopped and met with an error message
            if selected_subject == "Select A Subject":
                messagebox.showerror("Error", "Please select a subject.") # The error message popup
                return

            # If in some instance that the combobox becomes blank with no text within, the same error message will appear informing the user to select a subject
            if not selected_subject:
                messagebox.showerror("Error", "Please select a subject.")
                return

            # If the user selects Written English, this if statement will be activated and processed
            if selected_subject == 'Written English':
                self.exit_button.config(state="disabled") # Exit button will be disabled until the user exits the popup

                self.description_page = Frame(parent, borderwidth=3, relief="solid", height=850, width=850, bg="white") # A frame that holds the image of the subject the user selected
                self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER) # Specifically places the frame in the middle of the screen, so the image is the center of the users attention

                # Defines a function that will delete the popup frame if activated
                def delete_popup_wri():
                    self.exit_button.config(state="normal") # Exit button becomes usable
                    self.description_page.destroy() # Destroys frame
                    self.english_label.destroy() # Destroys the label holding the image

                eng_image = Image.open("vis_eng.png") # Assigns the variable to the specific image
                eng_image = eng_image.resize((600, 800), Image.LANCZOS) # Resizes to fit within the smaller frame while still having good quality due to the 'Image.LANCZOS'
                self.eng_image_tk = ImageTk.PhotoImage(eng_image)

                self.english_label = Label(parent, image=self.eng_image_tk, background="white") # The label holding the image
                self.english_label.image = self.eng_image_tk
                self.english_label.place(relx=0.5, rely=0.5, anchor=CENTER) # Places the label directly in the center of the frame

                # Defines the delete button that uses an 'X' image as the button.
                self.delete_button = Button(self.description_page,
                                            command=delete_popup_wri, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat") # Assigned the command to destroy the frame and label containing the image
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

            # The process described in the Written English if statement, is repeated through the rest of the subjects used. The only changes made will be to the variable names and titles of the png images
            if selected_subject == 'Visual English':
                self.exit_button.config(state="disabled")

                self.description_page = Frame(parent, borderwidth=3, relief="solid", height=850, width=850, bg="white")
                self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

                def delete_popup_vis():
                    self.exit_button.config(state="normal")
                    self.description_page.destroy()
                    self.vis_english_label.destroy()

                vis_eng_image = Image.open("writ_eng.png")
                vis_eng_image = vis_eng_image.resize((600, 800), Image.LANCZOS)
                self.vis_eng_image_tk = ImageTk.PhotoImage(vis_eng_image)

                self.vis_english_label = Label(parent, image=self.vis_eng_image_tk, background="white")
                self.vis_english_label.image = self.vis_eng_image_tk
                self.vis_english_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup_vis, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

            if selected_subject == 'Music Studies':
                self.exit_button.config(state="disabled")

                self.description_page = Frame(parent, borderwidth=3, relief="solid", height=850, width=850, bg="white")
                self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

                def delete_popup_mus():
                    self.exit_button.config(state="normal")
                    self.description_page.destroy()
                    self.mus_label.destroy()

                mus_image = Image.open("mus.png")
                mus_image = mus_image.resize((600, 800), Image.LANCZOS)
                self.mus_image_tk = ImageTk.PhotoImage(mus_image)

                self.mus_label = Label(parent, image=self.mus_image_tk, background="white")
                self.mus_label.image = self.mus_image_tk
                self.mus_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup_mus, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

            if selected_subject == 'Biology':
                self.exit_button.config(state="disabled")

                self.description_page = Frame(parent, borderwidth=3, relief="solid", height=850, width=850, bg="white")
                self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

                def delete_popup_bio():
                    self.exit_button.config(state="normal")
                    self.description_page.destroy()
                    self.bio_label.destroy()

                bio_image = Image.open("bio.png")
                bio_image = bio_image.resize((600, 800), Image.LANCZOS)
                self.bio_image_tk = ImageTk.PhotoImage(bio_image)

                self.bio_label = Label(parent, image=self.bio_image_tk, background="white")
                self.bio_label.image = self.bio_image_tk
                self.bio_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup_bio, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

            if selected_subject == 'Chemistry':
                self.exit_button.config(state="disabled")

                self.description_page = Frame(parent, borderwidth=3, relief="solid", height=850, width=850, bg="white")
                self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

                def delete_popup_chem():
                    self.exit_button.config(state="normal")
                    self.description_page.destroy()
                    self.chem_label.destroy()

                chem_image = Image.open("chem.png")
                chem_image = chem_image.resize((600, 800), Image.LANCZOS)
                self.chem_image_tk = ImageTk.PhotoImage(chem_image)

                self.chem_label = Label(parent, image=self.chem_image_tk, background="white")
                self.chem_label.image = self.chem_image_tk
                self.chem_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup_chem, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

            if selected_subject == 'Physics':
                self.exit_button.config(state="disabled")

                self.description_page = Frame(parent, borderwidth=3, relief="solid", height=850, width=850, bg="white")
                self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

                def delete_popup_phy():
                    self.exit_button.config(state="normal")
                    self.description_page.destroy()
                    self.phy_label.destroy()

                phy_image = Image.open("phy.png")
                phy_image = phy_image.resize((600, 800), Image.LANCZOS)
                self.phy_image_tk = ImageTk.PhotoImage(phy_image)

                self.phy_label = Label(parent, image=self.phy_image_tk, background="white")
                self.phy_label.image = self.phy_image_tk
                self.phy_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup_phy, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

            if selected_subject == 'Statistics':
                self.exit_button.config(state="disabled")

                self.description_page = Frame(parent, borderwidth=3, relief="solid", height=850, width=850, bg="white")
                self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

                def delete_popup_stat():
                    self.exit_button.config(state="normal")
                    self.description_page.destroy()
                    self.stats_label.destroy()

                stats_image = Image.open("stats.png")
                stats_image = stats_image.resize((600, 800), Image.LANCZOS)
                self.stats_image_tk = ImageTk.PhotoImage(stats_image)

                self.stats_label = Label(parent, image=self.stats_image_tk, background="white")
                self.stats_label.image = self.stats_image_tk
                self.stats_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup_stat, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

        # Defined function that holds the commands used for the Help button
        def help_button():

            def delete_popup():
                self.popup_frame.destroy()
                self.delete_button.destroy()
                self.exit_button.config(state="normal")


            self.exit_button.config(state="disabled")

            # The popup frame that hosts the text for the help section
            self.popup_frame = Frame(parent, borderwidth=5, relief="solid", height=650, width=1300, bg="#792782")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER) # Places the popup frame to the center of the screen

            # The label works almost identical to the one used for the previous help page, the only difference being the text describing the particular page the user is currently on, being the Subject Information page
            self.help_text = Label(self.popup_frame,
                                   text="\nThe Subject Information page allows you to freely browse various level 3 subjects "
                                        "\nto understand what each subject has to offer. "
                                        "\n\nSimply by entering the subject of your choice and selecting the ‘SEARCH’ button, "
                                        "\nyou are given a brief description of the subject, including what it might offer to you as a student. "
                                        "\n\nTo exit the subject, simply select the ‘X’ button and you will be taken back to the original page, "
                                        "\nfree to choose a new subject if wanted.", font=("Helvetica", 18), bg="#792782", fg="white",
                                   bd=0, highlightthickness=0)
            self.help_text.place(relx=0.5, rely=0.4, anchor=CENTER)

            exit_image = Image.open("red_x.png")
            exit_image = exit_image.resize((115, 128))
            self.exit_image_tk = ImageTk.PhotoImage(exit_image)

            self.delete_button = Button(self.popup_frame,
                                        command=delete_popup, image=self.exit_image_tk, cursor="hand2",
                                        background="#792782", relief="flat")
            self.delete_button.place(x=0, y=0, rely=0.13, relx=0.93, anchor=CENTER)
            self.delete_button.image = self.exit_image_tk

        self.main_bg = Image.open("2.png")
        self.resized_image = self.main_bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)
        self.my_label = Label(parent, image=self.bg)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image = self.bg
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.exit_button = Button(parent, text="EXIT", height=2, width=15, font=("Helvetica", 20),
                                  activebackground="#792782", bg="white", command=message_exit)
        self.exit_button.place(relx=1, rely=1, x=-20, y=-5, anchor="se")

        self.rank_calc_button = Button(parent, text="Rank Score Calculator", height=2, width=17, font=("Helvetica", 20),
                                       activebackground="#792782", bg="White", command=to_rank)
        self.rank_calc_button.place(x=0, y=0, relx=0.330, rely=0.17, anchor='w')

        self.information_button = Button(parent, text="Subject Information", height=2, width=17, font=("Helvetica", 20),
                                         activebackground="#792782", bg="#a8a8a8", state="disabled")
        self.information_button.place(x=0, y=0, relx=0.620, rely=0.17, anchor=CENTER)


        help_image = Image.open("Your4.png")
        help_image = help_image.resize((140, 140), Image.LANCZOS)
        self.help_image_tk = ImageTk.PhotoImage(help_image)

        self.help_button = Button(parent, image=self.help_image_tk, command=help_button, cursor="hand2",
                                  background="#792782", relief="flat")
        self.help_button.place(x=0, y=0, relx=0.940, rely=0.11, anchor=CENTER)

        # A list that hosts the subjects the user is able to find more about
        subject_choice = ['Written English', 'Visual English', 'Biology', 'Physics', 'Chemistry', 'Statistics']
        self.subject = ttk.Combobox(parent, width=55, height=150, font=("Helvetica", 35),
                                    values=subject_choice, state="readonly", justify="center")
        self.subject.place(x=0, y=0, relheight=0.1, relx=0.5, rely=0.620, anchor=CENTER) # Due to the state of the combobox, the user is not able to type anything, making it more difficult to potentially cause any errors, while also allowing the default text to be tampered with.
        self.subject.set("Select A Subject") # Sets default text to the combobox to help identify what the user must do to proceed

        # Once the user has a selected a subject they are able to select the 'Search' button which will in turn activated the command: 'subject_selected' and find the if statement that applied to what they are looking for
        self.search_button = Button(parent, text="SEARCH", height=2, width=17, font=("Helvetica", 20),
                                    activebackground="#792782", command=subject_selected, state="normal")
        self.search_button.place(x=0, y=0, relx=0.5, rely=0.725, anchor=CENTER)




app = login_page(root) # Allows the program to be displayed

root.attributes("-fullscreen", True) # Automatically makes the program take up the screen

root.mainloop() # Runs the program
