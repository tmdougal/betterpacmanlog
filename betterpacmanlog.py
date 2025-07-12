#betterpacmanlog.py
#Parses lines of text made during install, and through updates via pacman-Syu.
#Also filters out entries for dependencies.

filePath = "/var/log/pacman.log"

initialParsedData = []
initialSkippedData = []
finalParsedData = []
finalSkippedData = []

currentLine = ""
lastLine = ""

wantedLine = ["transaction started", "PACMAN"] 
notWantedLine = ["+0000] [", "--noconfirm"]

counter = -1
wlCounterLength = len(wantedLine)
wlCounterMax = wlCounterLength-1

#Initial data parsing
with open (filePath, "rt") as logFile:
    for line in logFile:
        counter = -1
        while counter < wlCounterMax:
            counter = counter + 1
            if wantedLine[counter] in line:
                initialParsedData.append(line.rstrip('\n'))
            else:
                initialSkippedData.append(line.rstrip('\n'))

#Final data parsing
for element in initialParsedData:
    if not notWantedLine[0] in element:
        finalParsedData.append(element)
    else:
        finalSkippedData.append(element)

for element in finalParsedData:
    print(element)
            
#function for troubleshooting
def printElements(passedList):
    for element in passedList: print(element)
