import random
 


def play():
    user = input("What's your choice, 'r' Rock, 'p' paper, 's' Scissors: \n")
    comp = random.choice(['r','p','s'])
    
    if user == comp:
        return "it's a Tie"
    
    if win_checker(user, comp):
        return "!Ye, You Won"
    
    return "You Lose, Bot won"
        

def win_checker(player, oppo):
    if(player == 'r' and oppo =='s') or (player =='s' and oppo == 'p') or (player =='p' and oppo == 'r'):
            return True
    else:
        return False
    
    
    
if __name__ == "__main__":
    print(play())