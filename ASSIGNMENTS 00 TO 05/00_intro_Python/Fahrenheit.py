"""
Program: Fahrenheit to Celsius Converter
-----------------------------------------
This program converts a temperature in Fahrenheit to Celsius
using the formula: degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
"""

def main():
    # Step 1: Prompt the user to enter the temperature in Fahrenheit
    # The input is taken as a string and converted to a float
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Step 2: Convert the Fahrenheit temperature to Celsius
    # The conversion formula is applied
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Step 3: Print the converted temperature with a formatted message
    # Using f-string to format the output
    print(f"Temperature: {fahrenheit}F = {celsius}C")


# This line ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
