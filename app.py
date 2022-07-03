#https://www.youtube.com/watch?v=MwZwr5Tvyxo&t=1s
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "majjhsfjkhdkfdfdkjfhdhfjd"

@app.route("/hello")
def index():
    flash("What your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", do you want to know your IMC?")
    return render_template("index.html")

@app.route("/measure", methods=["POST", "GET"])
def measure():
    flash("The value  " + str(request.form['number_input']) + ", is your IMC?")
    return render_template("index.html")
