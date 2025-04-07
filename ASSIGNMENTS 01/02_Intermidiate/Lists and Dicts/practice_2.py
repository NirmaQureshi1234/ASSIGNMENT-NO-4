def access_element(lst, index):
    """Access an element at a specified index."""
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range!"

def modify_element(lst, index, new_value):
    """Modify an element at a specified index."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    return "Index out of range!"

def slice_list(lst, start, end):
    """Slice the list between the given indices."""
    if start < 0 or end > len(lst) or start > end:
        return "Invalid slice range!"
    return lst[start:end]

def index_game():
    # Initialize a list with at least 5 different elements
    my_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Initial list:", my_list)

    while True:
        print("\nOptions:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        choice = input("Select an operation (1/2/3/4): ")

        if choice == '1':
            # Access an element
            index = int(input("Enter the index to access: "))
            print("Result:", access_element(my_list, index))
        elif choice == '2':
            # Modify an element
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated list:" if isinstance(result, list) else "Error:", result)
        elif choice == '3':
            # Slice the list
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print("Sliced list:", slice_list(my_list, start, end))
        elif choice == '4':
            # Exit the game
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    index_game()
