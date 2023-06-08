#!/usr/bin/env python3
# Script:  generatedir.py                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/8/2023   
# Purpose:Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

# Import libraries

import os


def generate_directory_structure(d_path):



for (root, dirs, files) in os.walk(d_path):  
   
    print("==root==")
    print(root)
   
    print("==dirs==")
    print(dirs)
   
    print("==files==")
    print(files)

# Main
user_input = input("Please enter the directory path: ")
generate_directory_structure(user_input)



# End
