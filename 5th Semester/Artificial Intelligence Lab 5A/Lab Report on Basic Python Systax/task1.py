

def nimm_game():
    # Start with 20 stones in the pile
    stones = 20
    # Set the current player to player 1
    current_player = 1
    
    # Continue the game until there are no stones left
    while stones > 0:
        print(f"\nStones remaining: {stones}")
        # Ask the current player to take 1 or 2 stones
        try:
            take = int(input(f"Player {current_player}, take 1 or 2 stones: "))
        except ValueError:
            print("Invalid input, please enter 1 or 2.")
            continue
        
        # Check if the input is valid (1 or 2 stones)
        if take not in [1, 2]:
            print("Invalid move! You can only take 1 or 2 stones.")
            continue

        # Check if there are enough stones to take
        if take > stones:
            print(f"There are only {stones} stones left. You cannot take {take} stones.")
            continue
        
        # Update the number of stones left
        stones -= take
        
        # Check if the game is over (no stones left)
        if stones == 0:
            print(f"\nPlayer {current_player} took the last stone. Player {current_player} loses!")
            break
        
        # Switch to the other player
        current_player = 2 if current_player == 1 else 1

# Run the game
nimm_game()
