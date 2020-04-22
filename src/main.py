from flask import Flask, render_template, request


app = Flask('Programmer-Job Searcher')

@app.route('/')
def home():
    return render_template("home.html")

app.run()