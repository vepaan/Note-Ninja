from flask import Flask,render_template, request, url_for
import os

app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def main():
    return render_template("index.html", active="home")

@app.route('/notes')
def notes():
    files =[]
    folder_path = "notes"
    if os.path.exists(folder_path):
        all_files = os.listdir(folder_path)
        all_files.remove(".DS_Store")
        files = [(i,f.split(" ")[-1].split(".")[0]) for i,f in enumerate(sorted(all_files),start=1)]
        links = [f"{folder_path}/{file}" for file in files]
    return render_template("notes.html", active="notes",files=zip(files,links))

@app.route('/login')
def login():
    return render_template("login.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")