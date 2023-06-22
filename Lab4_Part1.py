# Matt Carmody
# COSC 6375
# Lab 4 Part 1

def Fahrenheit(t):
    """Convert Celsius to Fahrenheit."""
    F = (9/5)*t+32
    return round(F, 1)

print('The freezing point for water is:',Fahrenheit(0))
print('The boiling point for water is:',Fahrenheit(100))
print('The normal body temperature is:',Fahrenheit(37))
