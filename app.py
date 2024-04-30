from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world(): 
    return render_template("home.html")

@app.route("/first")
def render_first(): 
    return render_template("first.html")

@app.route("/second")
def render_second():
    return render_template("second.html")

@app.route("/ref")
def render_ref(): 
    return render_template("ref.html")