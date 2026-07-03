
# Imports tkinter features
from tkinter import *

from tkinter import messagebox, ttk

# Imports PIL Image and Image Tk; helps displays images in GUI
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

            self.button_exit.config(state="disabled")

            self.popup_frame = Frame(parent, borderwidth=3, relief="solid", height=500, width=1200, bg="Grey")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.text_label = Label(self.popup_frame, text="PLEASE CONFIRM YOUR EXIT", font=("Helvitica", 50), bg="Grey", fg="White")
            self.text_label.place(relx=0.5, rely=0.25, anchor=CENTER)

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
            self.button_exit.config(state="normal")
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
        self.branch_dropdown = ttk.Combobox(self.my_frame, font=("Helvitica", 28), values=choices, state='readonly', justify='center')
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

            self.exit_button.config(state="disabled")

            self.popup_frame = Frame(parent, borderwidth=3, relief="solid", height=500, width=1200, bg="Grey")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.text_label = Label(self.popup_frame, text="PLEASE CONFIRM YOUR EXIT", font=("Helvitica", 50),
                                    bg="Grey", fg="White")
            self.text_label.place(relx=0.5, rely=0.25, anchor=CENTER)

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
            self.exit_button.config(state="normal")
            return

        def home_back():

            self.home_button.destroy()
            self.rank_calc_button.destroy()
            self.information_button.destroy()
            self.help_button.destroy()
            self.my_label.destroy()
            self.exit_button.destroy()
            self.outer_frame.destroy()
            self.done_button.destroy()
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
            Loginpage(root)

        def to_subject():

            self.home_button.destroy()
            self.rank_calc_button.destroy()
            self.information_button.destroy()
            self.help_button.destroy()
            self.my_label.destroy()
            self.exit_button.destroy()
            self.outer_frame.destroy()
            self.done_button.destroy()
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
            subject_information(root)

        def activate_button():

            sub_1 = self.subject_one.get().strip()
            sub_2 = self.subject_two.get().strip()
            sub_3 = self.subject_three.get().strip()
            sub_4 = self.subject_four.get().strip()
            sub_5 = self.subject_five.get().strip()

            if not sub_1:
                messagebox.showerror("ERROR", "Your Are Missing Subject 1")
                return

            if not sub_2:
                messagebox.showerror("ERROR", "Your Are Missing Subject 2")
                return

            if not sub_3:
                messagebox.showerror("ERROR", "Your Are Missing Subject 3")
                return

            if not sub_4:
                messagebox.showerror("ERROR", "Your Are Missing Subject 4")
                return

            if not sub_5:
                messagebox.showerror("ERROR", "Your Are Missing Subject 5")
                return

            else:
                self.summary_button.config(state="normal")

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


        def calculate_summary():

            subject_rows = [
                (self.subject_1_excellence, self.subject_1_merit, self.subject_1_achieved),
                (self.subject_2_excellence, self.subject_2_merit, self.subject_2_achieved),
                (self.subject_3_excellence, self.subject_3_merit, self.subject_3_achieved),
                (self.subject_4_excellence, self.subject_4_merit, self.subject_4_achieved),
                (self.subject_5_excellence, self.subject_5_merit, self.subject_5_achieved),

            ]

            total_score = 0

            for exc_cb, mer_cb, ach_cb in subject_rows:
                exc_val = int(exc_cb.get() if exc_cb.get() else 0)
                mer_val = int(mer_cb.get() if mer_cb.get() else 0)
                ach_val = int(ach_cb.get() if ach_cb.get() else 0)

                total_score += (exc_val * 4) + (mer_val * 3) + (ach_val * 2)

            def delete_summary():
                self.summary_frame.destroy()
                self.summary_label.destroy()
                self.delete_button.destroy()

                self.summary_button.config(state="disabled")

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

                #total_score = 0

            self.exit_button.config(state="disabled")

            self.summary_frame = Frame(parent, borderwidth=3, relief="solid", height=650, width=1000, bg="Grey")
            self.summary_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.summary_label = Label(self.summary_frame, text=f"Your Rank Score is:",
                                       font=("Helvitica", 50), bg="Grey", fg="White")
            self.summary_label.place(relx=0.5, rely=0.35, anchor=CENTER)

            self.value_label = Label(self.summary_frame, text=f"{total_score}", font=("helvitica", 80, "bold"), bg="Grey", fg="White")
            self.value_label.place(relx=0.5, rely=0.6, anchor=CENTER)

            exit_image = Image.open("red_x.png")
            exit_image = exit_image.resize((115, 128))
            self.exit_image_tk = ImageTk.PhotoImage(exit_image)

            self.delete_button = Button(self.summary_frame,
                                        command=delete_summary, image=self.exit_image_tk, cursor="hand2", background="Grey", relief="flat")
            self.delete_button.place(x=0, y=0, rely=0.13, relx=0.93, anchor=CENTER)
            self.delete_button.image = self.exit_image_tk


        self.main_bg = Image.open("rank_calculator.png")
        self.resized_image = self.main_bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)
        self.my_label = Label(parent, image=self.bg)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1,relheight=1)

        self.exit_button = Button(parent, text="EXIT", height=2, width=15, font=("Helvitica", 20),
                                  activebackground="#a3a3a3", command=message_exit)
        self.exit_button.place(relx=1, rely=1, x=-20, y=-5, anchor="se")

        self.home_button = Button(parent, text="Home", height=2, width=17, font=("Helvitica", 20),
                                  activebackground="#a3a3a3", command=home_back)
        self.home_button.place(x=0, y=0, relx=0.189, rely=0.15, anchor='w')

        self.rank_calc_button = Button(parent, text="Rank Score Calculator", height=2, width=17, font=("Helvitica", 20),
                                activebackground="#a3a3a3")
        self.rank_calc_button.place(x=0, y=0, relx=0.364, rely=0.15, anchor='w')

        self.information_button = Button(parent, text="Subject Information", height=2, width=17, font=("Helvitica", 20),
                                         activebackground="#a3a3a3", command=to_subject)
        self.information_button.place(x=0, y=0, relx=0.608, rely=0.15, anchor=CENTER)

        self.help_button = Button(parent, text="Help", height=2, width=17, font=("Helvitica", 20),
                                         activebackground="#a3a3a3")
        self.help_button.place(x=0, y=0, relx=0.850, rely=0.15, anchor='e')



        self.outer_frame = Frame(parent, height=130, width=1300, bg="#52005b")
        self.outer_frame.pack_propagate(False)
        self.outer_frame.place(x=0, y=5, relx=0.5, rely=0.96, anchor='s')

        self.done_button = Button(self.outer_frame, text="DONE", height=4, width=20, font=("Helvitica", 20),
                                  activebackground="#a3a3a3", command=activate_button)
        self.done_button.place(x=10, y=-10, relx=0, rely=0.5, anchor="w")

        self.summary_button = Button(self.outer_frame, text="SUMMARY", height=4, width=20, font=("Helvitica", 20),
                                     activebackground="#a3a3a3", command=calculate_summary)
        self.summary_button.place(x=10, y=-10, relx=1.0, rely=0.5, anchor="e")
        self.summary_button.config(state='disabled')


        #Subject drop-down menus:
        subjects = ['English', 'Maths', 'Science', 'History', 'Computer Science']
        self.subject_one = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_one.place(x=0, y=0, rely=0.440, relx=0.280, anchor=CENTER)

        self.subject_two = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_two.place(x=0, y=0, rely=0.505, relx=0.280, anchor=CENTER)

        self.subject_three = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_three.place(x=0, y=0, rely=0.565, relx=0.280, anchor=CENTER)

        self.subject_four = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_four.place(x=0, y=0, rely=0.625, relx=0.280, anchor=CENTER)

        self.subject_five = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_five.place(x=0, y=0, rely=0.690, relx=0.280, anchor=CENTER)


        #Subject 1 Credits:
        credits_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                            '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                            '20', '21', '22', '23', '24']
        self.subject_1_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                               state='readonly', justify="center")
        self.subject_1_excellence.place(x=0, y=0, rely=0.440, relx=0.435, anchor=CENTER)

        self.subject_1_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_1_merit.place(x=0, y=0, rely=0.440, relx=0.545, anchor=CENTER)

        self.subject_1_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_1_achieved.place(x=0, y=0, rely=0.440, relx=0.659, anchor=CENTER)


        #Subject 2 Credits:
        self.subject_2_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_2_excellence.place(x=0, y=0, rely=0.505, relx=0.435, anchor=CENTER)

        self.subject_2_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_2_merit.place(x=0, y=0, rely=0.505, relx=0.545, anchor=CENTER)

        self.subject_2_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_2_achieved.place(x=0, y=0, rely=0.505, relx=0.659, anchor=CENTER)


        #Subject 3 Credits:
        self.subject_3_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_3_excellence.place(x=0, y=0, rely=0.565, relx=0.435, anchor=CENTER)

        self.subject_3_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_3_merit.place(x=0, y=0, rely=0.565, relx=0.545, anchor=CENTER)

        self.subject_3_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_3_achieved.place(x=0, y=0, rely=0.565, relx=0.659, anchor=CENTER)

        #Subject 4 Credits:
        self.subject_4_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_4_excellence.place(x=0, y=0, rely=0.630, relx=0.435, anchor=CENTER)

        self.subject_4_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                            values=credits_num,
                                            state='readonly', justify="center")
        self.subject_4_merit.place(x=0, y=0, rely=0.630, relx=0.545, anchor=CENTER)

        self.subject_4_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                               values=credits_num,
                                               state='readonly', justify="center")
        self.subject_4_achieved.place(x=0, y=0, rely=0.630, relx=0.659, anchor=CENTER)


        #Subject 5 Credits:
        self.subject_5_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_5_excellence.place(x=0, y=0, rely=0.690, relx=0.435, anchor=CENTER)

        self.subject_5_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                            values=credits_num,
                                            state='readonly', justify="center")
        self.subject_5_merit.place(x=0, y=0, rely=0.690, relx=0.545, anchor=CENTER)

        self.subject_5_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                               values=credits_num,
                                               state='readonly',
                                               justify="center")
        self.subject_5_achieved.place(x=0, y=0, rely=0.690, relx=0.659, anchor=CENTER)

        self.total_credits_1 = Entry(parent, width=10, font=("Helvitica", 20), state='readonly', justify="center")
        self.total_credits_1.place(x=0, y=0, rely=0.440, relx=0.769, anchor=CENTER)

        self.total_credits_2 = Entry(parent, width=10, font=("Helvitica", 20), state='readonly', justify="center")
        self.total_credits_2.place(x=0, y=0, rely=0.505, relx=0.769, anchor=CENTER)

        self.total_credits_3 = Entry(parent, width=10, font=("Helvitica", 20), state='readonly', justify="center")
        self.total_credits_3.place(x=0, y=0, rely=0.565, relx=0.769, anchor=CENTER)

        self.total_credits_4 = Entry(parent, width=10, font=("Helvitica", 20), state='readonly', justify="center")
        self.total_credits_4.place(x=0, y=0, rely=0.630, relx=0.769, anchor=CENTER)

        self.total_credits_5 = Entry(parent, width=10, font=("Helvitica", 20), state='readonly', justify="center")
        self.total_credits_5.place(x=0, y=0, rely=0.690, relx=0.769, anchor=CENTER)


