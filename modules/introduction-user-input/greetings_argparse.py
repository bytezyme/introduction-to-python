#!usr/bin/bash python

import argparse

# Define our parser
parser = argparse.ArgumentParser(description="Pass arguments to generate a greeting!")

# Define an argument that accepts our name
parser.add_argument("name")

# Declare the variable that stores the passed arguments
args = parser.parse_args()
