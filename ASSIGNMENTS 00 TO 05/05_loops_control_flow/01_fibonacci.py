def main():
    MAX_VALUE = 10000  # Maximum value for Fibonacci terms
    fib_0, fib_1 = 0, 1  # Initial Fibonacci terms

    print(fib_0, end=" ")
    while fib_1 < MAX_VALUE:
        print(fib_1, end=" ")
        fib_0, fib_1 = fib_1, fib_0 + fib_1  # Update the Fibonacci sequence

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
