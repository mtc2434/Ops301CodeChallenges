#!/bin/bash

# Script:  Conditionalmenu.sh                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/5/2023   
# Purpose:   Create a bash script that launches a menu system with different options                  

# Declare global variables



# Declare functions

# Main
while true; do
    # Displays options for menu 
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    echo -n "Enter your choice: "
    
    #will read user inputs "choice"
     read choice
