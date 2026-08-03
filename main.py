
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

        def go_button():
            self.my_label.destroy()
            self.my_frame.destroy()
            self.button_go.destroy()
            self.button_exit.destroy()
            Rankcalculator(root)


        self.bg = Image.open("home_bright.png")
        self.resized_image = self.bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.my_frame = Frame(parent, height=300, width=1000, bg="#792782")
        self.my_frame.place(x=0, y=0, relx=0.5, rely=0.6, anchor=CENTER)

        self.button_go = Button(self.my_frame, text="START HERE", height=2, width=16, font=("Helvitica", 20),
                                activebackground="#792782", command=go_button)
        self.button_go.grid(row=2, column=2, pady=20, columnspan=2)

        self.button_exit = Button(parent, text="EXIT", height=2, width=15, font=("Helvitica", 20),
                                  activebackground="#792782", command=message_exit)
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

        def to_subject():

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


        def help_button():

            def delete_popup():
                self.popup_frame.destroy()
                self.help_text.destroy()
                self.delete_button.destroy()
                self.exit_button.config(state="normal")


            self.exit_button.config(state="disabled")

            self.popup_frame = Frame(parent, borderwidth=5, relief="solid", height=650, width=1300, bg="#792782")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.help_text = Label(self.popup_frame, text="\nCurious to discover the progress towards entry into University?"
                                                          " \nBy using the rank score calculator you are able to efficiently and effectively calculate your total rank score"
                                                          " \nfrom your total accumulated credits throughout your five subjects."
                                                          "\n\nTo operate the calculator, please select all five subjects you have taken throughout the year"
                                                          "\nbefore entering all achieved, merit and excellence credits."
                                                          "\nYou must enter in each subject, even if you have not acquired any credits throughout the year."
                                                          "\n\nOnce you have entered in all necessary values, select the “DONE” button. "
                                                          "\nThis will activate the ‘SUMMARY’, permitting you to see your total rank score without any interruptions."
                                                          "\n\nOnce you finished, select the ‘X’ button where you will be taken back to the original screen.", font=("Helvitica", 16), bg="#792782", fg="white",
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


        self.main_bg = Image.open("bright_cal.png")
        self.resized_image = self.main_bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)
        self.my_label = Label(parent, image=self.bg)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image=self.bg
        self.my_label.place(x=0, y=0, relwidth=1,relheight=1)

        self.exit_button = Button(parent, text="EXIT", height=2, width=15, font=("Helvitica", 20),
                                  activebackground="Grey", command=message_exit)
        self.exit_button.place(relx=1, rely=1, x=-20, y=-5, anchor="se")

        self.rank_calc_button = Button(parent, text="Rank Score Calculator", height=2, width=17, font=("Helvitica", 20),
                                activebackground="#792782")
        self.rank_calc_button.place(x=0, y=0, relx=0.330, rely=0.15, anchor='w')

        self.information_button = Button(parent, text="Subject Information", height=2, width=17, font=("Helvitica", 20),
                                         activebackground="#792782", command=to_subject)
        self.information_button.place(x=0, y=0, relx=0.620, rely=0.15, anchor=CENTER)



        help_image = Image.open("Your4.png")
        help_image = help_image.resize((180, 180), Image.LANCZOS)
        self.help_image_tk = ImageTk.PhotoImage(help_image)

        self.help_button = Button(parent, image=self.help_image_tk, command=help_button, cursor="hand2", background="#792782", relief="flat")
        self.help_button.place(x=0, y=0, relx=0.940, rely=0.11, anchor=CENTER)



        self.outer_frame = Frame(parent, height=130, width=1300, bg="#792782")
        self.outer_frame.pack_propagate(False)
        self.outer_frame.place(x=0, y=5, relx=0.5, rely=0.96, anchor='s')

        self.done_button = Button(self.outer_frame, text="DONE", height=4, width=20, font=("Helvitica", 20),
                                  activebackground="#792782", command=activate_button)
        self.done_button.place(x=10, y=-10, relx=0, rely=0.5, anchor="w")

        self.summary_button = Button(self.outer_frame, text="SUMMARY", height=4, width=20, font=("Helvitica", 20),
                                     activebackground="#792782", command=calculate_summary)
        self.summary_button.place(x=10, y=-10, relx=1.0, rely=0.5, anchor="e")
        self.summary_button.config(state='disabled')


        #Subject drop-down menus:
        subjects = ['English', 'Maths', 'Science', 'History', 'Computer Science']
        self.subject_one = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_one.place(x=0, y=0, rely=0.440, relx=0.335, anchor=CENTER)

        self.subject_two = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_two.place(x=0, y=0, rely=0.505, relx=0.335, anchor=CENTER)

        self.subject_three = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_three.place(x=0, y=0, rely=0.565, relx=0.335, anchor=CENTER)

        self.subject_four = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_four.place(x=0, y=0, rely=0.625, relx=0.335, anchor=CENTER)

        self.subject_five = ttk.Combobox(parent, font=("Helvitica", 20), values=subjects, state='readonly', justify="center")
        self.subject_five.place(x=0, y=0, rely=0.690, relx=0.335, anchor=CENTER)


        #Subject 1 Credits:
        credits_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                            '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                            '20', '21', '22', '23', '24']
        self.subject_1_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                               state='readonly', justify="center")
        self.subject_1_excellence.place(x=0, y=0, rely=0.440, relx=0.490, anchor=CENTER)

        self.subject_1_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_1_merit.place(x=0, y=0, rely=0.440, relx=0.605, anchor=CENTER)

        self.subject_1_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_1_achieved.place(x=0, y=0, rely=0.440, relx=0.712, anchor=CENTER)


        #Subject 2 Credits:
        self.subject_2_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_2_excellence.place(x=0, y=0, rely=0.505, relx=0.490, anchor=CENTER)

        self.subject_2_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_2_merit.place(x=0, y=0, rely=0.505, relx=0.605, anchor=CENTER)

        self.subject_2_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_2_achieved.place(x=0, y=0, rely=0.505, relx=0.712, anchor=CENTER)


        #Subject 3 Credits:
        self.subject_3_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20), values=credits_num,
                                            state='readonly', justify="center")
        self.subject_3_excellence.place(x=0, y=0, rely=0.565, relx=0.490, anchor=CENTER)

        self.subject_3_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_3_merit.place(x=0, y=0, rely=0.565, relx=0.605, anchor=CENTER)

        self.subject_3_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_3_achieved.place(x=0, y=0, rely=0.565, relx=0.712, anchor=CENTER)

        #Subject 4 Credits:
        self.subject_4_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_4_excellence.place(x=0, y=0, rely=0.630, relx=0.490, anchor=CENTER)

        self.subject_4_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                            values=credits_num,
                                            state='readonly', justify="center")
        self.subject_4_merit.place(x=0, y=0, rely=0.630, relx=0.605, anchor=CENTER)

        self.subject_4_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                               values=credits_num,
                                               state='readonly', justify="center")
        self.subject_4_achieved.place(x=0, y=0, rely=0.630, relx=0.712, anchor=CENTER)


        #Subject 5 Credits:
        self.subject_5_excellence = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                                 values=credits_num,
                                                 state='readonly', justify="center")
        self.subject_5_excellence.place(x=0, y=0, rely=0.694, relx=0.490, anchor=CENTER)

        self.subject_5_merit = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                            values=credits_num,
                                            state='readonly', justify="center")
        self.subject_5_merit.place(x=0, y=0, rely=0.694, relx=0.605, anchor=CENTER)

        self.subject_5_achieved = ttk.Combobox(parent, width=10, height=10, font=("Helvitica", 20),
                                               values=credits_num,
                                               state='readonly',
                                               justify="center")
        self.subject_5_achieved.place(x=0, y=0, rely=0.694, relx=0.712, anchor=CENTER)


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
            Rankcalculator(root)

        def subject_selected():

            self.exit_button.config(state="disabled")

            selected_subject = self.subject.get()

            self.description_page = Frame(parent, borderwidth=3, relief="solid", height=850, width=850, bg="white")
            self.description_page.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            exit_image = Image.open("red_x.png")
            exit_image = exit_image.resize((115, 128))
            self.exit_image_tk = ImageTk.PhotoImage(exit_image)

            def delete_popup():
                self.description_page.destroy()
                self.english_label.destroy()
                self.vis_english_label.destroy()
                self.exit_button.config(state="normal")

            if selected_subject == 'Written English':
                eng_image = Image.open("writ_eng.png")
                eng_image = eng_image.resize((600, 800), Image.LANCZOS)
                self.eng_image_tk = ImageTk.PhotoImage(eng_image)

                self.english_label = Label(parent, image=self.eng_image_tk, background="white")
                self.english_label.image = self.eng_image_tk
                self.english_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

            if selected_subject == 'Visual English':
                vis_eng_image = Image.open("vis_eng.png")
                vis_eng_image = vis_eng_image.resize((600, 800), Image.LANCZOS)
                self.vis_eng_image_tk = ImageTk.PhotoImage(vis_eng_image)

                self.vis_english_label = Label(parent, image=self.vis_eng_image_tk, background="white")
                self.vis_english_label.image = self.eng_image_tk
                self.vis_english_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

            if selected_subject == 'Music Studies':
                mus_image = Image.open("mus.png")
                mus_image = mus_image.resize((600, 800), Image.LANCZOS)
                self.mus_image_tk = ImageTk.PhotoImage(mus_image)

                self.mus_label = Label(parent, image=self.mus_image_tk, background="white")
                self.mus_label.image = self.eng_image_tk
                self.mus_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                self.delete_button = Button(self.description_page,
                                            command=delete_popup, image=self.exit_image_tk, cursor="hand2",
                                            background="white", relief="flat")
                self.delete_button.place(x=0, y=0, rely=0.13, relx=0.925, anchor=CENTER)
                self.delete_button.image = self.exit_image_tk

        def help_button():

            def delete_popup():
                self.popup_frame.destroy()
                self.delete_button.destroy()
                self.exit_button.config(state="normal")


            self.exit_button.config(state="disabled")

            self.popup_frame = Frame(parent, borderwidth=5, relief="solid", height=650, width=1300, bg="#792782")
            self.popup_frame.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)

            self.help_text = Label(self.popup_frame,
                                   text="\nThe Subject Information page allows you to freely browse various level 3 subjects "
                                        "\nto understand what each subject has to offer. "
                                        "\n\nSimply by entering the subject of your choice and selecting the ‘ENTER’ button, "
                                        "\nyou are given a brief description of the subject, including what it might offer to you as a student. "
                                        "\n\nTo exit the subject, simply select the ‘X’ button and you will be taken back to the original page, "
                                        "\nfree to choose a new subject if wanted.", font=("Helvitica", 18), bg="#792782", fg="white",
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



        self.main_bg = Image.open("bright_info.png")
        self.resized_image = self.main_bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.resized_image)
        self.my_label = Label(parent, image=self.bg)

        self.my_label = Label(parent, image=self.bg)
        self.my_label.image = self.bg
        self.my_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.exit_button = Button(parent, text="EXIT", height=2, width=15, font=("Helvitica", 20),
                                  activebackground="#792782", command=message_exit)
        self.exit_button.place(relx=1, rely=1, x=-20, y=-5, anchor="se")

        self.rank_calc_button = Button(parent, text="Rank Score Calculator", height=2, width=17, font=("Helvitica", 20),
                                       activebackground="#792782", command=to_rank)
        self.rank_calc_button.place(x=0, y=0, relx=0.330, rely=0.15, anchor='w')

        self.information_button = Button(parent, text="Subject Information", height=2, width=17, font=("Helvitica", 20),
                                         activebackground="#792782")
        self.information_button.place(x=0, y=0, relx=0.620, rely=0.15, anchor=CENTER)


        help_image = Image.open("Your4.png")
        help_image = help_image.resize((180, 180), Image.LANCZOS)
        self.help_image_tk = ImageTk.PhotoImage(help_image)

        self.help_button = Button(parent, image=self.help_image_tk, command=help_button, cursor="hand2",
                                  background="#792782", relief="flat")
        self.help_button.place(x=0, y=0, relx=0.940, rely=0.11, anchor=CENTER)


        subject_choice = ['Written English', 'Visual English', 'Maths', 'Music Studies']
        self.subject = ttk.Combobox(parent, width=55, height=150, font=("Helvitica", 35),
                                    values=subject_choice, state="readonly", justify="center")
        self.subject.place(x=0, y=0, relheight=0.1, relx=0.5, rely=0.620, anchor=CENTER)

        self.done_button = Button(parent, text="DONE", height=2, width=17, font=("Helvitica", 20), activebackground="#792782", command=subject_selected)
        self.done_button.place(x=0, y=0, relx=0.5, rely=0.725, anchor=CENTER)



app = Loginpage(root)

root.mainloop()
