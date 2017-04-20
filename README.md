# Instant Slideshow

Hack OHIO 2016 project.

# Project Discription

Make an app or website that makes a slideshow for you as you talk. Approach:

- Use [Google Cloud Speech API](https://cloud.google.com/speech/) to recognize the words that presenter is saying.
- Pipe the words to Flickr to get nice images
- Automatically create fancy, animated slides with nice images and important words/transitions.
- Have a **meme** percentage to give your slides more pizazz! 

**Idea submitted by Arnab Nandi([site](http://arnab.org))**

# Install Instructions

Install all of the following:

- [Uberi/speech_recognition](https://github.com/Uberi/speech_recognition)
- [Bottle](http://bottlepy.org/docs/dev/tutorial.html#quickstart-hello-world)
- [Reveal.js](https://github.com/hakimel/reveal.js)

# Setup

**NOTE**: this is a Python 3 application

1. Install the `requirements.txt` with:

    ```
    pip install -r requirements.txt
    ```

2. Setup your API keys as environment variables:

    ```bash
    export microsoftapi="<Bing image grab key>"
    ```

3. Run the server with:

    ```
    python LiveSlides.py
    ```

4. Navigate to `localhost:8080/` and use the application!
