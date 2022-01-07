# lets create a guess game using the random.randint 
# amd if elif statement

import random


def UserGuess(x):
    guess = 0
    guessnumber = random.randint(1, x)
    while guess != guessnumber:
        guess = int(input("Enter a guess number: "))
        if(guess < guessnumber):
            print(f"Number {guess} is low")
        elif(guess > guessnumber):
            print(f"Number {guess} is high")
        
    print(f"!YE, Correct, you guess the number {guessnumber} !!")
            

def ComGuess(x):
   feedback =''
   low = 0
   high =x
   while feedback != 'c':
       if low != high:
            comp_guess = random.randint(low, high)
       else:
           comp_guess = low
           
       print(f"Is the bot guess {comp_guess} low(l), high(h) or correct(c) ??")
       feedback = input(": ".lower())
       if feedback == 'h':
         high =   comp_guess-1
       elif feedback == 'l':
           low = comp_guess +1
       
   print(f"!YE, Bot was able to guess your number {comp_guess}")
           
           

if __name__ == "__main__":
    game_menu = input("play us a User(1) or let bot play(2): ")
    if game_menu == '1':
        guess_range = int(input("Enter guess range(2 and above): "))
        UserGuess(guess_range)
    else:
        guess_range = int(input("Enter guess range(2 and above): "))
        ComGuess(guess_range)