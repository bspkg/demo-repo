#!/usr/bin/env python

# This function takes a button colour as input and returns the corresponding robot name.
def summon_bot(button_colour):
    if button_colour == 'Gold':
        return 'C3P0'  # If the button colour is Gold, return 'C3P0'
    elif button_colour == 'Blue':
        return 'R2D2'  # If the button colour is Blue, return 'R2D2'
    else:
        return 'Unknown'  # If the button colour is neither Gold nor Blue, return 'Unknown'


# Example usage
print(summon_bot('Gold'))  # Output: C3P0
print(summon_bot('Blue'))  # Output: R2D2
print(summon_bot('Red'))   # Output: Unknown

# Unit tests for summon_bot function
def test_summon_bot():
    assert summon_bot('Gold') == 'C3P0'
    assert summon_bot('Blue') == 'R2D2'
    assert summon_bot('Red') == 'Unknown'
    assert summon_bot('Green') == 'Unknown'

test_summon_bot()
