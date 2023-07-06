#!/bin/bash

# Script:  Conditionalmenu.sh
# Author:  Marcelo Clark
# Date of latest revision:   7/5/2023
# Purpose:   Create a bash script that launches a menu system with different options

# Declare functions

# Display menu function
print_menu() {
  echo "Menu:"
  echo "1. Hello world"
  echo "2. Ping self"
  echo "3. IP info"
  echo "4. Exit"
  echo -n "Enter your choice: "
}

# handle_choice is a function to read user input and give output of choice
handle_choice() {
  read -r choice
  case $choice in
    1) echo "Hello world";;
    2) ping -c 4 127.0.0.1;;
    3) ifconfig;;
    4) exit;;
    *) echo "Not a valid choice. Please enter a number 1-4";;
  esac
}

# Main
while true; do
  print_menu
  handle_choice
done
