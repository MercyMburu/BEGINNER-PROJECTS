import random

def rps_game():
    picks = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0
    
    while True:
        user_choice = input("Choose between rock, paper, scissors: ").lower()
        
        if user_choice not in picks:
            print("Invalid input, enter rock, paper or scissors")
            continue
        
        comp_choice = random.choice(picks)
        
        print(f"Computer chose: {comp_choice}")
        print(f"You chose: {user_choice}")
        
        if user_choice == comp_choice:
            print("It's a draw!")
            
        elif (
            (user_choice == "scissors" and comp_choice == "paper")
            or (user_choice == "rock" and comp_choice == "scissors")
            or (user_choice == "paper" and comp_choice == "rock")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1
            
        print(f"User score: {user_score} | Computer score: {comp_score}")
     
        # End game if someone reaches 3 points   
        if user_score == 3:
            print("🎉 Yay! You win the game!")
            break
        elif comp_score == 3:
            print("🤖 Computer wins the game! Better luck next time!")
            break
    
    # Ask to play again    
    again = input("Do you want to play again? Yes or No?: ").lower()
    
    if again == "yes":
        rps_game()
    else:
        print("Thanks for playing! 👋")
        
            
if __name__ == "__main__":
    rps_game()
