import common
import string

fhand = common.getFile()
otherFile = open("first file", "w")
for line in fhand:
    if line.startswith("a1z4"):

        newLine = line[4:]
        newLine = newLine.translate(None, string.punctuation)
        newLine = newLine.lstrip()

        print newLine
        otherFile = open(newLine, "w")
        otherFile.write(newLine)
    otherFile.write(line)
