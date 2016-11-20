import sys, time, random
from threading import Thread
from GetImage import GetImage
from Speech2Text import Speech2Text
from bottle import Bottle, run, static_file, request

url = "images/this-is-not-fine.png"
app = Bottle()
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
    memelevel = int(request.forms.get('MemeLevel'))
    print("\n>> GOT: \ttopic: {}\n\t\tmemelevel: {}\n".format(topic, memelevel))
    return "<p>Settings Updated</p>"


class LiveSlides:
    def __init__(self, microsoftkey):
        random.seed(None, 2)
        self.bing = GetImage(microsoftkey)
        self.listener = Speech2Text()

    def run(self):
        t1 = Thread(None, self.__updateURL)
        t1.daemon = True
        t1.start()

    def __updateURL(self):
        global url, topic, memelevel
        
        while True:
            topicMeme = []

            num = random.randint(0,99)
            if num < memelevel:
                topicMeme = [ topic, "meme" ]
            else:
                topicMeme = [ topic ]

            words = self.listener.listen()
            if words != None:
                newUrl = self.bing.getImage(topicMeme + words)
                if newUrl != None:
                    url = newUrl


"""
    Start everything off.
"""
def main():
    global url
    
    try :
        script, apikeysFile = sys.argv

        keys = parseKeys(apikeysFile)
        liveSlide = LiveSlides(keys["microsoftapi"])
        liveSlide.run()
        run(app, host="localhost", port=8080)
    except ValueError as err:
        print("ERROR:\t Run LiveSlides as the follows:\t python LiveSlides.py <apikeys file> ")

if __name__ == "__main__":
    main()
