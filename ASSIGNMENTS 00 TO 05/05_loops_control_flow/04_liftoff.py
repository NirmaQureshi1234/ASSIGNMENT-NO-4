def main():
    for i in range(10, 0, -1):  # Start from 10, go to 1, decrement by 1
        print(i, end=" ")       # Print numbers on the same line with a space
    print("Liftoff!")           # Print "Liftoff!" after the countdown

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
