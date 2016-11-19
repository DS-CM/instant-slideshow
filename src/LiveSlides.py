import sys
from GetImage import GetImage

"""
    Format is:

    MicrosoftAPI 12345676
"""
def parseKeys(apikeysFile):
    keys = {}

    try:
        with open(apikeysFile) as keysFile:
            for line in keysFile:
                (service, key) = line.split(" ")
                keys[service] = key.strip("\n")
    except IOError as err:
        print("ERROR:\t Cannot open:\t ", apikeysFile, "\n\t Because:\t ", err)
        sys.exit(1)
    
    return keys


"""
    Start everything off.
"""
def main():
    try :
        script, apikeysFile = sys.argv

        keys = parseKeys(apikeysFile)
        bing = GetImage(keys["microsoftapi"])
        url = bing.getImage(["code", "programming"])
    except ValueError as err:
        print("ERROR:\t Run LiveSlides as the follows:\t python LiveSlides.py <apikeys file> ")

if __name__ == "__main__":
    main()
