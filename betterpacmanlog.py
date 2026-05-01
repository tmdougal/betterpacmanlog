#betterpacmanlog.py
#Parses lines of text in pacman log to show only what packages you've installed with 'pacman -S'. Filters out
#dependencies, packages you've uninstalled with '-R or 'Rns', and the multiple '-Syu's in the file.

filePath = "/var/log/pacman.log"

p1Filter= "[PACMAN] Running"

allLinesList = []
p1ParsedLinesList = []
p1SkippedLinesList = []

with open (filePath, "rt") as logFile:
    for line in logFile:
        allLinesList.append(line.rstrip('\n'))
        if p1Filter in line:
            p1ParsedLinesList.append(line.rstrip('\n'))
        else:
            p1SkippedLinesList.append(line.rstrip('\n'))

for element in p1ParsedLinesList:
    print(element)

