#!/usr/bin/env python

def droid_name(color):
    if color == 'Gold':
        return 'C3P0'
    elif color == 'Blue':
        return 'R2D2'
    else:
        return 'Unknown'

# Example usage
print(droid_name('Gold'))  # Output: C3P0
print(droid_name('Blue'))  # Output: R2D2
print(droid_name('Red'))   # Output: Unknown