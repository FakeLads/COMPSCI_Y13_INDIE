# Imports tkinter features
from tkinter import *

# Imports the messagebox function from the tkinter library
from tkinter import messagebox

# Imports PIL/Pillow
from PIL import Image, ImageTk

from tkinter import PhotoImage

import matplotlib.pyplot as plt

# Imports random function
import random

# A list that stores the user's username
names_list = []

# Questions that were asked
asked = []

# A list that holds the user's results from the Quiz
quiz_results = []

# Globalises the use if the 'question_answers' list
global question_answers

# List of my questions and possible answers
question_answers = {
    1: ["What definition fits this language feature: ‘Alluring’",
        'Consonant sounds in two or more neighbouring words',
        'An indirect reference to an event, place, or person',
        'Exaggerating something using rhetorical language',
        'Something or someone that very attractive'
        , 4],
    2: ["What definition fits this language feature: ‘Connotations’",
        'Words that describe a sound',
        'A positive or negative word suggested by a word or thing',
        'Two concepts that contradict one another',
        'A figure of speech',
        2],
    3: ["The arrangement of words, phrases, and clauses in a sentence to make them sound and look meaningful.",
        'Syntax',
        'Allegory',
        'Simile',
        'Juxtaposition',
        1],
    4: ["An indirect/subtle reference to an event, place, or person.",
        'Tone',
        'Colloquialism',
        'Allusion',
        'Repetition',
        3],
    5: ["What definition fits this language feature: ‘Oxymoron’",
        'A figure of speech that juxtaposes concepts with opposite meanings to create a paradoxical phrase',
        'Repeating something that has already been said or written',
        'Visually descriptive language that creates a scene in the mind of the reader',
        'A phrase or opinion that is often overused and betrays a lack of original thought',
        1],
    6: ["Using a similar grammatical structure for words within a sentence, creating a sense of rhythm.",
        'Colloquialism',
        'Extended Metaphor',
        'Personification',
        'Parallelism',
        4],
    7: ["What definition fits this language feature: 'Metaphor'",
        'Human characteristics given to something that is non-human, like animals, objects, ideas',
        'The occurrence of the same letter or sound at the beginning words closely connected',
        'A figure of speech in which a person or thing is compared to something different',
        'A word that describes something with similar characteristics',
        3],
    8: ["A play on words that involve words that have similar sounds, with different meanings",
        'Slang',
        'Pun',
        'Extended Metaphor',
        'Personification',
        2],
    9: ["What definition fits this language feature: 'Extended Metaphor'",
        'Human attributes given to something that is non-human, like animals, objects, or ideas',
        'Compares two things that are not alike over the course of multiple lines',
        'A phrase or opinion that is often overused and betrays a lack of original thought',
        'Words that describe a sound, like explosions or footsteps',
        2],
    10: ["Words that intend to imitate the sound they describe",
         'Onomatopoeia',
         'Simile',
         'Hyperbole',
         'Parallelism',
         1],

}


# The purpose of the randomiser function is to select an unasked question from the question_answers list for the user to answer
def randomiser():
    global qnum # Globalises the use of the variable qnum
    global asked # Globalises the use of the 'asked' list

    remaining = [num for num in question_answers if num not in asked] # Inspects all the 'question_answers' list to find questions that have not been asked and then puts them in a list to be used
    if remaining: # If there are questions remaining
        qnum = random.choice(remaining) # Select a random question from the list with questions and places them in the global qnum variable
        asked.append(qnum) # Ensures the same question can't be asked twice
    else: # If there are no questions remaining
        qnum = None # qnum is equal to None


