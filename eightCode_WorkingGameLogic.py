import tkinter as tk


class Game:
    def __init__(self):
        self.lives = 3
        self.main_questions = [
            {"question": "Which year was Nintendo 64 released?", "options": ["2000", "1996", "2008"], "correct": 1},
            {"question": "How many series is there of the game The Sims?", "options": ["1", "3", "4"], "correct": 2},
            {"question": "What is the style this game is made in?", "options": ["Pixels", "Lego", "3D"], "correct": 0},
            {"question": "What color does the Pokémon Pikachu has?",
             "options": ["Brown", "Yellow", "Blue"], "correct": 1},
            {"question": "What is the latest console from Sony?", "options": ["PS5", "PSP", "Sony Move"], "correct": 0},
            {"question": "What is the name of main characther in the Zelda games?",
             "options": ["Zelda", "Link", "Winnie"], "correct": 1},
            {"question": "What is the next evolation of Magickarp?",
             "options": ["Bigger Fish", "Gyarados", "Kingler"], "correct": 1},
            {"question": "What is the neame of the newst game that takes place in the magic world of Harry Potter?",
             "options": ["Harry Potter the 10th game", "Magic School", "Hogwarts Legacy"], "correct": 2},
            {"question": "What is the name of Nintendo's newest console?",
             "options": ["Nintendo Switch", "Nintendo Root", "Nintendo Up"], "correct": 0},
            {"question": "What is Need for Speed?", "options": ["Car Game", "Car", "Best Game"], "correct": 0},
        ]
        self.side_questions1 = [
            {"question": "Who are making The Sims games?", "options": ["EA", "Steam", "Nintendo"], "correct": 0},
            {"question": "What is the color of Link's hat?", "options": ["Pink", "Green", "Yellow"], "correct": 1},
            {"question": "What is person called that play games a lot?",
             "options": ["Lazy person", "Energetic person", "Gamer"], "correct": 2},
            {"question": "What is the color of the crystal called in the Sims?",
             "options": ["Crystal", "Plumbob", "Green Diamond"], "correct": 1},
            {"question": "What is a Eevee?", "options": ["Pokémon", "Little Fox", "Cat"], "correct": 0},
            {"question": "What is the color of Mario's hat?", "options": ["Green", "Yellow", "Red"], "correct": 2},
            {"question": "What is one of the most used cheat codes in the Sims?",
             "options": ["Motherlode", "moveobjects", "Sims has no cheat codes"], "correct": 0},
            {"question": "What are games you can play on your phone called?",
             "options": ["Small Games", "Mobile Games", "Small Screen Games"], "correct": 1},
            {"question": "What is the name of Microsoft's most popular console?",
             "options": ["Xbox", "PC", "Console Microsoft"], "correct": 0},
            {"question": "What is the name of the Princess in Super Mario?",
             "options": ["Peach", "Sunny", "Pink Princess"], "correct": 1},
        ]
        self.side_questions2 = [
            {"question": "What color are bananas?", "options": ["Blue", "Yellow", "Red"], "correct": 1},
            {"question": "What color is the sky?", "options": ["Blue", "Yellow", "Red"], "correct": 0},
            {"question": "What is early in the day called?",
             "options": ["Early", "Morning", "Late Night"], "correct": 1},
            {"question": "How many legs does a dog has?", "options": ["4", "2", "6"], "correct": 0},
            {"question": "Which season is the warmest?", "options": ["Spring", "Summer", "Fall"], "correct": 1},
            {"question": "What is the thing we check the time on, called?",
             "options": ["Sun", "Clock", "Screen"], "correct": 1},
            {"question": "What has many colors during spring?", "options": ["Sky", "Grass", "Flowers"], "correct": 2},
            {"question": "What is the full name of the country that start with an N and are placed up North?",
             "options": ["Norway", "Netherlands", "New Zealand"], "correct": 0},
            {"question": "What is the name of a person called?",
             "options": ["Name", "First Name", "Their Name"], "correct": 1},
            {"question": "What is this setence called?",
             "options": ["Questions", "Sentences", "Weird things"], "correct": 0},
        ]
        self.current_main_question_index = 0
        self.current_side_question1_index = 0
        self.current_side_question2_index = 0
        self.is_main_question = True
        self.got_side_question1 = False
        self.got_side_question2 = False

        # Create main window for tkinter
        self.window = tk.Tk()
        self.window.title("Treasure Hunt Game")

        # Label for lives
        self.lives_label = tk.Label(self.window, text=f"Lives: {self.lives}", font=("Arial", 12))

        # Label for question
        self.question_label = tk.Label(self.window, text="", font=("Arial", 14))

        # Label for instructions
        self.instructions_label_top = tk.Label(self.window, text="Click on answers below:", font=("Arial", 12))

        # Option buttons
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(self.window, text="", command=lambda idx=i: self.check_answer(idx))
            self.option_buttons.append(button)

        # Label for input instructions
        self.instructions_label_bottom = tk.Label(self.window, text="Or write the number below:", font=("Arial", 12))
        self.instructions_label_bottom.pack()

        # Input field for text answers
        self.answer_entry = tk.Entry(self.window)

        # Button to submit answer via keyboard
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_answer)

        # Label for error messages
        self.error_label = tk.Label(self.window, text="", font=("Arial", 12), fg="red")

        # Startskjerm
        self.show_start_screen()

        # Run the tkinter window
        self.window.mainloop()

    def show_start_screen(self):
        # Fjern andre elementer hvis de finnes
        self.lives_label.pack_forget()
        self.question_label.pack_forget()
        self.instructions_label_top.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.error_label.pack_forget()

        # Vis startskjerm med knapper
        start_label = tk.Label(self.window, text="Welcome to the Treasure Hunt Game!", font=("Arial", 16))
        start_label.pack(pady=20)

        start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        start_button.pack(pady=10)

        quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)
        quit_button.pack(pady=10)

    def start_game(self):

        for widget in self.window.winfo_children():
            widget.pack_forget()

        self.lives = 3  # Reset lives when starting the game
        self.current_main_question_index = 0
        self.current_side_question1_index = 0
        self.current_side_question2_index = 0
        self.is_main_question = True
        self.got_side_question1 = False
        self.got_side_question2 = False
        self.lives_label.config(text=f"Lives: {self.lives}")  # Update lives label
        self.ask_question()

        self.lives_label.pack(anchor="nw", padx=10, pady=10)
        self.question_label.pack()
        self.instructions_label_top.pack()
        for button in self.option_buttons:
            button.pack(pady=5)
        self.answer_entry.pack()
        self.submit_button.pack()
        self.error_label.pack()

        self.ask_question()

    def ask_question(self):
        if self.is_main_question:
            if self.current_main_question_index < len(self.main_questions):
                question = self.main_questions[self.current_main_question_index]
                self.display_question(question)
            else:
                self.win_game()  # Call win_game if all main questions are answered
        else:
            if not self.got_side_question1:
                if self.current_side_question1_index < len(self.side_questions1):
                    question = self.side_questions1[self.current_side_question1_index]
                    self.display_question(question)
                else:
                    self.win_game()
            elif self.got_side_question1 and not self.got_side_question2:
                if self.current_side_question2_index < len(self.side_questions2):
                    question = self.side_questions2[self.current_side_question2_index]
                    self.display_question(question)
                else:
                    self.win_game()

    def display_question(self, question):
        self.error_label.config(text="")
        self.question_label.config(text=question["question"])

        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=f"{i + 1}. {option}")

        self.answer_entry.delete(0, tk.END)

    def submit_answer(self):
        try:
            player_answer = int(self.answer_entry.get()) - 1  # Convert user's answer to 0-based index

            if player_answer < 0 or player_answer >= len(self.option_buttons):
                raise ValueError("Out of range")

            self.check_answer(player_answer)

        except (ValueError, TypeError):
            self.error_label.config(text="Not a valid number, you need to enter a number from 1-3")

    def check_answer(self, player_answer):
        if self.is_main_question:
            question = self.main_questions[self.current_main_question_index]
            correct_answer = question["correct"]

            if player_answer == correct_answer:
                self.correct_answer_main()
            else:
                self.wrong_answer_main()
        else:  # For side questions
            if not self.got_side_question1:  # First side question
                question = self.side_questions1[self.current_side_question1_index]
                correct_answer = question["correct"]

                if player_answer == correct_answer:
                    self.correct_answer_side1()
                else:
                    self.wrong_answer_side1()
            elif self.got_side_question1 and not self.got_side_question2:  # Second side question
                question = self.side_questions2[self.current_side_question2_index]
                correct_answer = question["correct"]

                if player_answer == correct_answer:
                    self.correct_answer_side2()
                else:
                    self.wrong_answer_side2()

    def correct_answer_main(self):
        self.current_main_question_index += 1
        self.is_main_question = True
        self.ask_question()

    def wrong_answer_main(self):
        self.lives -= 1  # Lose a life for a wrong answer
        self.lives_label.config(text=f"Lives: {self.lives}")  # Update lives label
        if self.lives <= 0:
            self.lose_game()  # Call the lose_game method when out of lives
        else:
            self.is_main_question = False
            self.got_side_question1 = False  # Player will now get a question from side_questions1
            self.ask_question()

    def correct_answer_side1(self):
        self.got_side_question1 = True  # Player has now answered side_question1 correctly
        self.is_main_question = True  # Return to main questions
        self.ask_question()

    def wrong_answer_side1(self):
        self.lives -= 1  # Lose a life for a wrong answer
        self.lives_label.config(text=f"Lives: {self.lives}")  # Update lives label
        if self.lives <= 0:
            self.lose_game()  # Call the lose_game method when out of lives
        else:
            self.got_side_question1 = True  # Player has now answered side_question1
            self.got_side_question2 = False  # Now they will get a question from side_questions2
            self.ask_question()

    def correct_answer_side2(self):
        self.got_side_question2 = True  # Player has now answered side_question2 correctly
        self.got_side_question1 = False  # Go back to side_questions1
        self.ask_question()

    def wrong_answer_side2(self):
        self.lives -= 1  # Lose a life for a wrong answer
        self.lives_label.config(text=f"Lives: {self.lives}")  # Update lives label
        if self.lives <= 0:
            self.lose_game()  # Call the lose_game method when out of lives
        else:
            self.got_side_question1 = True  # Player har nådd side_question1
            self.got_side_question2 = True  # Player har nådd side_question2
            self.ask_question()

    def win_game(self):
        self.show_end_screen("Congratulations! You won and found the Treasure!")

    def lose_game(self):
        self.show_end_screen("Game Over!")

    def show_end_screen(self, message):
        self.question_label.config(text=message)
        self.instructions_label_top.pack_forget()
        self.instructions_label_bottom.pack_forget()
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()

        for button in self.option_buttons:
            button.pack_forget()

        try_again_button = tk.Button(self.window, text="Try Again", command=self.restart_game)
        try_again_button.pack(pady=5)

        quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)
        quit_button.pack(pady=5)

    def restart_game(self):
        self.lives = 3
        self.current_main_question_index = 0
        self.current_side_question1_index = 0
        self.current_side_question2_index = 0
        self.is_main_question = True
        self.got_side_question1 = False
        self.got_side_question2 = False
        self.lives_label.config(text=f"Lives: {self.lives}")  # Reset lives label

        for widget in self.window.winfo_children():
            widget.pack_forget()

        # Reset GUI
        self.lives_label.pack(anchor="nw", padx=10, pady=10)
        self.instructions_label_top.pack()
        self.question_label.pack()
        for button in self.option_buttons:
            button.pack(pady=5)

        self.instructions_label_bottom.pack()
        self.answer_entry.pack()
        self.submit_button.pack()

        self.start_game()


# Run the game
if __name__ == "__main__":
    Game()
