def num_in_stock(fruit):
    """
    Returns the number of the given fruit in Sophia's inventory.
    """
    # Sophia's inventory
    inventory = {
        "apple": 50,
        "banana": 25,
        "pear": 1000,
        "orange": 30
    }
    # Return the count of the fruit or 0 if it's not in the inventory
    return inventory.get(fruit.lower(), 0)

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ")
    
    # Get the number of that fruit in stock
    stock = num_in_stock(fruit)
    
    # Print the appropriate message
    if stock > 0:
        print(f"This fruit is in stock! Here is how many:\n{stock}")
    else:
        print("This fruit is not in stock.")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
