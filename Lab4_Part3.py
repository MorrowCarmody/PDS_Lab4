# Matt Carmody
# COSC 6375
# Lab 4 Part 3

def Fibonacci(n):
    """Return the Fibonacci Sequence of a number."""
    if(type(n) != int):
        # non-integer value: return nothing and print error message
        print('The input must be an integer.')
    elif(n < 0):
        # negative value: return nothing and print error message
        print('The sequence of a negative value is not possible.')
    else:
        # calculate and return sequence
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        else:
            fib_num = Fibonacci(n - 1) + Fibonacci(n - 2)
            return fib_num

print(Fibonacci(-5))
print(Fibonacci(3.75))
print(Fibonacci(8))