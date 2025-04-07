"""
Program: Mass-Energy Equivalence Calculator
--------------------------------------------
This program continually reads in mass from the user in kilograms
and calculates the equivalent energy using Einstein's famous equation:
E = m * c^2
"""

# Define the constant for the speed of light (C)
SPEED_OF_LIGHT = 299792458  # in meters per second

def main():
    # Step 1: Continuously read mass input from the user
    while True:
        # Prompt the user for mass in kilograms
        mass = float(input("Enter kilos of mass (or enter 0 to quit): "))
        
        # Check if the user wants to exit the program
        if mass == 0:
            print("Exiting the program. Goodbye!")
            break

        # Step 2: Calculate the energy using Einstein's formula
        energy = mass * SPEED_OF_LIGHT**2

        # Step 3: Display the calculation steps and result
        print("\ne = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {SPEED_OF_LIGHT} m/s")
        print(f"{energy} joules of energy!\n")

# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
