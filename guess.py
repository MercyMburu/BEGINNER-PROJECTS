import random

def guess_game():
    
    number = random.randint(1, 10)
    guess = None

    while number!=guess:
        
        guess=int(input("Guess a number between 1 and 10: "))
        
        if guess>number:
            print("Guess is too high,try again!")
            
        if guess<number:
            print("Guess is too low,try again!")
        
    print("Yay!You guessed the correct number")
        
    
if __name__=="__main__":
    guess_game()