#!/usr/bin/env python

# This function takes as input the colour of the button pressed and returns the corresponding robot name on the display terminal.
def summon_bot(button_colour):
    if button_colour == 'Gold':
        return 'C3PO'  # If the button colour is Gold, return 'C3PO'
    elif button_colour == 'Blue':
        return 'R2D2'  # If the button colour is Blue, return 'R2D2'
    else:
        return 'Unrecognised button colour' # If the button colour is neither Gold nor Blue, return 'Unrecognised button colour'

# This generates output for the function when the file is run
print(summon_bot('Gold'))  # Output: C3PO
print(summon_bot('Blue'))  # Output: R2D2
print(summon_bot('Red'))  # Output: Unrecognised button colour