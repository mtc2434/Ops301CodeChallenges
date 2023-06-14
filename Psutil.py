#!/usr/bin/env python3
# Script:  Psutil.py                     
# Author:  Marcelo Clark                      
# Date of latest revision:   6/14/2023   
# Purpose:  Install Psutil.

#Create a Python script that fetches this information using Psutil:

#Time spent by normal processes executing in user mode
#Time spent by processes executing in kernel mode
#Time when system was idle
#Time spent by priority processes executing in user mode
#Time spent waiting for I/O to complete.
#Time spent for servicing hardware interrupts
#Time spent for servicing software interrupts
#Time spent by other operating systems running in a virtualized environment
#Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

import psutil


utilities = psutil.cpu_times() 

print("User Process Time", utilities.user)
print("Time Kernel Execution Time", utilities.system)
print("Idle Time", utilities.idle) 
print("User Priority Process Execution Time", utilities.nice)
print("I/O Completion Time", utilities.iowait)
print("Hardware Interrupt Servicing Time", utilities.irq)
print("Software Interrupt Servicing Time", utilities.softirq)
print("Virtualized Environment Time", utilities.steal)
print("Virtual CPU under Linux Kernel Time", utilities.guest)

#End
