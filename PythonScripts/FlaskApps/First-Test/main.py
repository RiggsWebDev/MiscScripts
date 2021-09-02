from flask import Flask

app = Flask(__name__)

from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/about')
def about():
    return 'The about page'


#This won't work on localhost, you could do some hostfile trickery to get around it, I was just curious how flask handled subdomains though.
@app.route('/', subdomain ='help')
def practice():
    return "This is a subdomain in my Flask web app"
