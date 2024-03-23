def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
number = int(input("Enter a number to calculate its factorial: "))
print("Factorial of", number, "is", factorial(number))
