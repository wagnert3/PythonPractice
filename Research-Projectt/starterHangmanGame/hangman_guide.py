#Imports the random module, allowing you to use its functions, like selecting a random item from a list.
import random


#Defines a dictionary named words_and_hints containing pairs of words and their corresponding hints.

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

# Esse metodo pega os items do dictionary e transforma em uma lista de tuples para que a library random possa 
# entao usar a funcao choice, que sera responsavel por escolher aleatoriamente um key value pair do dictionary

# This method takes the items from the dictionary and turns them into a list of tuples so that the random
# library can use the choice function, which will be responsible for randomly selecting a key-value pair from the dictionary.
def choose_word_and_hint():
    word, hint = random.choice(list(words_and_hints.items())) #randomly selects a key-value pair from the dictionary, assigning the word to word and the hint to hint.
    return word, hint

# Essa funcao vai percorrer a palavra da vez, vai pegar as letras que o user ja tentou adivinhar e vai olhar letra por letra
# da palavra da vez pra ver se bate com as letras que o user tentou usar, se bater ele mostra a letra se nao bater ele mostra _

# This function will go through the current word, take the letters that the user has already tried to guess, and check 
# each letter of the current word to see if it matches the letters the user has tried; if it matches, it shows the letter, 
# otherwise it shows _.


def display_progress(word, correct_guesses):
    displayed = ''
    for letter in word:
        if letter in correct_guesses:
            displayed += letter
        else:
            displayed += '_'
        displayed += ' ' # add space btw the letters
    return displayed

# Essa funcao comeca com a escolha aleatoria da palavra da vez, bem como sua dica.
# Depois eh criada uma lista vazia para ser armazenada as letras que o user tentar adivinhas
# Define que o user pode errar ate 6 vezes
# hint_show comeca com false pra dizer que a dica ainda nao foi mostrada

# This function starts by randomly choosing the current word and its hint.
# Then it creates an empty list to store the letters the user tries to guess.
# It sets that the user can make up to 6 wrong guesses.
# hint_shown starts as false to indicate that the hint has not been shown yet.


def play_game():
    word, hint = choose_word_and_hint()
    correct_guesses = []
    attempts = 6
    hint_shown = False
    print("Hangman Game!") # Inicia a mensagem inicial do game

# Enquanto a quantidade de tentativas for maior que 0, ou seja, quando chegar em 6 vai parar,  e tiver _ em display_progress 
# signigica que ainda tem _ ou seja tem letrar para serem adivinhadas

# While the number of attempts is greater than 0, meaning it will stop after 6 attempts, and there are _ in display_progress,
# it means there are still letters to be guessed.
    while attempts > 0 and '_' in display_progress(word, correct_guesses):
        print(display_progress(word, correct_guesses))
        guess = input("Guess a letter: ").lower() #captura o inpute do user e guarda na variavel guess, converte para minuscula

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
                if show_hint == 'yes' or  show_hint == 'y':
                    print(f"Hint: {hint}")
                    hint_shown = True

    if '_' not in display_progress(word, correct_guesses):
        print("Congratulations, you won!")
    else:
        print(f"Game over! The word was '{word}'.")
# Esse pedaco quer dizer: Se este arquivo python eh o que estamos executando diretamente, 
# nao sendo usado por outro arquivo, entao vamos comecar a execucao por play_game()
# Essa verificação é uma prática usada para controlar o comportamento do script quando ele é executado 
# diretamente ou importado como um módulo, 
# mas não é necessária para a execução do script em si.
# é uma variável especial no Python, definida automaticamente pelo interpretador. 
# Ela existe em todos os scripts e módulos Python. 
# Quando um script é executado diretamente pelo Python, a variável __name__ é definida como "__main__" pelo interpretador. 
# Isso indica que o script é o ponto de entrada principal do programa.

# This piece means: If this Python file is what we are running directly,
# not being used by another file, then let's start the execution with play_game().
# This check is a practice used to control the script’s behavior when it’s executed
# directly or imported as a module,
# but it is not necessary for the script’s execution itself.
# __name__ is a special variable in Python, automatically defined by the interpreter.
# It exists in all Python scripts and modules.
# When a script is executed directly by Python, the __name__ variable is set to "__main__" by the interpreter,
# indicating that the script is the main entry point of the program.
if __name__ == "__main__":
    play_game()