# A class that hosts all the code for my Quizstarter page
class Quizstarter:
    def __init__(self, main_canvas, bg_image_canvas_id):

        # Main canvas variable
        self.main_canvas = main_canvas

        # Creates the ID for the canvas image to identify what objects or elements have been drawn onto it, making it possible to delete items
        self.bg_image_canvas_id = bg_image_canvas_id


        self.canvas_width = main_canvas.winfo_width()
        self.canvas_height = main_canvas.winfo_height()

        # Insures that if the width and height of the image equate to 1, it will change their
        if self.canvas_width == 1:
            self.canvas_width = 1400
        if self.canvas_height == 1:
            self.canvas_height = 800

        # An inner frame that's used to hold widgets in a more precise location
        self.inner_frame = Frame(main_canvas, bg="#1174db", padx=40, pady=100,)

        # Finds and assigns the middle x and y values of the canva by splitting the value of overall width and height
        self.center_x = self.canvas_width / 2
        self.center_y = self.canvas_height / 2

        # Creates canvas widget
        self.frame_window = main_canvas.create_window(self.center_x, self.center_y, window=self.inner_frame,
                                                      anchor="center")

        # Columnconfigure(s) allow me to set a size of columns, as well as how many columns I would like
        self.inner_frame.columnconfigure(0, weight=1)
        self.inner_frame.columnconfigure(1, weight=3)
        self.inner_frame.columnconfigure(2, weight=1)

        # A for loop crates 4 row with weights of 1
        for i in range(4):
            self.inner_frame.rowconfigure(i, weight=1)

        # Heading label - Holds main title
        self.home_label = Label(self.inner_frame, text="English Language Features Quiz",
                                font=("Helvetica", "50", "bold"),
                                bg="#02a298", fg="black", bd=3, relief="solid")
        self.home_label.grid(row=0, column=1, sticky="nsew", pady=10) # Grid geometry manager for the main label

        # Username prompt
        self.user_label = Label(self.inner_frame, text="Please enter your username",
                                font=("Helvetica", "30"),
                                bg="#02a298", fg="black", bd=3, relief="solid", padx=20)
        self.user_label.grid(row=1, column=1,) # Grid geometry manager for the second label

        # Entry box for users to enter their usernames
        self.entry = Entry(self.inner_frame, width=40, bg="White", fg="Black", font=("Helvetica", "24"), )
        self.entry.grid(row=2, column=1, columnspan=1, pady=20, sticky="nsew") # Geometry manager for the entry label
        self.entry.insert(0, "Enter your username:") # Inserts the string text into the entry label

        # Continue button
        self.continue_button = Button(self.inner_frame, text="Continue", font=("Helvetica", "20", "bold"),
                                      bg="White", fg="Black", command=self.name_collection, bd=3, relief="groove",
                                      highlightthickness=0, pady=20, )
        self.continue_button.grid(row=3, column=1, columnspan=1, pady=0, padx=0, sticky="nsew") # Grid geometry manager used for the continue button

    # This is a defined method that collects the user's username, while also destroying the Quizstater root
    def name_collection(self):
        name = self.entry.get().strip()  # The variable name is equal to what the user entered into the 'self.entry' box

        if not name:
            messagebox.showerror("ERROR",
                                 "Please enter a username")  # If the user does not enter a username an error message will appear informing them to enter a username
        elif len(name) > 10:
            messagebox.showerror("ERROR", "Username must be 10 characters or less") # If the user enters a username that is longer 10 characters an error prompt will appear
        else:
            names_list.append(name)  # This line appends/places the user's name into the names_list to be saved
            self.main_canvas.delete(self.bg_image_canvas_id)  # This deletes the ID for canvas
            self.main_canvas.delete(self.frame_window)  # This deletes the components on the canvas
            self.main_canvas.destroy()  # This ensures that the canvas background is destroyed
            Quiz(root) # Opens the Quiz class


