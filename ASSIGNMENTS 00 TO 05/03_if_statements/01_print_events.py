"""
Program: First 20 Even Numbers
------------------------------
This program prints the first 20 even numbers using a loop.
"""

def main():
    # Loop through the first 20 even numbers
    for i in range(20):
        even_number = i * 2  # Calculate the even number
        print(even_number, end=" ")  # Print the even number on the same line with a space

if __name__ == '__main__':
    main()
