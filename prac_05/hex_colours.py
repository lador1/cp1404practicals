"""Look up hexadecimal colour codes"""

COLOUR_NAME_TO_CODE = {'AliceBlue': '#f0f8ff', 'Amethyst': '#9966cc', 'AntiqueWhite': '#faebd7',
                       'Alizarin crimson': '#e32636',
                       'Apricot': '#fbceb1', 'Baby Pink': '#f4c2c2', 'Banana Yellow': '#ffe135',
                       'Bittersweet Shimmer': '#bf4f51'}

colour_name = input("Enter name of colour: ")
while colour_name != "":  # While there is valid input
    try:
        print(colour_name, ':', COLOUR_NAME_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour")
    colour_name = input("Enter name of colour: ")
