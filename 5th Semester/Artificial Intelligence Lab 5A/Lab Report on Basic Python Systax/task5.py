def spellbook_manager():
    spellbook = {}  # Initialize an empty spellbook
    
    while True:
        print("\n--- Wizard's Spellbook Manager ---")
        print("1. Add a new spell")
        print("2. Update a spell's power")
        print("3. Remove a spell")
        print("4. View all spells")
        print("5. Find the most powerful spell")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            spell = input("Enter the spell name: ")
            power = int(input(f"Enter the power level for '{spell}': "))
            spellbook.update({spell: power})
            print(f"'{spell}' has been added to the spellbook with power level {power}.")
        
        elif choice == '2':
            spell = input("Enter the spell name to update: ")
            if spell in spellbook:
                new_power = int(input(f"Enter the new power level for '{spell}': "))
                spellbook[spell] = new_power
                print(f"'{spell}' has been updated to power level {new_power}.")
            else:
                print(f"'{spell}' is not in the spellbook.")
        
        elif choice == '3':
            spell = input("Enter the spell name to remove: ")
            if spell in spellbook:
                spellbook.pop(spell)
                print(f"'{spell}' has been removed from the spellbook.")
            else:
                print(f"'{spell}' is not in the spellbook.")
        
        elif choice == '4':
            if spellbook:
                print("The spellbook contains the following spells:")
                for spell, power in spellbook.items():
                    print(f"Spell: {spell}, Power Level: {power}")
            else:
                print("The spellbook is empty.")
        
        elif choice == '5':
            if spellbook:
                most_powerful = max(spellbook, key=spellbook.get)
                print(f"The most powerful spell is '{most_powerful}' with a power level of {spellbook[most_powerful]}.")
            else:
                print("The spellbook is empty.")
        
        elif choice == '6':
            print("Exiting the Wizard's Spellbook Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice, please select a valid option.")

# Run the spellbook manager program
spellbook_manager()
