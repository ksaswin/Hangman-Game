#### Hangman Terminal Game


Hangman Terminal game using Python.<br />
You basically just guess the word and fill the blanks.  
You can either guess a single letter or the word itself.  
You can have a total of 7 wrong guesses for each word.  
Your health will reset after each round.  
Your score will be total number of words you guessed correctly.  
All the scores will be stored in scoresheet.txt file.    
Clone the repository using:
```
git clone https://github.com/ksaswin/Hangman-Game.git
```
You may need to install the pickle module.
```
pip install pickle-mixin
```

If your highscores.pickle file is empty, then uncomment lines 98 and 99 in the player_details.py file.  
Then run the program once:
```
python3 player_details.py
```
After that, comment lines 98 and 99 in player_details.py file again.  
Then run hangman_game.py to play the game.
```
python3 hangman_game.py
```
You may follow the same procedure to reset the highscores back to default value.  
You may need to make changes in the call function in hangman_game.py for it to work in windows terminal.
