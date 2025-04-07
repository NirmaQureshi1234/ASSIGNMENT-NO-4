"""
Program: Phonebook Example
---------------------------
This program demonstrates the use of dictionaries to manage a phonebook. 
Users can add, view, and search for contact information.
"""

def main():
    # Initialize an empty dictionary for the phonebook
    phonebook = {}
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            # Add a contact
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            phonebook[name] = phone_number
            print(f"Contact '{name}' added successfully!")
        
        elif choice == "2":
            # View all contacts
            if phonebook:
                print("\nPhonebook Contacts:")
                for name, phone_number in phonebook.items():
                    print(f"{name}: {phone_number}")
            else:
                print("The phonebook is empty.")
        
        elif choice == "3":
            # Search for a contact
            search_name = input("Enter the name of the contact to search for: ")
            if search_name in phonebook:
                print(f"{search_name}'s phone number is {phonebook[search_name]}.")
            else:
                print(f"No contact found with the name '{search_name}'.")
        
        elif choice == "4":
            # Exit the program
            print("Exiting the phonebook program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select an option between 1 and 4.")

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
