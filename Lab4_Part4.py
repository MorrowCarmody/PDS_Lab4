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
        # HINT: use recursion
        Tower(n-1, start, end, helper)
        print(f'Move disk {n} from {start} to {end}.')
        return

Tower(3, 'A', 'B', 'C')

"""
> 1 DISK
Move disk 1 from START to END

> 2 DISKS
Move disk 1 from START to HELPER
Move disk 2 from START to END
Move disk 1 from HELPER to END

> 3 DISKS
Move disk 1 from START to END
Move disk 2 from START to HELPER
Move disk 1 from END to HELPER
Move disk 3 from START to END
Move disk 1 from HELPER to START
Move disk 2 from HELPER to END
Move disk 1 from START to END

"""