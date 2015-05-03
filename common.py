#common tasks
def getFile():
    while True:
        try:
            fname = raw_input("Enter a file name: ")
            fhand = open(fname)
            break
        except:
            print "Try again."

    return fhand


def folderPrompt():
    return raw_input("Enter a target directory: ")
