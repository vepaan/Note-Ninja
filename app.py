from flask import Flask,render_template, request

app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def main():
    return render_template("index.html", active="home")

@app.route('/notes')
def notes():
    return render_template("notes.html", active="notes")

@app.route('/login')
def login():
    return render_template("login.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")