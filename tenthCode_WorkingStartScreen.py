import tkinter as tk
from PIL import Image, ImageTk
import os


class Game:
    def __init__(self):
        self.lives = 3
        self.main_questions = [
            {"question": "Which year was Nintendo 64 released?", "options": ["2000", "1996", "2008"], "correct": 1},
            {"question": "How many series is there of the game The Sims?", "options": ["1", "3", "4"], "correct": 2},
            {"question": "What is the style this game is made in?", "options": ["Pixels", "Lego", "3D"], "correct": 0},
            {"question": "What color does the Pokémon Pikachu has?", "options": ["Brown", "Yellow", "Blue"], "correct": 1},
            {"question": "What is the latest console from Sony?", "options": ["PS5", "PSP", "Sony Move"], "correct": 0},
            {"question": "What is the name of main character in the Zelda games?", "options": ["Zelda", "Link", "Winnie"], "correct": 1},
            {"question": "What is the next evolution of Magikarp?", "options": ["Bigger Fish", "Gyarados", "Kingler"], "correct": 1},
            {"question": "What is the name of the newest game that takes place in the magic world of Harry Potter?", "options": ["Harry Potter the 10th game", "Magic School", "Hogwarts Legacy"], "correct": 2},
            {"question": "What is the name of Nintendo's newest console?", "options": ["Nintendo Switch", "Nintendo Root", "Nintendo Up"], "correct": 0},
            {"question": "What is Need for Speed?", "options": ["Car Game", "Car", "Best Game"], "correct": 0},
        ]
        self.side_questions1 = [
            {"question": "Who are making The Sims games?", "options": ["EA", "Steam", "Nintendo"], "correct": 0},
            {"question": "What is the color of Link's hat?", "options": ["Pink", "Green", "Yellow"], "correct": 1},
            {"question": "What is person called that plays games a lot?", "options": ["Lazy person", "Energetic person", "Gamer"], "correct": 2},
            {"question": "What is the color of the crystal called in The Sims?", "options": ["Crystal", "Plumbob", "Green Diamond"], "correct": 1},
            {"question": "What is an Eevee?", "options": ["Pokémon", "Little Fox", "Cat"], "correct": 0},
            {"question": "What is the color of Mario's hat?", "options": ["Green", "Yellow", "Red"], "correct": 2},
            {"question": "What is one of the most used cheat codes in The Sims?", "options": ["Motherlode", "moveobjects", "The Sims has no cheat codes"], "correct": 0},
            {"question": "What are games you can play on your phone called?", "options": ["Small Games", "Mobile Games", "Small Screen Games"], "correct": 1},
            {"question": "What is the name of Microsoft's most popular console?", "options": ["Xbox", "PC", "Console Microsoft"], "correct": 0},
            {"question": "What is the name of the Princess in Super Mario?", "options": ["Peach", "Sunny", "Pink Princess"], "correct": 1},
        ]
        self.side_questions2 = [
            {"question": "What color are bananas?", "options": ["Blue", "Yellow", "Red"], "correct": 1},
            {"question": "What color is the sky?", "options": ["Blue", "Yellow", "Red"], "correct": 0},
            {"question": "What is early in the day called?", "options": ["Early", "Morning", "Late Night"], "correct": 1},
            {"question": "How many legs does a dog have?", "options": ["4", "2", "6"], "correct": 0},
            {"question": "Which season is the warmest?", "options": ["Spring", "Summer", "Fall"], "correct": 1},
            {"question": "What is the thing we check the time on called?", "options": ["Sun", "Clock", "Screen"], "correct": 1},
            {"question": "What has many colors during spring?", "options": ["Sky", "Grass", "Flowers"], "correct": 2},
            {"question": "What is the full name of the country that starts with an N and is placed up North?", "options": ["Norway", "Netherlands", "New Zealand"], "correct": 0},
            {"question": "What is the name of a person called?", "options": ["Name", "First Name", "Their Name"], "correct": 1},
            {"question": "What is this sentence called?", "options": ["Questions", "Sentences", "Weird things"], "correct": 0},
        ]
        self.current_main_question_index = 0
        self.current_side_question1_index = 0
        self.current_side_question2_index = 0
        self.is_main_question = True
        self.got_side_question1 = False
        self.got_side_question2 = False

        # Create main window for tkinter
        self.window = tk.Tk()
        self.window.title("Pixel Quests Island")

        # Set default window size
        self.window.geometry("800x600")

        # Load and resize the background image
        self.bg_image = Image.open("assets/Island_front.jpeg")  # Change this to the correct path for your image
        self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)  # Replaced ANTIALIAS with LANCZOS
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Load and resize the welcome text image
        self.logo_image = Image.open("assets/Pixel_Questions_Island_WithoutBackground.png")
        self.logo_image = self.logo_image.resize((500, 500), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        # Create a canvas to display the background image
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Display the background image on the canvas
        self.background = self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        # Knapper
        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)

        # Plassering av knapper
        self.start_button_window = self.canvas.create_window(400, 300, anchor="center", window=self.start_button)
        self.quit_button_window = self.canvas.create_window(400, 360, anchor="center", window=self.quit_button)


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

        # Label for error messages
        self.error_label = tk.Label(self.window, text="", font=("Arial", 12), fg="red")

        # Startskjerm
        self.show_start_screen()

        # Bind resizing event to the window
        self.window.bind("<Configure>", self.resize_elements)

        # Run the tkinter window
        self.window.mainloop()

    def resize_elements(self, event):
        # Get the new width and height
        new_width = event.width
        new_height = event.height

        if new_width >= 800 and new_height >= 600:
            # Resize the background image to the new dimensions
            resized_bg_image = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized_bg_image)

            resized_logo_image = self.logo_image.resize((new_width // 2, new_height // 2), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(resized_logo_image)

            # Update the canvas with the resized images
            self.canvas.itemconfig(self.background, image=self.bg_photo)
            self.canvas.itemconfig(self.logo, image=self.logo_photo)

            # Justere logoen KUN i widescreen-modus
            if new_width > 800:  # Dette vil skje kun i widescreen-modus
                # Resize logo image dynamically with a max width and height limit
                max_logo_width = new_width // 1  # Set max width to a third of window width
                max_logo_height = new_height // 2  # Set max height to a fourth of window height

                # Keep the aspect ratio of the logo
                aspect_ratio = self.logo_image.width / self.logo_image.height
                new_logo_width = min(max_logo_width, int(max_logo_height * aspect_ratio))
                new_logo_height = min(max_logo_height, int(max_logo_width / aspect_ratio))

                # Resize the logo image
                resized_logo = self.logo_image.resize((new_logo_width, new_logo_height), Image.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(resized_logo)

                # Update the canvas with the new logo image
                self.canvas.itemconfig(self.logo, image=self.logo_photo)

                # Flytt knappene lenger ned i widescreen-modus
                self.canvas.coords(self.start_button_window, new_width // 2, new_height // 2 + 50)
                self.canvas.coords(self.quit_button_window, new_width // 2, new_height // 2 + 100)
            else:
                # Standard plassering for vindusmodus
                self.canvas.coords(self.start_button_window, new_width // 2, new_height // 3 + 150)
                self.canvas.coords(self.quit_button_window, new_width // 2, new_height // 3 + 200)

            # Reposisjoner logoen og knappene
            self.canvas.coords(self.logo, new_width // 2, new_height // 3)
            #self.canvas.coords(self.start_button_window, new_width // 2, new_height // 3 + 150)  # Flytter "Start Game" lengre ned
            #self.canvas.coords(self.quit_button_window, new_width // 2, new_height // 3 + 200)  # Flytter "Quit" også lengre ned

    def show_start_screen(self):
        # Fjern andre elementer hvis de finnes
        self.canvas.delete("all")
        self.background = self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
        self.lives_label.pack_forget()
        self.question_label.pack_forget()
        self.instructions_label_top.pack_forget()
        for button in self.option_buttons:
            button.pack_forget()
        self.error_label.pack_forget()

        # Display the logo on the start screen
        self.logo = self.canvas.create_image(400, 200, anchor="center", image=self.logo_photo)

        # Plassere knappene under hverandre med mellomrom
        # Endre knappene til å ha svart bakgrunn, hvit fet tekst
        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game,
                                      bg="black", fg="white", font=("Arial", 12, "bold"))
        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit,
                                     bg="black", fg="white", font=("Arial", 12, "bold"))

        # Oppretting av knappene på canvas under hverandre
        self.start_button_window = self.canvas.create_window(400, 250, anchor="center", window=self.start_button)
        self.quit_button_window = self.canvas.create_window(400, 350, anchor="center", window=self.quit_button)

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
        self.instructions_label_top.pack(pady=10)
        for button in self.option_buttons:
            button.pack(pady=5)
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

    def check_answer(self, player_answer):
        if self.is_main_question:
            question = self.main_questions[self.current_main_question_index]
            correct_answer = question["correct"]

            if player_answer == correct_answer:
                self.correct_answer_main()
            else:
                self.wrong_answer_main()
        else:
            if not self.got_side_question1:
                question = self.side_questions1[self.current_side_question1_index]
                correct_answer = question["correct"]

                if player_answer == correct_answer:
                    self.correct_answer_side1()
                else:
                    self.wrong_answer_side1()
            elif self.got_side_question1 and not self.got_side_question2:
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

        self.start_game()


# Run the game
if __name__ == "__main__":
    Game()
