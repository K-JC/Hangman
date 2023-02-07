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
lives = 6 # remove later?

"""
dashes position/letters function
"""

"""
while loop main game
"""
