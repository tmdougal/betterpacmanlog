#betterpacmanlog.py
#Filters out all log entries made automatically, like during initial install
#or through updates via pacman-Syu. Also filters out entries for dependencies.

filePath = "/var/log/pacman.log"

initialParsedData = []
finalParsedData = []
skippedData = []

counter1 = 0

substr1 = "PACMAN"
substr2 = "transaction started"
substr3 = "+0000] ["
substr4 = "--noconfirm"

 
with open (filePath, "rt") as logFile: 
    for line in logFile:
        if substr1 in line:
            initialParsedData.append(line.rstrip('\n'))
        elif substr2 in line:
            initialParsedData.append(line.rstrip('\n'))
        else:
            skippedData.append(line.rstrip('\n'))
            
for element in initialParsedData:
    if not substr3 in element:
        if not substr4 in element:
            finalParsedData.append(line)
            print(element)
            
