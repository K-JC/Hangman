# HANGMAN GAME

Hangman a guessing game. Guess the hidden word and you win, but if you can't you loose. With 6 lives this game is made challenging.

Contents?

# Features/future features

Player welcome message
Enter a letter message 
Incorrect letters will be displayed below the hangman which will also appear for an incorrect guess
correct guesses will result in that correct letter being iploaded to the terminal with dashes for the letters stil to be guessed. The player can use this to see what letters they have left and what letters might be worth picking next.
Entering a letter you have already got wrong will result in a message you have already guessed this letter try another one.
Entering any number or symbol will result in a oops this isnt a letter message.
Entering the correct word will result in a message you won
Loosing the game will result in a loss message but also a message that will tell you what the correct hidden word was. So the player will always finish knowing what the hidden word was. 
Hangman Display will give the player 6 tries to guess the word. Each letter wrong is another peice to the hangman display. 


Future features for a lives count on the screen to keep tabs on how many are left. Adding some visuals, hangman title to make it look more visial pleasing as looks quite bland.




# Testing
Testing in github terminal and heroku...
Family testing the game on the terminal.

# Bugs

solved and unfixed

Numbers and symbols were still allowed to be entered with loosing a life - needed to make a function for this to work and then use this function in my main while loop
The word that was chosen at random was showing on the terminal - i forgot to remove the print statment, once removed all fixed. The player will not see the word they have to guess already on the screen. 
No statment was given for loosing - so game wasnt finished when lost. Needed to add hangman(len(...)
Wasnt visually pleasing to have each turn ontop of one another. Fixed this with a print statement with = at first but then changed this to * as I found it more visially pleasing. 
Hangman display needed to be put in a function with print statments around for it to work
lowercase letters needed to change to upper in order for them to be uppercase when guessed.


# Validator testing
Using Python CI Linter tester, the only error left that I after correcting the rest was "ERROR: W605 invalid escape sequence '\ '". Only the hangman displays with the backslash in were effected.

# Deployment (heroku)
Following the steps that Code Insitute have shown me to do....


# Credits
Tutorial-[Tech With Mike](https://www.youtube.com/channel/UCnvj-t_xNcB0ap82KoEm8mQ)
Tutorial-[Kylie Ying](https://www.youtube.com/watch?v=cJJTnI22IF8)
Tutorial-[Shaun Halverson](https://www.youtube.com/watch?v=pFvSb7cb_Us)
Tutorial-[Kite](https://www.youtube.com/watch?v=m4nEnsavl6w)