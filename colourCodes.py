"""
CP1404/CP5632 Practical
Colour codes in a dictionary
File needs reformatting
"""

COLOUR_CODES = {'white': '#FFFFFF', 'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'black': '#000000'}

colour = input("Enter short state: ").upper()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid short state")
    colour = input("Enter short state: ")

for colour in COLOUR_CODES:
    print("{:4} is {}".format(colour, COLOUR_CODES[colour]))