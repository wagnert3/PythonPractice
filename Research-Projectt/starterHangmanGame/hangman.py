import random

words_and_hints = {
    'python': 'A popular programming language.',
    'jupiter': 'The largest planet in the solar system.',
    'stephen': 'The best instructor in the wmad course.',
    'ballet': 'A classical form of dance using precise and highly formalized set steps and gestures.',
    'ghost': 'An apparition of a dead person.',
    'ocean': 'A large body of salt water that covers most of the Earth\'s surface.',
    'eclipse': 'An astronomical event where one celestial body moves into the shadow of another.',
    'volcano': 'A mountain or hill with a crater which lava, rock fragments, hot vapor, and gas are being or have been erupted from the Earth\'s crust.',
    'kangaroo': 'A large hopping mammal from Australia, known for carrying its babies in a pouch.',
    'pyramid': 'A monumental structure with a square or triangular base and sloping sides that meet in a point at the top, especially in Egypt.',
    'amazon': 'The largest rainforest in the world, or the longest river in South America.',
    'sherlock': 'A fictional detective known for his keen observational skills and deductive reasoning.',
    'titanic': 'A famous ship that sank in the North Atlantic Ocean in 1912.',
    'chocolate': 'A sweet, brown food made from roasted and ground cacao seeds, often eaten as a candy.',
    'piano': 'A large keyboard musical instrument',
}

def choose_word_and_hint():
    word, hint = random.choice(list(words_and_hints.items())) # choice is a function from the random module that picks a random element from a list
    return word, hint

def display_progress(word, correct_guesses):
    displayed = ''
    for letter in word:
        displayed += letter if letter in correct_guesses else '_'
        displayed += ' '
    return displayed

def play_game():
    word, hint = choose_word_and_hint()
    correct_guesses = []
    attempts = 6
    hint_shown = False
    print("Hangman Game!")

    while attempts > 0 and '_' in display_progress(word, correct_guesses):
        print(display_progress(word, correct_guesses))
        guess = input("Guess a letter: ").lower()

        if guess in correct_guesses:
            print("You already tried that letter.")
            continue
        elif guess in word:
            correct_guesses.append(guess)
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")
            if attempts <= 3 and not hint_shown:
                show_hint = input("Do you want a hint (yes or no)? ").lower()
                if show_hint == 'yes' or show_hint == 'y':
                    print(f"Hint: {hint}")
                    hint_shown = True
                else:
                    print("No hint for you, then!")  
                    
                      
    if '_' not in display_progress(word, correct_guesses):
        print("Congratulations, you won!")
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_game()
