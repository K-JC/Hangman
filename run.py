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



    