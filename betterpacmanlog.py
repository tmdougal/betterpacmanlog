#betterpacmanlog.py
#Parses lines of text in pacman log to show only what packages you've installed with 'pacman -S'. Filters out
#dependencies, packages you've uninstalled with '-R or 'Rns', and the multiple '-Syu's in the file.

filePath = "/var/log/pacman.log"

p1Filter1 = "[ALPM] installed "
p1Filter2 = "[ALPM] transaction completed"

allLinesList = []
p1ParsedLinesList = []
p1SkippedLinesList = []

#Take each line from the log file and put into a list.
with open (filePath, "rt") as logFile:
    for line in logFile:
        allLinesList.append(line.rstrip('\n'))

#For each index in the list, compare the current index to p1Filter1
#and the next index to p1Filter2, and add to current to p1ParsedLinesList
#if both criteria are met.
for i in range(len(allLinesList) - 1):
    if p1Filter1 in allLinesList[i]:
        if p1Filter2 in allLinesList[i + 1]:
            p1ParsedLinesList.append(allLinesList[i])

for element in p1ParsedLinesList:
    print(element

