import sys, time
from threading import Thread
from GetImage import GetImage
from Speech2Text import Speech2Text
from bottle import Bottle, run, static_file

url = ""
app = Bottle()
keys = []

"""
    Format is:

    MicrosoftAPI 12345676
"""
def parseKeys(apikeysFile):
    keys = {}
    try:
        with open(apikeysFile) as keysFile:
            for line in keysFile:
                (service, key) = line.split(" : ")
                keys[service] = key.strip("\n")
    except IOError as err:
        print("ERROR:\t Cannot open:\t ", apikeysFile, "\n\t Because:\t ", err)
        sys.exit(1)
    return keys

def getKeywords():
    global url
    global keys

    bing = GetImage(keys["microsoftapi"])
    listener = Speech2Text()
    url = bing.getImage(listener.listen())
    time.sleep(5)
    getKeywords()

@app.route("/")
@app.route("/<filepath:path>")
def index(filepath="index.html"):
    return static_file(filepath, root="")

@app.route("/imagelink")
def image():
    print(url)
    return url

"""
    Start everything off.
"""
def main():
    global url
    global keys
    
    try :
        script, apikeysFile = sys.argv
        keys = parseKeys(apikeysFile)
        t1 = Thread(None, getKeywords)
        t1.daemon = True
        t1.start()
        run(app, host="localhost", port=8080)
    except ValueError as err:
        print("ERROR:\t Run LiveSlides as the follows:\t python LiveSlides.py <apikeys file> ")

if __name__ == "__main__":
    main()
