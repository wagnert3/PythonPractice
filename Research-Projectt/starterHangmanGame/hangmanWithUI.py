import random
import tkinter as tk

words_and_hints = {
    'python': 'A popular programming language.',
    'jupiter': 'The largest planet in the solar system.',
    'stephen': 'The best instructor in the wmad course.',
    'ballet': 'A classical form of dance using precise and highly formalized set steps and gestures.',
    'ghost': 'An apparition of a dead person.',
    'ocean': 'A large body of salt water that covers most of the Earth\'s surface.',
    'eclipse': 'An astronomical event where one celestial body moves into the shadow of another.',
    'volcano': 'A mountain or hill with a crater which lava, rock fragments, hot vapor, and gas are being or have been erupted from the Earth\'s crust.',
    'sahara': 'The largest hot desert in the world, located in North Africa.',
    'kangaroo': 'A large hopping mammal from Australia, known for carrying its babies in a pouch.',
    'pyramid': 'A monumental structure with a square or triangular base and sloping sides that meet in a point at the top, especially in Egypt.',
    'amazon': 'The largest rainforest in the world, or the longest river in South America.',
    'sherlock': 'A fictional detective known for his keen observational skills and deductive reasoning.',
    'titanic': 'A famous ship that sank in the North Atlantic Ocean in 1912.',
    'chocolate': 'A sweet, brown food made from roasted and ground cacao seeds, often eaten as a candy.',
    'himalayas': 'The highest mountain range in the world,',
    'piano': 'A large keyboard musical instrument',
    'sudoku': 'A number puzzle game where each row, column, and region must contain all digits from 1 to 9.'
}

def choose_word_and_hint():
    word, hint = random.choice(list(words_and_hints.items()))
    return word, hint

class HangmanGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.word, self.hint = choose_word_and_hint()
        self.correct_guesses = []
        self.wrong_attempts = 0

        self.title("Hangman Game")
        self.create_widgets()

    def create_widgets(self):
        self.label_word = tk.Label(self, text="_ " * len(self.word))
        self.label_word.pack()

        self.entry_guess = tk.Entry(self)
        self.entry_guess.pack()

        self.button_guess = tk.Button(self, text="Guess", command=self.guess)
        self.button_guess.pack()

        self.button_hint = tk.Button(self, text="Show Hint", command=self.show_hint, state=tk.DISABLED)
        self.button_hint.pack()

        self.label_status = tk.Label(self, text="")
        self.label_status.pack()

    def guess(self):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)  # Clear the entry field

        if guess in self.correct_guesses or guess in self.word:
            self.label_status['text'] = "You already tried that letter."
            return

        if guess in self.word:
            self.correct_guesses.append(guess)
            self.label_status['text'] = "Correct!"
        else:
            self.wrong_attempts += 1
            self.label_status['text'] = f"Wrong! You have {6 - self.wrong_attempts} attempts left."

        self.update_displayed_word()

        if self.wrong_attempts >= 3:
            self.button_hint['state'] = tk.NORMAL

        if self.wrong_attempts == 6 or "_" not in self.label_word['text']:
            self.end_game()

    def show_hint(self):
        self.label_status['text'] = f"Hint: {self.hint}"

    def update_displayed_word(self):
        displayed = ' '.join([letter if letter in self.correct_guesses else '_' for letter in self.word])
        self.label_word['text'] = displayed

    def end_game(self):
        if "_" not in self.label_word['text']:
            self.label_status['text'] = "Congratulations, you won!"
        else:
            self.label_status['text'] = f"Game over! The word was '{self.word}'. The hint was: {self.hint}"

if __name__ == "__main__":
    app = HangmanGame()
    app.mainloop()