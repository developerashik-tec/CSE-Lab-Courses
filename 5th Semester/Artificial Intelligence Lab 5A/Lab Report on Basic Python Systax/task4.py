def backpack_manager():
    backpack = []  # Initialize an empty backpack
    
    while True:
        print("\n--- Backpack Manager ---")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View the contents")
        print("4. Check for an item")
        print("5. Sort the items")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            if item not in backpack:
                backpack.append(item)
                print(f"'{item}' has been added to the backpack.")
            else:
                print(f"'{item}' is already in the backpack.")
        
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in backpack:
                backpack.remove(item)
                print(f"'{item}' has been removed from the backpack.")
            else:
                print(f"'{item}' is not in the backpack.")
        
        elif choice == '3':
            if backpack:
                print("The backpack contains the following items:")
                for item in backpack:
                    print(f"- {item}")
            else:
                print("The backpack is empty.")
        
        elif choice == '4':
            item = input("Enter the item to check: ")
            if item in backpack:
                print(f"'{item}' is in the backpack.")
            else:
                print(f"'{item}' is not in the backpack.")
        
        elif choice == '5':
            if backpack:
                backpack.sort()
                print("The backpack contents have been sorted:")
                for item in backpack:
                    print(f"- {item}")
            else:
                print("The backpack is empty, nothing to sort.")
        
        elif choice == '6':
            print("Exiting the Backpack Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice, please select a valid option.")

# Run the backpack manager program
backpack_manager()