class subject_information:
   def __init__(self, parent):

        def message_exit():

            self.exit_button.config(state="disabled")

            self.popup_frame = Frame(parent, borderwidth=3, relief="solid", height=500, width=1200, bg="Grey")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.text_label = Label(self.popup_frame, text="PLEASE CONFIRM YOUR EXIT", font=("Helvitica", 50),
                                    bg="Grey", fg="White")
            self.text_label.place(relx=0.5, rely=0.25, anchor=CENTER)

            self.yes_button = Button(self.popup_frame, height=5, width=20, text="YES", font=("Helvitica", 20),
                                     bg="Dark Green", fg="White", command=proceed_destroy)
            self.yes_button.place(x=0, y=0, relx=0.1, rely=0.5)

            self.no_button = Button(self.popup_frame, height=5, width=20, text="NO", font=("Helvitica", 20), bg="Red",
                                    fg="White", command=cancel_popup)
            self.no_button.place(x=0, y=0, relx=0.65, rely=0.5)

        def back_home():

            self.my_label.destroy()
            self.exit_button.destroy()
            self.home_button.destroy()
            self.rank_calc_button.destroy()
            self.information_button.destroy()
            self.help_button.destroy()
            self.subject.destroy()
            self.done_button.destroy()
            Loginpage(root)


        def proceed_destroy():
            root.destroy()

        def cancel_popup():
            self.popup_frame.destroy()
            self.yes_button.destroy()
            self.no_button.destroy()
            self.exit_button.config(state="normal")
            return

        def to_rank():
            self.home_button.destroy()
            self.rank_calc_button.destroy()
            self.information_button.destroy()
            self.help_button.destroy()
            self.my_label.destroy()
            self.exit_button.destroy()
            Rankcalculator(root)

        def subject_selected():

            self.description_page = Frame(parent, borderwidth=3, relief="solid", height=500, width=1200, bg="Grey")
            self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            if self.subject == 'English':

                self.text_label = Label(self.description_page, text="The subject", font=("Helvitica", 50),
                                    bg="Grey", fg="White")
                self.text_label.place(relx=0.5, rely=0.35, anchor=CENTER)

            if self.subject == 'Computer Science':

                self.text_label = Label(self.description_page, text="The subject", font=("Helvitica", 50),
                                        bg="Grey", fg="White")
                self.text_label.place(relx=0.5, rely=0.35, anchor=CENTER)



        self.main_bg = Image.open("subjects.png")
        self.resized_image = self.main_bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)
        self.my_label = Label(parent, image=self.bg)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image = self.bg
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.exit_button = Button(parent, text="EXIT", height=2, width=15, font=("Helvitica", 20),
                                  activebackground="#a3a3a3", command=message_exit)
        self.exit_button.place(relx=1, rely=1, x=-20, y=-5, anchor="se")

        self.home_button = Button(parent, text="Home", height=2, width=17, font=("Helvitica", 20),
                                  activebackground="#a3a3a3", command=back_home)
        self.home_button.place(x=0, y=0, relx=0.189, rely=0.15, anchor='w')

        self.rank_calc_button = Button(parent, text="Rank Score Calculator", height=2, width=17, font=("Helvitica", 20),
                                       activebackground="#a3a3a3", command=to_rank)
        self.rank_calc_button.place(x=0, y=0, relx=0.364, rely=0.15, anchor='w')

        self.information_button = Button(parent, text="Subject Information", height=2, width=17, font=("Helvitica", 20),
                                         activebackground="#a3a3a3")
        self.information_button.place(x=0, y=0, relx=0.608, rely=0.15, anchor=CENTER)

        self.help_button = Button(parent, text="Help", height=2, width=17, font=("Helvitica", 20),
                                  activebackground="#a3a3a3")
        self.help_button.place(x=0, y=0, relx=0.850, rely=0.15, anchor='e')

        subject_choice = ['English', 'Science', 'Maths', 'Computer Science']
        self.subject = ttk.Combobox(parent, width=55, height=150, font=("Helvitica", 35),
                                    values=subject_choice, state="readonly", justify="center")
        self.subject.place(x=0, y=0, relheight=0.1, relx=0.5, rely=0.620, anchor=CENTER)

        self.done_button = Button(parent, text="DONE", height=2, width=17, font=("Helvitica", 20), activebackground="#a3a3a3", command=subject_selected)
        self.done_button.place(x=0, y=0, relx=0.5, rely=0.725, anchor=CENTER)



app = Loginpage(root)

root.mainloop()
