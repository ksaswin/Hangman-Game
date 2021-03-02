### HANGMAN TERMINAL GAME
<br />
Hangman terminal game using Python.<br />
You are basically just supposed to guess the word.<br />
You can either guess a single letter or the word itself.<br />
You can have a total of 7 wrong guesses for each word, after which you'll die.<br />
Your health will reset after each level.<br />
Your score will be the total number of words you gussed right.<br />
<br />
All the scores will be stored in scoresheet.txt file.<br />
<br />
You will need to install a few python libraries.<br />
<br />
```
pip install pickle-mixin
```
<br /> <br />
If your highscores.pickle file is empty, then uncomment lines 98 and 99 in the player_details.py file.
Then run the program once
```
python3 player_details.py
```
After that, comment lines 98 and 99 in player_details.py file again.<br />
Then run hangman_game.py to play the game.
```
python3 hangman_game.py
```
You may follow the same procedure to reset the highscores back to default value.
