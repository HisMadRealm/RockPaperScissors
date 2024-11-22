import random

def rock_paper_scissors():
    print("Welcome to Rock/Paper/Scissors!")
    options = ["rock", "paper", "scissors"]
    
    while True:
        # User choice
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        if user_choice not in options:
            print("Invalid choice. Try again.")
            continue
        
        # Computer choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

# Run the game
rock_paper_scissors()
