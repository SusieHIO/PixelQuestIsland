import tkinter as tk
import random


class Game:
    def __init__(self):
        self.lives = 3
        self.main_questions = [
            {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "correct": 1},
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "correct": 0},
            # Add more questions here
        ]
        self.side_questions = [
            {"question": "What color is the sky?", "options": ["Blue", "Green", "Red"], "correct": 0},
            {"question": "How many legs does a spider have?", "options": ["6", "8", "10"], "correct": 1},
        ]
        self.current_question_index = 0
        self.side_question_index = 0
        self.main_question_correct_count = 0

        # Opprett hovedvinduet for tkinter
        self.window = tk.Tk()
        self.window.title("Treasure Hunt Game")

        # Label for spørsmål
        self.question_label = tk.Label(self.window, text="", font=("Arial", 14))
        self.question_label.pack()

        # Instruksjoner for å klikke eller skrive inn svar
        self.instructions_label = tk.Label(self.window, text="Click your answer below or write it in the box",
                                           font=("Arial", 12))
        self.instructions_label.pack()

        # Knappene for svaralternativene
        self.option_buttons = []
        for i in range(3):
            button = tk.Button(self.window, text="", command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

        # Inntastingsfelt for tekstsvar
        self.answer_entry = tk.Entry(self.window)
        self.answer_entry.pack()

        # Knapp for å skrive inn svar via tastatur
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

        # Label for feilmeldinger
        self.error_label = tk.Label(self.window, text="", font=("Arial", 12), fg="red")
        self.error_label.pack()

        # Label for å vise antall liv
        self.lives_label = tk.Label(self.window, text=f"Lives: {self.lives}")
        self.lives_label.pack()

        self.start_game()

        # Kjører tkinter-vinduet
        self.window.mainloop()

    def start_game(self):
        self.ask_main_question()

    def ask_main_question(self):
        if self.current_question_index < len(self.main_questions):
            question = self.main_questions[self.current_question_index]
            self.display_question(question)
        else:
            self.win_game()

    def display_question(self, question):
        # Tømmer feilmeldingsfeltet
        self.error_label.config(text="")

        # Oppdater spørsmålsteksten
        self.question_label.config(text=question["question"])

        # Oppdater svaralternativene i knappene med tall foran hvert alternativ
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(text=f"{i + 1}. {option}")

        # Tømmer inntastingsfeltet hver gang et nytt spørsmål vises
        self.answer_entry.delete(0, tk.END)

    def submit_answer(self):
        try:
            # Henter spillerens input og konverterer det til en int
            player_answer = int(self.answer_entry.get()) - 1

            # Sjekker om input er i riktig område
            if player_answer < 0 or player_answer >= len(self.option_buttons):
                raise ValueError("Out of range")

            # Sjekker om inputen fra tastaturet er riktig
            self.check_answer(player_answer)

        except (ValueError, TypeError):
            # Viser feilmelding hvis input er ugyldig
            self.error_label.config(text="Not valid number, you need to add number from 1-3")

    def check_answer(self, player_answer):
        question = self.main_questions[self.current_question_index]
        if player_answer == question["correct"]:
            self.correct_answer()
        else:
            self.wrong_answer()

    def correct_answer(self):
        print("Correct answer!")
        self.main_question_correct_count += 1
        self.check_progress()

    def wrong_answer(self):
        print("Wrong answer!")
        self.lives -= 1
        self.lives_label.config(text=f"Lives: {self.lives}")
        self.check_lives()

    def check_lives(self):
        if self.lives > 0:
            self.ask_side_question()
        else:
            self.game_over()

    def ask_side_question(self):
        question = self.side_questions[self.side_question_index]
        self.display_question(question)

    def check_progress(self):
        if self.main_question_correct_count == 10:
            self.win_game()
        else:
            self.current_question_index += 1
            self.ask_main_question()

    def win_game(self):
        self.show_end_screen("Congratulations! You won and found the Treasure!")

    def game_over(self):
        self.show_end_screen("Game Over!")

    def show_end_screen(self, message):
        # Skjuler spørsmål og svaralternativer
        self.question_label.config(text=message)
        self.instructions_label.pack_forget()
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()

        for button in self.option_buttons:
            button.pack_forget()

        # Knappene for å starte på nytt eller avslutte
        try_again_button = tk.Button(self.window, text="Try Again", command=self.restart_game)
        try_again_button.pack(pady=5)

        quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)
        quit_button.pack(pady=5)

    def restart_game(self):
        self.lives = 3
        self.current_question_index = 0
        self.side_question_index = 0
        self.main_question_correct_count = 0
        self.lives_label.config(text=f"Lives: {self.lives}")

        # Fjerner avslutningsskjermen og starter spillet på nytt
        for widget in self.window.winfo_children():
            widget.pack_forget()

        self.instructions_label.pack()
        self.question_label.pack()
        for button in self.option_buttons:
            button.pack(pady=5)

        self.answer_entry.pack()
        self.submit_button.pack()
        self.lives_label.pack()

        self.start_game()


# Kjør spillet
if __name__ == "__main__":
    Game()
