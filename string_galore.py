#!/usr/bin/env python3

# codename: string_galore.py
# Task: Create a Python script that includes the following:
# author: Marcelo Clark
# Date of last revision: 7/5/2023

# Assign to a variable a list of ten string elements.
shopping_list = ["apple", "banana", "cherry", "marionberry", "blackberry", "mango", "grape", "honeydew", "dragonfruit", "pineapple"]

# Print the 4th element. remember 0=1 for computers
print("element 4:", shopping_list[3])

# Print the sixth through tenth element of the list.
print("elements 6 through 10", shopping_list[5:])

# Change the value of the seventh element to "onion".
shopping_list[6] = "onion"
print("Updated shopping list:", shopping_list)
