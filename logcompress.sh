#!/bin/bash

# Script:  logclear.sh                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/6/2023   
# Purpose:   Create a script that compresses log data and compares it to the original                

#Note: run sudo apt-get install zip in terminal for compression software

# Declaration of variables

# Time of compression
filetime=$(date +"%Y%m%d%H%M%S")

#Declaring the backup directory location
dir_backup="/var/log/backups"

# Main


#Prints the file sizes before being compressed down
echo "File Sizes before compression:"
ls -l /var/log/syslog
ls -l /var/log/wtmp
echo ""

#Compresses the  log files to "dir_backup", or the backup directory
mkdir -p "$dir_backup"
zip "$dir_backup/syslog-$filetime.zip" /var/log/syslog
zip "$dir_backup/wtmp-$filetime.zip" /var/log/wtmp

#Clears the log files
truncate --size 0 /var/log/syslog
truncate --size 0 /var/log/wtmp

#Prints the compressed file sizes to the screen
echo "Compressed file sizes:"
ls -l "$dir_backup/syslog-$filetime.zip"
ls -l "$dir_backup/wtmp-$filetime.zip"
echo ""

#Non compresses vs compressed file sizes
echo "Original vs Compressed"
echo "Original log file sizes:"
du -h /var/log/syslog
du -h /var/log/wtmp
echo "Compressed file sizes:"
du -h "$dir_backup/syslog-$filetime.zip"
du -h "$dir_backup/wtmp-$filetime.zip"
