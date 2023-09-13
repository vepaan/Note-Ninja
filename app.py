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
    folder_path = "static/notes/physics"
    if os.path.exists(folder_path):
        file_names = sorted(os.listdir(folder_path))
        files = [(" ".join(f.split(" ")[1::]).split(".")[0],f"{folder_path}/{f}" ) for f in sorted(file_names,key=lambda f:int(f.split(" ")[0]))]
        files_phy = files
        
    folder_path = "static/notes/chemistry"
    if os.path.exists(folder_path):
        file_names = sorted(os.listdir(folder_path))
        files = [(" ".join(f.split(" ")[1::]).split(".")[0],f"{folder_path}/{f}" ) for f in sorted(file_names,key=lambda f:int(f.split(" ")[0]))]

    return render_template("notes.html", active="notes",files_phy=files_phy,files_chem=files)

@app.route('/login')
def login():
    return render_template("login.html",active=None)

@app.route('/practice')
def practice():
    return render_template("practice.html",active="practice")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")