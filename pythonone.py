import os

# Script Name:                  pythonone.py
# Author:                       Marcelo Clark
# Date of latest revision:      06/07/2023
# Purpose:                      The Python module “os” must be utilized at least three variables must be declared and referenced in Python
                               


#Main
#creates whoami variable
whoami_output = os.popen('whoami').read().strip()

# Executes ip a command an puts output into variable
ip_output = os.popen('ip a').read().strip()

# puts output of 'lshw -short' into a variable
lshw_output = os.popen('lshw -short').read().strip()

# prints the values of the variables
print("Current user:", whoami_output)
print("IP addresses:", ip_output)
print("System hardware information:", lshw_output)

#End





