import sys, time
from threading import Thread
from GetImage import GetImage
from Speech2Text import Speech2Text
from bottle import Bottle, run, static_file, request

url = "images/this-is-not-fine.png"
app = Bottle()
keys = []
topic = ""
memelevel = 0

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
    words = listener.listen()
    if words != None:
        url = bing.getImage(words)
    #time.sleep(2)
    getKeywords()

@app.route("/")
@app.route("/<filepath:path>")
def index(filepath="index.html"):
    return static_file(filepath, root="")

@app.route("/imagelink")
def image():
    print(url)
    return url

@app.route('/settings', method='POST')
def settings():
    global topic, memelevel
    topic = request.forms.get('Topic')
    memelevel = request.forms.get('MemeLevel')
    print("\n>> GOT: \ttopic: {}\n\t\tmemelevel: {}\n".format(topic, memelevel))
    return "<p>Settings Updated</p>"

"""
    Start everything off.
"""
def main():
    global url, keys
    
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
