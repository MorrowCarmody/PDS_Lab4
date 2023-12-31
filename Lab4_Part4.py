# Matt Carmody
# COSC 6375
# Lab 4 Part 4

def Tower(n, start, helper, end):
    """Move n disks from the start pin to the end pin."""
    if(type(n) != int):
        # non-integer value: print error message
        print('The input must be an integer.')
    elif(n < 0):
        # negative value: print error message
        print('The sequence of a negative value is not possible.')
    elif(n == 0):
        return
    else:
        Tower(n-1, start, end, helper)
        print(f'Move disk {n} from {start} to {end}.')
        Tower(n-1, helper, start, end)
        return

Tower(6, 'A', 'B', 'C')
