from flask import Flask
import random
app = Flask(__name__)

from markupsafe import escape


"""
via Windows CMD this is how you start the app
> set FLASK_APP=main
> flask run
 * Running on http://127.0.0.1:5000/
"""


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"



@app.route('/')
def run_script():
    file = open(r'C:/Users/hriggs/Downloads/pythonscripts/GuessNumberGame.py', 'r').read()
    return exec(file)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/about')
def about():
    return 'The about page'

#This won't work on localhost, you could do some hostfile trickery to get around it, I was just curious how flask handled subdomains though.
@app.route('/', subdomain ='help')
def practice():
    return "This is a subdomain in my Flask web app"

