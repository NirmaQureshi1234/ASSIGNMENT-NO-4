"""
Program: Fruit Shop Calculator
------------------------------
This program calculates the total cost of fruits based on user input and predefined prices.
"""

def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 10.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 4.0
    }
    
    total_cost = 0  # Initialize total cost to 0
    
    print("Welcome to the Fruit Shop!")
    
    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        # Ask the user how many of each fruit they want
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        # Add the cost for this fruit to the total cost
        total_cost += quantity * price
    
    # Print the total cost
    print(f"\nYour total is ${total_cost:.2f}")

# This line ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
