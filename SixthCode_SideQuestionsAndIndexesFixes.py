import tkinter as tk

class Game:
    def __init__(self):
        self.lives = 3
        self.main_questions = [
            {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "correct": 1},
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "correct": 0},
        ]
        self.side_questions1 = [
            {"question": "Which color is the sky?", "options": ["Blue", "Green", "Red"], "correct": 0},
        ]
        self.side_questions2 = [
            {"question": "What color are bananas?", "options": ["Blue", "Yellow", "Red"], "correct": 1},
        ]
        self.current_main_question_index = 0
        self.current_side_question1_index = 0
        self.current_side_question2_index = 0
        self.is_main_question = True
        self.got_side_question1 = False  # Flagg for side_questions1
        self.got_side_question2 = False  # Flagg for side_questions2

        # Opprett hovedvinduet for tkinter
        self.window = tk.Tk()
        self.window.title("Treasure Hunt Game")

        # Label for spørsmål
        self.question_label = tk.Label(self.window, text="", font=("Arial", 14))
        self.question_label.pack()

        # Label for instruksjoner
        self.instruction_label = tk.Label(self.window, text="Click on answers below:", font=("Arial", 12))
        self.instruction_label.pack()

        # Knappene for svaralternativene
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(self.window, text="", command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

        # Label for instruksjoner til inputfeltet
        self.input_instruction_label = tk.Label(self.window, text="Or write the number below:", font=("Arial", 12))
        self.input_instruction_label.pack()

        # Inntastingsfelt for tekstsvar
        self.answer_entry = tk.Entry(self.window)
        self.answer_entry.pack()

        # Knapp for å skrive inn svar via tastatur
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

        # Label for feilmeldinger
        self.error_label = tk.Label(self.window, text="", font=("Arial", 12), fg="red")
        self.error_label.pack()

        self.start_game()

        # Kjører tkinter-vinduet
        self.window.mainloop()

    def start_game(self):
        self.ask_question()

    def ask_question(self):
        if self.is_main_question:
            if self.current_main_question_index < len(self.main_questions):
                question = self.main_questions[self.current_main_question_index]
                self.display_question(question)
            else:
                self.win_game()
        else:
            if not self.got_side_question1:
                question = self.side_questions1[self.current_side_question1_index]
                self.display_question(question)
            elif self.got_side_question1 and not self.got_side_question2:
                question = self.side_questions2[self.current_side_question2_index]
                self.display_question(question)

    def display_question(self, question):
        self.error_label.config(text="")
        self.question_label.config(text=question["question"])

        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=f"{i + 1}. {option}")

        self.answer_entry.delete(0, tk.END)

    def submit_answer(self):
        try:
            player_answer = int(self.answer_entry.get()) - 1  # Gjør brukerens svar 0-basert

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
        else:  # For sidespørsmålene
            if not self.got_side_question1:  # Første sidespørsmål
                question = self.side_questions1[self.current_side_question1_index]
                correct_answer = question["correct"]

                if player_answer == correct_answer:
                    self.correct_answer_side1()
                else:
                    self.wrong_answer_side1()
            elif self.got_side_question1 and not self.got_side_question2:  # Andre sidespørsmål
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
        self.is_main_question = False
        self.got_side_question1 = False  # Spilleren skal nå få et spørsmål fra side_questions1
        self.ask_question()

    def correct_answer_side1(self):
        self.got_side_question1 = True  # Spilleren har nå fått et sidespørsmål1 riktig
        self.is_main_question = True  # Returner til hovedspørsmålene
        self.ask_question()

    def wrong_answer_side1(self):
        self.got_side_question1 = True  # Spilleren har nå fått et sidespørsmål1
        self.got_side_question2 = False  # Nå skal de få et spørsmål fra side_questions2
        self.ask_question()

    def correct_answer_side2(self):
        self.got_side_question2 = True  # Spilleren har nå fått et sidespørsmål2 riktig
        self.got_side_question1 = False  # Gå tilbake til side_questions1
        self.ask_question()

    def wrong_answer_side2(self):
        self.lives -= 1  # Spilleren mister et liv
        if self.lives <= 0:
            self.lose_game()
        else:
            self.got_side_question2 = True  # Spilleren har nå fått et sidespørsmål2
            self.ask_question()

    def lose_game(self):
        self.question_label.config(text="You lost! Do you want to try again or Quit?")
        self.display_end_buttons()

    def win_game(self):
        # Slett alle knapper og inputfelt når spilleren vinner
        self.question_label.config(text="You WON & found the treasure!")
        self.instruction_label.pack_forget()  # Fjern instruksjoner
        self.input_instruction_label.pack_forget()  # Fjern instruksjoner til inputfeltet
        self.answer_entry.pack_forget()  # Fjern inntastingsfeltet
        self.submit_button.pack_forget()  # Fjern submit-knappen
        for button in self.option_buttons:
            button.pack_forget()  # Fjern svarknapper

        # Vis "Try Again" og "Quit" knapper
        self.try_again_button = tk.Button(self.window, text="Try Again", command=self.restart_game)
        self.try_again_button.pack(pady=5)

        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)
        self.quit_button.pack(pady=5)

    def display_end_buttons(self):
        # Deaktiver svarknapper og submit knapp
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.answer_entry.config(state=tk.DISABLED)

        # Vis "Try Again" og "Quit" kn
