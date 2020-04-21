from flask import Flask


app = Flask('Programmer-Job Searcher')

@app.route('/')
def home():
    return "hi"

app.run()