# The Quiz class is the page that hosts the quiz questions
class Quiz:
    def __init__(self, main):
        self.background_color = "#004b99" # Assigns the variable 'self.background_color' to a specific shade of brown

        self.score = 0 # Starting user point score/value
        self.main_window = main # Assigns 'self.main_window' to the parent root of the class: 'main'

        self.frame = Frame(main, bg=self.background_color, padx=100, pady=100) # Creates the main frame used in my quiz class
        self.frame.pack(fill=BOTH, expand=True) # Packs the frame so it can expand the whole window

        # Column configurations allow me to create and dictate the size of my columns as well as how many there are
        self.frame.columnconfigure(0, weight=1) # Both columns have weight of one, meaning that the screen will be split 50 to 50 or two halves
        self.frame.columnconfigure(1, weight=1)

        # Row configurations allow me to create dictate the size of my rows as well as how many there are
        self.frame.rowconfigure(0, weight=0) # The first row's weight is set to 0 as it does not hold many elements
        self.frame.rowconfigure(1, weight=1) # The rest of the index rows have a weight of 1 as they hold large button widgets and lables
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)

        # Displays the user's current score towards the top-left of the screen, the scores changes depending if the user has answered a question correctly or not
        self.display_score = Label(self.frame, text=f"Score: {self.score}", font=("Helvetica", "20", "bold"), # The 'f' string in the text is used to help display the user's score, grabbing the current value of the score and displaying it in the text label
                                   bg="#a532ff", fg="white", bd=3, relief="solid", padx=20) # The bd widget option is used to create boarder lines, with it controlling the thickness of the line. The relief option helps to design the look of the boarder, I have chosen solid.
        self.display_score.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Displays the question the user is tasked with answering
        self.question_label = Label(self.frame, text="", font=("Helvetica", "24", "bold"),
                                    bg="#1174db", wraplength=600, bd=4, relief="solid") # The use of 'wraplength' is to ensure that text does not overlap or underlap beyond the label, forcing the text to go to the next line if too large
        self.question_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Displays the first button option
        self.answer_button1 = Button(self.frame, text="", font=("Helvetica", "20"), # The reason for the text being blank is that later in my code, I will use a 'configure' function to add the first answer
                                     command=lambda: self.check_answer(1), wraplength=300) # The lambda command uses the defined function: 'self.check_answer' to check whether the first index/option is the correct answer
        self.answer_button1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        # Displays the second button option
        self.answer_button2 = Button(self.frame, text="", font=("Helvetica", "20"),
                                     command=lambda: self.check_answer(2), wraplength=300) # The lambda command uses the defined function: 'self.check_answer' to check whether the second index/option is the correct answer
        self.answer_button2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        # Displayed the third button option
        self.answer_button3 = Button(self.frame, text="", font=("Helvetica", "20"),
                                     command=lambda: self.check_answer(3), wraplength=300) # The lambda command uses the defined function: 'self.check_answer' to check whether the third index/option is the correct answer
        self.answer_button3.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        # Displays the fourth button option
        self.answer_button4 = Button(self.frame, text="", font=("Helvetica", "20"),
                                     command=lambda: self.check_answer(4), wraplength=300) # The lambda command uses the defined function: 'self.check_answer' to check whether the fourth index/option is the correct answer
        self.answer_button4.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        # Displays the continue button used to proceed to the next question after being answered and to the next page once the quiz is completed
        self.continue_button = Button(self.frame, text="Continue", font=("Helvetica", "20", "bold"),
                                      # When the button is clicked it triggers the 'next_question' function which takes the user to the next question if not completed or to the next page if done
                                      command=self.next_question, state=DISABLED) # When the continue button is first displayed it is disabled for the purpose of ensuring the user selects answer before proceeding, if the user was to just press continue there would be an error

        self.continue_button.grid(row=4, column=0, columnspan=2, padx=10, pady=15, sticky="nsew")

        self.next_question() # Informs tkinter to display the first question, filling in the label and button widgets with text. This is different from the 'Continue' button as the purpose of the widget is to take the user to next question

    # This defined function: 'check_answer' is used to check if the user's answer is correct incorrect
    def check_answer(self, selected_answer_index):
        global qnum

        correct_answer_index = question_answers[qnum][5] # This means that fifth index in each of the questions is the correct answer

        # This if statement means that if the user's answer is equal to the 5th index/the correct answer, execute the following commands
        if selected_answer_index == correct_answer_index:
            self.score += 1 # If the answer is correct the user's score will go up by one point

            # Displays a label that informs the user that they have gotten the question correct
            self.correct_answer = Label(self.frame, text="Correct! ✓", font=("Helvetica", "20", "bold"), bg="Black",
                                        fg="Light Green") # The text will use a check mark with a green figment and black background to make it eye-catching for the user
            self.correct_answer.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # This else statement means that if the user's answer is not equal to the 5th index/the correct answer, execute the following commands
        else:
            # Displays a label that informs the user that they have gotten the question incorrect
            self.incorrect_answer = Label(self.frame, text=f"Incorrect X \n The Correct answer is: {question_answers[qnum][5]}", # The not only informs the user that they have gotten the question incorrect, it also gives the user the number of the correct answer
                                          font=("Helvetica", "20", "bold"), bg="Black",
                                          fg="Red") # The text will be red with a black background
            self.incorrect_answer.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.display_score.config(text=f"Score: {self.score}/{len(question_answers)}") # This changes the text with in the 'self.display_score' to the user's current score with the amount of questions in total

        self.disable_answer_button() # Disables the buttons so the user does not mistakenly cause an error by clicking an answer button.

        self.continue_button.config(state=NORMAL) # The continue button will become available to interact with

