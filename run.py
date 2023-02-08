import random

"""
list of words that will be randomly assigned each turn
by use of import random
"""
random_words = [
    'birthday',
    'dream',
    'kitten',
    'coding',
    'burger',
    'castle',
    'science',
    'pickle',
    'magic',
    'computer',
    'beach',
    'holiday',
    'christmas',
    'animal',
    'joker',
    'lion',
    'earth',
    'space',
    'rocket',
    'viking',
    'norway',
    'sunny',
    'rain',
    'snow',
    'winter',
    'summer',
    'autumn',
    'spring',
    'thor',
    'brave',
    'hero',
    'giant',
    'family',
    'united',
    'home',
    'house',
    'safe']

"""
select a word at random from above list
"""
words = random.choice(random_words).upper()
# TESTING IT WORKS WILL REMOVE LATER
print(words)
print(len(words))

"""
screen message for start of the game
"""

print("Welcome player")
print("The game is simple...")
print("Correctly guess the hidden word and you win!")
print("But you only 6 lives")
print("Are you ready?")
print("Let's begin!")
print("")

"""
A function for the hangman display
"""

def hangman(life):
    """
    function to print hangman to the terminal when
    the player makes an incorrect guess, it will have a total of six
    display picutures so the player will have 6 six attempts.
    """
    if life == 0:
        print("+======+  ")
        print("|      |  ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("==========")
    if life == 1:
        print("+======+  ")
        print("|      |  ")
        print("|      O  ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("==========")
    if life == 2:
        print("+======+  ")
        print("|      |  ")
        print("|      O  ")
        print("|      |  ")
        print("|         ")
        print("|         ")
        print("==========")
    if life == 3:
        print("+======+  ")
        print("|      |  ")
        print("|      O  ")
        print("|     /|  ")
        print("|         ")
        print("|         ")
        print("==========")
    if life == 4:
        print("+======+  ")
        print("|      |  ")
        print("|      O  ")
        print("|     /|\ ")
        print("|         ")
        print("|         ")
        print("=========")
    if life == 5:
        print("+======+  ")
        print("|      |  ")
        print("|      O  ")
        print("|     /|\ ")
        print("|     /   ")
        print("|         ")
        print("==========")
    if life == 6:
        print("+======+  ")
        print("|      |  ")
        print("|      O  ")
        print("|     /|\ ")
        print("|     / \ ")
        print("|         ")
        print("==========")


"""
variables for right letter and wrong letter
guess and the max number of lives
"""
correct_guess = ['_'] * len(words)
wrong_guess = []

def letters():
    """
    function for correct guess position dashes
    """
    for i in correct_guess:
        print(i, end=' ')
    print()


"""
While loop for the main game, for every correct guess that letter 
will be added to the dashes to reveal the hidden word, every
incorrect guess will lead to 1 more peice of the hangman to appear.
Game over will reveal the hidden word.
"""

while True:
    print('**************************')
    player_guess = input("Enter a letter here: ").upper()
    if player_guess in words:
        index = 0
        for i in words:
            if i == player_guess:
                correct_guess[index] = player_guess
            index += 1
        letters()
        print('Well done that was the right letter!')
    else:    
        if player_guess not in wrong_guess:
            wrong_guess.append(player_guess)
            print('Haha that letter was wrong!The noose is getting tighter..')
            hangman(len(wrong_guess))
        else:
            print('sorry you already tried that letter!:', player_guess)
        print(wrong_guess)

    if len(wrong_guess) > 5:
        print("Oh dear the Hangman has claimed another poor soul!")
        print("The correct word was ", words)
        break

    if '_' not in correct_guess:
        print('Lucky you....you survived the Hangman..for today')
        break