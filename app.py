from flask import Flask,render_template, request

app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def main():
    return render_template("index.html", active="home")

@app.route('/about')
def about():
    return render_template("index.html", active="about")
