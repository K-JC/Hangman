# HANGMAN GAME

Hangman a guessing game. Guess the hidden word and you win, but if you can't guess the hidden word you loose. With only 6 lives this game is made a bit more challenging.

Contents?

# Features/future features



The first messages the user will see when the page is loaded is the player welcome message. This welcomes the user to the game hangman and explains the rules. 
Underneath this welcome message will be another message for the user which will say "Enter a letter here". This will give the user clear indication that they can now enter a letter and the game has begun.  

Entering a correct letter will result in a display message "Well done that was the right letter". The correct letter will be shown on the terminal with the remaining hidden letters shown by an underscore "_". The user can use this as a way to see how many letters are in the word they have to guess and what letter might be worth picking next.

Entering an incorrect letters will result in the incorrect letter showing on the screen and the hangman peice to appear indicating the a life lost/wrong guess. Each letter wrong is another peice to the hangman display. The user will only have 6 attempts to guess the hidden word.

Entering a letter that the user has already got wrong will result in a message "sorry you already tried that letter" No life is lost and the user can now choose another letter.

Entering any number or symbol will result in an "oops, not a letter, try again" message. Entering more than one letter at a time will result in a message "please enter one letter at a time". This will not effect the users life count.

Once all the correct letters have been entered and the hidden word has been reveled the message will print to the terminal with a winner message.

Loosing the game will result in a lose message and a message which will tell the user what the correct hidden word was. So the user will always finish knowing what the hidden word was. 

For future features I would like to add a lives count to the terminal so the user can keep tabs on how many lives they have left. 
I would also like to add some visuals like a large Hangman title at the top of the terminal and once a game has been won or lost a "Winner" or "Gameover" display. I think that would make it look better and more visually pleasing as I feel it comes across as a little bland. 


# Testing
Testing in github terminal and heroku...
Family testing the game on the terminal.

# Bugs

solved and unfixed

Numbers and symbols were still allowed to be entered with loosing a life - needed to make a function for this to work and then use this function in my main while loop

More than one letter was still allowed to be entered with loosing a life - i needed to make an if stament that said if more than 1 letter is entered then to print a message. once i had done this i tested but the game would exit after this had been done. I had accidently left a break statemnt in after the if statment once i had taken this out it worked just as i expected it to. 

The word that was chosen at random was showing on the terminal - i forgot to remove the print statment, once removed all fixed. The player will not see the word they have to guess already on the screen. 

No statment was given for loosing - so game wasnt finished when lost. Needed to add hangman(len(...)
Wasnt visually pleasing to have each turn ontop of one another. Fixed this with a print statement with = at first but then changed this to * as I found it more visially pleasing. 

Hangman display needed to be put in a function with print statments around for it to work
lowercase letters needed to change to upper in order for them to be uppercase when guessed.


# Validator testing
Using PEP8 Python Validator, the only error left that I after correcting the rest was "ERROR: W605 invalid escape sequence '\ '". Only the hangman displays with the backslash in were effected. 

# Deployment (heroku)
Following the steps that Code Insitute have shown me to do....


# Credits
Tutorial-[Tech With Mike](https://www.youtube.com/channel/UCnvj-t_xNcB0ap82KoEm8mQ)

Tutorial-[Kylie Ying](https://www.youtube.com/watch?v=cJJTnI22IF8)

Tutorial-[Shaun Halverson](https://www.youtube.com/watch?v=pFvSb7cb_Us)

Tutorial-[Kite](https://www.youtube.com/watch?v=m4nEnsavl6w)