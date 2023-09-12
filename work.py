from flask import Flask, render_template

work = Flask(__name__)

@work.route("/")
def homepage():
    return render_template("index.html")

@work.route('/')
def hello():
    return "Hello, Devops!."

if __name__== "__main__":
    work.run()