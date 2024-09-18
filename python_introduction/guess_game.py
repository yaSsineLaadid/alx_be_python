import random

def guess_game():
    # Generate a secret number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Initialize the guess counter
    attempts = 0
    correct_guess = False
    
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    
    while not correct_guess:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("That's not a valid number. Please enter an integer.")
            continue
        
        # Increment the guess counter
        attempts += 1
        
        # Use if-elif-else to evaluate the guess
        if guess == secret_number:
            print("Congratulations, you guessed it in {} attempts!".format(attempts))
            correct_guess = True
        elif guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        else:  # guess < secret_number
            print("Nope, your guess is a bit low. Give it another shot!")
    
    # Ask if the player wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_game()
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
guess_game()