# When the defined function is called, it will disable all answer buttons
    def disable_answer_button(self):
        self.answer_button1.config(state=DISABLED)
        self.answer_button2.config(state=DISABLED)
        self.answer_button3.config(state=DISABLED)
        self.answer_button4.config(state=DISABLED)

# Called at the start of the loop of the Quiz to make it so the user can choose an answer
    def enable_answer_button(self):
        self.answer_button1.config(state=NORMAL)
        self.answer_button2.config(state=NORMAL)
        self.answer_button3.config(state=NORMAL)
        self.answer_button4.config(state=NORMAL)

# The defined function 'next_question' is called it will display the question and question answers within the widgets
    def next_question(self):
        global qnum # Globalises the use of the 'qnum' variable
        global asked # Globalises the use of the 'asked' list
        global root # Globalises the use of the root

        # This if statement is executed if the number of questions asked is greater or equal to the number of questions in the 'question_answers' list
        if len(asked) >= len(question_answers):
            self.show_results() # This calls the defined function show_results if the above statement is true
            return

# If the user gets the question correct they will be presented with the 'Correct!' label that informs the user they got the question right
        if hasattr(self, 'correct_answer') and self.correct_answer:
            self.correct_answer.destroy() # Destroys the label when the continue button is clicked
            self.correct_answer = None # By setting 'self.correct_answer' to None, it cleans up any trace of the label being present, which will help to ensure no errors

# If the user gets the question incorrect they will be informed through the use of a label that they have gotten the question wrong
        if hasattr(self, 'incorrect_answer') and self.incorrect_answer:
            self.incorrect_answer.destroy() # Destroys the label when the continue button is clicked
            self.incorrect_answer = None


        randomiser() # Calls the randomiser function

# Fills Question label and the answer buttons with text from the question_answers list
        self.question_label.config(text=question_answers[qnum][0])
        self.answer_button1.config(text=question_answers[qnum][1])
        self.answer_button2.config(text=question_answers[qnum][2])
        self.answer_button3.config(text=question_answers[qnum][3])
        self.answer_button4.config(text=question_answers[qnum][4])

        self.enable_answer_button() # Called upon the function to enable all the buttons once again for the next question
        self.continue_button.config(state=DISABLED) # This disables the continue button for the next question so users cannot click on it

# When the function is called it will destroy the Quiz frame and take the user to the Results page
    def show_results(self):
        self.frame.destroy() # Destroys the Quiz frame
        global quiz_results # Globalises the use of 'quiz_results'
        self.current_username = names_list[0] #
        quiz_results.append({"username": self.current_username, "score": self.score}) # Assigns the user's username and results to the 'quiz_results' list to be used later in the Results class

        # This executes the Results page. Passing through the parameters of this line of code is the root window as well as the user's quiz results
        Results(self.main_window, quiz_results,)


