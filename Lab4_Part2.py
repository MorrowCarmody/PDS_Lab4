# Matt Carmody
# COSC 6375
# Lab 4 Part 2

def Factorial(n):
    """Return the factorial of a number."""
    if(type(n) != int):
        # non-integer value: return nothing and print error message
        print('The input must be an integer.')
    elif(n < 0):
        # negative value: return nothing and print error message
        print('The factorial of a negative value is not possible.')
    else:
        # calculate and return factorial
        total = n
        while(n > 2):
            n = n - 1
            total *= n
        return total

print(Factorial(-1))
print(Factorial(1.2))
print(Factorial(3))