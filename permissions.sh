#!/bin/bash

# Script:  permissions.sh                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/1/2023   
# Purpose:    create a bash script that alters file permissions of everything in a directory.                 

# Declare global variables

# Declare functions

#Main 

# Echos text to prompt input for directory path
echo "Please enter the Directory path"

# The input for the directory path
read Dirpath

# Echos text to prompt for the permissions number
echo "Enter the permissions number"

#input for the permissions number
read pnumber

#navigates to the directory path we input earlier
cd "$Dirpath" 

#changes the rwx permissions based on the number we input. the -R is for changing all the files in the directory for the permissions to change. The * is for all directories in that directory to change.
chmod -R "$pnumber" *

ls -l "$Dirpath"

# End