# Class for Results page
class Results:
    def __init__(self, main, quiz_results):

        # Sets the variable for the background colour
        self.background_color = "#004b99"

        # Sets the variable to the main parent of the Results page
        self.main = main

        # Sets the variable to the user's results list: 'quiz_results'
        self.quiz_results = quiz_results

        # Creates the main frame used to hold components
        self.frame = Frame(main, bg=self.background_color)
        self.frame.pack(fill=BOTH, expand=True) # Expands the page to fit the geometry of window

        self.bg_image_results = Image.open("RPB.png") # Sets 'self.bg_image_results' to the image 'RPB.png'
        self.resized_bg_image_results = self.bg_image_results.resize(
            (self.main.winfo_width(), self.main.winfo_height()), Image.LANCZOS) # Resizes the image to fit the main width and height of the window, while also ensuring the image reaches its highest quality
        self.bg_image_results = ImageTk.PhotoImage(self.resized_bg_image_results) # Converts the PIL/Pillow image into a Photoimage so it can be displayed

        # Creates the main canvas widget to hold image background
        self.bg_canvas_results = Canvas(self.frame, width=self.main.winfo_width(), height=self.main.winfo_height(),
                                        bd=0,
                                        highlightthickness=0)
        self.bg_canvas_results.place(x=0, y=0, relwidth=1, relheight=1) #Places the canvas to the top left of the screen
        self.bg_canvas_results.create_image(0, 0, image=self.bg_image_results, anchor=NW) # Draws the image on the canvas widget

        # The row configurations create one large row in the middle of the window with two smaller ones to the very top and bottom
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=5)
        self.frame.rowconfigure(2, weight=1)

        # The column configurations creates one larger row in the middle of the window, and two smaller ones to the top and bottom
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
        self.frame.columnconfigure(2, weight=1)

        # Displays the heading label that hosts the text: SCORE
        self.label = Label(self.frame, text="SCORE", font=("Helvetica", "40", "bold"), bg=self.background_color)
        self.label.grid(row=0, column=1, padx=10, pady=10, )

        # Creates an inner frame to host label widgets
        self.results_inner_frame = Frame(self.frame, bg="#1174db", bd=5, relief=SOLID)
        self.results_inner_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Row configurations for the inner frame. This is used to provide the labels with a row each with a small gap to the top and bottom of the frame
        self.results_inner_frame.rowconfigure(0, weight=1)
        self.results_inner_frame.rowconfigure(1, weight=1)
        self.results_inner_frame.rowconfigure(2, weight=1)
        self.results_inner_frame.rowconfigure(3, weight=1)
        self.results_inner_frame.rowconfigure(4, weight=1)
        self.results_inner_frame.rowconfigure(5, weight=1)

        # Column configuration for the inner frame. Only two columns with each having a weight of '1'
        self.results_inner_frame.columnconfigure(0, weight=1)
        self.results_inner_frame.columnconfigure(1, weight=1)

        self.result_labels = [] # This list hosts the
        # A 'for' loop that creates four labels to hold the user's results
        for i in range(4):
            self.a_label = Label(self.results_inner_frame, text="", font=("Helvetica", "20", "bold"), bg="Black", wraplength=300) # Displays a label to hold the user's results
            self.a_label.grid(row=i + 1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew") # The 'row=i + 1' is used so that when this loop is executed again, the row values goes up by 1.
            self.result_labels.append(self.a_label)

        #
        self.display_all_results()

        # Displays the 'Menu' button towards the bottom left of the screen. The button allows users to go back to the first page (Quizstarter) to try the quiz again
        self.menu_button = Button(self.frame, text="MENU", font=("Helvetica", "20", "bold"),
                                  command=self.return_home) # The command 'return_home' is the function needed to transport the user back to the Quizstarter page
        self.menu_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Displays the 'Quit' button towards the bottom right of the screen. The button allows users to immediately quit the quiz
        self.quit_button = Button(self.frame, text="QUIT", font=("Helvetica", "20", "bold"),
                                  command=root.destroy) # The command 'root.destroy' deletes the main root, this stops the GUI from running thereby terminating the quiz
        self.quit_button.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    # The defined function 'display_all_results' is used to display the user's most recent results a display to the top label
    def display_all_results(self):
        for i, result in enumerate(reversed(self.quiz_results)): # Gathers the user's results and places them according to the order of the most recent
            if i < len(self.result_labels): # If the index is less than the number of labels available to change the present properties contained within the widget
                self.result_labels[i].config(
                    text=f"{result['username']} \n Score: {result['score']}/{len(question_answers)}") # Displays the user's results. This contains the username and score of the user
            else:
                break # If the previous condition is not true, then the break command will be called to end the loop

        # This 'for' loop is responsible for cleaning up old date from past attempts
        for i in range(len(self.quiz_results), len(self.result_labels)):
            self.result_labels[i].config(text="")

    # The defined function 'return_home' is used to transport the user back to the Quizstarter page
    def return_home(self):
        self.frame.destroy() # Destroys the Result class frame
        global asked # Globalises the use of the 'asked' list
        global names_list # Globalises the use of the 'names_list' list
        asked = [] # This list is re-used to reset the questions that have been asked so the user can play again
        names_list = [] # This list is also re-used to reset username so it is carried into the next attempt

        self.new_canvas = Canvas(self.main, width=1400, height=800) # Creates a new canvas to host the background image
        self.new_canvas.pack(fill=BOTH, expand=True) # Expands the canvas to fit the entire screen

        self.original_bg_image = Image.open("PBG.png") # Assigns the variable to 'PBG.png' image
        self.resized_bg_image = self.original_bg_image.resize((1400, 800), Image.LANCZOS) # Resizes the image to fit the window and ensures the image reaches peak quality
        self.bg_image_tk = ImageTk.PhotoImage(self.resized_bg_image) # Converts the image from a PIL/Pillow image, to a Photoimage so it can be displayed
        self.main.bg_image_tk = self.bg_image_tk # Stores a reference to the PhotoImage so it is not garbage collected

        self.bg_canvas_item_id = self.new_canvas.create_image(0, 0, image=self.bg_image_tk, anchor="nw") # Places the photoimage to the top left of the screen and allows to be easily edited or deleted if need be

        Quizstarter(self.new_canvas, bg_canvas_item_id) # Executes the Quizstarter page, with the canvas variable and ID passing through the parentheses

# The __main__ method. It is responsible for setting up my entire GUI
if __name__ == "__main__":
    root = Tk() # 'root' is set to tk
    root.title("English_Quiz")  # Creates the title for the Quiz
    root.geometry("1400x800")  # Sets the geometry for the main window

    canvas = Canvas(root, width=1400, height=800) # Creates a canvas widget within the main root
    canvas.pack(fill=BOTH, expand=True) # Expands the canvas to fill the entire screen

    original_bg_image = Image.open("PBG.png") # Sets the variable 'original_bg_image' to the image: 'PBG.png'
    resized_bg_image = original_bg_image.resize((1400, 800), Image.LANCZOS) # Resizes the image to fit the geometry of the window and ensures the image reaches peak quality
    bg_image_tk = ImageTk.PhotoImage(resized_bg_image) # Changes PIL/Pillow image into Photoimage so it can be displayed

    bg_canvas_item_id = canvas.create_image(0, 0, image=bg_image_tk, anchor="nw") # Creates an ID for canvas background

    root.update_idletasks() # Informs tkinter to render/create the window

    quizstarter = Quizstarter(canvas, bg_canvas_item_id) # Starts the quizstarter page, passing through canvas and 'bg_canvas_item_id' to be used in the class

    root.bg_image_tk = bg_image_tk # Ensures my background image does not disappear

    root.mainloop() # 'root.mainloop()' loops the entire code to keep the window open