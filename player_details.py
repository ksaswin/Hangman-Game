import pickle


player_name = 'Anonymous'
score = 0
highscore_dict = {1: ['default', '0'],
                  2: ['default', '0'],
                  3: ['default', '0'],
                  4: ['default', '0'],
                  5: ['default', '0'] }


def player_info():
    print("\nPlease type in your name (or hit enter to skip)")
    player_name = input("Your name: ")
    
    if not ((player_name.find(' ') >= 0) or (player_name.find('.') >= 0)):
        if not player_name.isalpha():
            player_name = 'Anonymous'
    return player_name


def highscoreUpdate(player_name, score):                                        #Update the highscores
    with open('highscores.pickle', 'rb') as handle:                             #Prints the current highscores
        highscore_dict = pickle.load(handle)
    if highscore_dict[1][0] == 'default':                                       #First time updating a player score
        highscore_dict[1].clear()
        highscore_dict[1].append(player_name)
        highscore_dict[1].append(str(score))
    else:
        for i in range(1, 6):
            if score == int(highscore_dict[i][1]):                              #Two players sharing same score
                highscore_dict[i].append(player_name)
                highscore_dict[i].append(str(score))
                if len(highscore_dict[i]) > 4:
                    del highscore_dict[i][0]
                    del highscore_dict[i][0]
                break
            if score > int(highscore_dict[i][1]):                                #Update score
                temp = highscore_dict[i].copy()
                highscore_dict[i].clear()
                highscore_dict[i].append(player_name)
                highscore_dict[i].append(str(score))
                for j in range((i+1), 6):
                    temp1 = highscore_dict[j].copy()
                    highscore_dict[j].clear()
                    for k in temp:
                        highscore_dict[j].append(k)
                    temp = temp1
                break      
        
    with open('highscores.pickle', 'wb') as handle:
        pickle.dump(highscore_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def playerwrite(player_name, points):
    score = points
    with open('scoresheet.txt', 'a') as file:
        file.write(player_name)                                                 #Stores the player name
        file.write(' '*(60-len(player_name)))
        file.write(str(score))                                                  #Stores the points achieved
        file.write('\n')
    
    highscoreUpdate(player_name, score)                                         #Call update highscore

  
def highscorePrint():
    with open('highscores.pickle', 'rb') as handle:                             #Prints the current highscores
        highscore_dict = pickle.load(handle)
    if highscore_dict[1][0] != 'default':
        print('\n\n')
        print((' '*17) + 'HIGH SCORES')
        print('+' + ('-'*44) + '+')
        print('| RANK |' + (' '*9) + 'PLAYER NAME' + (' '*9) + '| ' + 'SCORE |')
        print('-'*46)
        for i in range(1, 6):
            if highscore_dict[i][0] != 'default':
                for j in range(0, len(highscore_dict[i])):
                    if (j%2) == 0:
                        print('|  ' + str(i) + '   |', end='')
                        print(highscore_dict[i][j], end='')
                        print(' '*(29-len(highscore_dict[i][j])), end='')
                        print('| ', end='')
                    else:
                        print(' ', end='')
                        print(highscore_dict[i][j], end='')
                        print(' '*(5-len(highscore_dict[i][j])), end='')
                        print('|')
            else:
                break
        print('+' + ('-'*44) + '+')
        print('\n')

#IF YOUR highsores.pickle FILE IS EMPTY, THEN UNCOMMENT LINES 98 AND 99 AND RUN THIS PROGRAM ONCE.
#AFTER THAT COMMENT THOSE TWO LINES AGAIN AND PLAY THE GAME (RUN hangman_game.py)
#YOU MAY FOLLOW THE SAME PROCEDURES TO RESET THE HIGHSCORES TO DEFAULT VALUE.

#with open('highscores.pickle', 'wb') as handle:                                 #Highscore reset
#    pickle.dump(highscore_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

