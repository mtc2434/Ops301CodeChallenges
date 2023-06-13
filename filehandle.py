#!/usr/bin/env python3
# Script:  filehandle.py                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/8/2023   
# Purpose:  create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.

# Creates file
f = open("filetest.txt", "w")

# Appending the 3 lines
lines = ["line1", "line2", "line3"]
for line in lines: 
    f.write(line + "\n")

# Opens the file and reads first line
f = open("filetest.txt", "r")
first_line = f.readline()
print("First line:", first_line)
