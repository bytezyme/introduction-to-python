#!usr/bin/bash python

import sys


# Print out the length of the list
print("Length of sys.argv: {}".format(len(sys.argv)))

# Print out the entire list
print(sys.argv)  

# Loop over each argument and print
for arg in sys.argv:
    print("{}: {}".format(arg, type(arg)))
