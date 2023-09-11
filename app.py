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
        all_files = os.listdir(folder_path)
        file_names = [f for f in sorted(all_files)]
        files = [(i," ".join(f.split(" ")[1::]).split(".")[0]) for i,f in enumerate(sorted(all_files),start=1)]
        links = [f"{folder_path}/{file}" for file in file_names]
        files_phy=zip(files,links)

    folder_path = "static/notes/chemistry"
    if os.path.exists(folder_path):
        all_files = os.listdir(folder_path)
        file_names = [f for f in sorted(all_files)]
        files = [(i," ".join(f.split(" ")[1::]).split(".")[0]) for i,f in enumerate(sorted(all_files),start=1)]
        links = [f"{folder_path}/{file}" for file in file_names]
    return render_template("notes.html", active="notes",files_phy=files_phy,files_chem=zip(files,links))

@app.route('/login')
def login():
    return render_template("login.html",active=None)

@app.route('/practice')
def practice():
    return render_template("practice.html",active="practice")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")