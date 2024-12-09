import random

def high_low_game():
    # The computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    print("Welcome to the High-Low Game!")
    print("I have picked a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            # Ask the player to guess the number
            guess = int(input("Enter your guess: "))
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Provide feedback based on the player's guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number: {secret_number}")
            break

# Run the High-Low game
high_low_game()
