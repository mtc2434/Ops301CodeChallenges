#!/bin/bash

# Script:  appendDandT.sh                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/1/2023   
# Purpose:   Create a script that appends the date and time                  

# Declare global variables



# Declare functions

# Main

# copies the date and time to a log file, and creates the log file itself and the name
cp /var/log/syslog "syslog_$(date +"%Y-%m-%d")"
