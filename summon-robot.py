#!/usr/bin/env python

# This function takes a button colour as input and returns the corresponding robot name.
def summon_bot(button_colour):
    if button_colour == 'Gold':
        return 'C3PO'  # If the button colour is Gold, return 'C3PO'
    elif button_colour == 'Blue':
        return 'R2D2'  # If the button colour is Blue, return 'R2D2'

# Example usage
print(summon_bot('Gold'))  # Output: C3PO
print(summon_bot('Blue'))  # Output: R2D2