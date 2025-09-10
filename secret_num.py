import random

def guess():

    secret_number=5
    comp_pick=None
    attempts=0
    
    
    while attempts<4:
        comp_pick=random.randint(1,10)
        print(f"Computer chose:{comp_pick}")
        attempts += 1
        
        if comp_pick==secret_number:
            print("Yay!you guessed correctly!")
            break
        
        elif comp_pick>secret_number:
            print("Pick again,Too high")
            
            
            
        elif comp_pick<secret_number:
            print("Pick again,Too low")
            
    else:
        # this runs if loop finishes without a correct guess
        print("Game over! Better luck next time ")
        
        
    
    again=input("Do you want to play again? Yes or No?: ").lower()
    
    if again=="yes":
        guess()
    else:
        print("Thanks for playing")
        
if __name__=="__main__":
    guess()
        



