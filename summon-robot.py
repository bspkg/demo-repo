#!/usr/bin/env python

# This function takes as input the colour of the button pressed and returns the corresponding robot name on the display terminal.
def summon_bot(button_colour):
    if button_colour == 'Gold':
        return 'C3PO'  # If the button colour is Gold, return 'C3PO'
    elif button_colour == 'Blue':
        return 'R2D2'  # If the button colour is Blue, return 'R2D2'
    else:
        return 'Unrecognised button colour' # If the button colour is neither Gold nor Blue, return 'Unrecognised button colour'

# Example usage
print(summon_bot('Gold'))  # Output: C3PO
print(summon_bot('Blue'))  # Output: R2D2
print(summon_bot('Red'))  # Output: Unrecognised button colour

# Generate unit tests for summon_bot function
def test_summon_bot():
    assert summon_bot('Gold') == 'C3PO'
    assert summon_bot('Blue') == 'R2D2'
    assert summon_bot('Red') == 'Unrecognised button colour'
    assert summon_bot('Green') == 'Unrecognised button colour'

test_summon_bot()  # Run the unit tests