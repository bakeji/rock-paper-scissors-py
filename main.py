import random
play =True
while play == True:
    player=str (input("'r' for rock, 'p' for paper, 's' for scissors.enter your option here: "))
    player=player.lower()
    computer = random.choice(['r','s','p'])
    if player == computer:
            print ("you and the computer picked the same option. it's a tie! pick another option\n".format(computer))
            if play ==True:
                continue
    elif ( player=='r'and computer== 'p') or (player == 'r'and computer== 's') or (player== 's'and computer== 'p'):
            print ("you picked {} while the computer picked {}, YOU WON!".format(player,computer))
            play =False
        

    elif ( player== 's'and computer== 'r') or (player== 'p'and computer== 'r') or (player== 'p'and computer == 's'):
            print ("you picked {} while the computer picked {}, YOU LOSE!". format(player, computer))
            if play==True:
                    continue

              
    else:
            print("ERROR! You have to select one of the options available" )
           


