# Matt Carmody
# COSC 6375
# Lab 4 Part 4

moves = 1

def Tower(n, start, helper, end):
    """Move n disks from the start pin to the end pin."""
    global moves
    if(type(n) != int):
        # non-integer value: print error message
        print('The input must be an integer.')
    elif(n < 0):
        # negative value: print error message
        print('The sequence of a negative value is not possible.')
    elif(n == 0):
        return
    else:
        # Recursive call 1
        Tower(n-1, start, end, helper)
        print(f'{moves}. Move disk {n} from {start} to {end}.')
        moves += 1
        # Recursive call 2
        Tower(n-1, helper, start, end)
        return

Tower(6, 'A', 'B', 'C')