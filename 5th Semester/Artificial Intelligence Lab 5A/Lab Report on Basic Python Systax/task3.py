def affirmation_program():
    correct_affirmation = "I am capable of doing anything I put my mind to."
    
    print("Welcome! Let's reinforce a positive mindset.")
    
    while True:
        # Prompt the user to type the affirmation
        print("\nPlease type the following affirmation exactly:")
        print(correct_affirmation)
        user_input = input("Your input: ")
        
        # Check if the user typed the affirmation correctly
        if user_input == correct_affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmm, that was not the affirmation. Please try again.")
    
# Run the affirmation program
affirmation_program()
