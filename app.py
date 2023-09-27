from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_oauthlib.client import OAuth
from dotenv import load_dotenv
from termcolor import cprint
import secrets
import os
from copy import deepcopy

app = Flask(__name__)
load_dotenv()
app.secret_key = secrets.token_hex(16)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Initialize Flask-OAuthlib
oauth = OAuth(app)
# Replace with your Google OAuth credentials
google = oauth.remote_app(
    'google',
    consumer_key=os.getenv('GOOGLE_CLIENT_ID'),
    consumer_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    request_token_params={
        'scope': ["profile",'email'],
        'include_granted_scopes': 'true',
    },
    base_url='https://accounts.google.com/o/oauth2/v2/auth',
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


# Example User class (you should replace this with your user management system)
class User(UserMixin):
    def __init__(self, id):
        self.id = id


# Simulated user database (replace this with your real user management system)
users = {"user_id": User("user_id")}  # Replace "user_id" with actual user data


@login_manager.user_loader
def load_user(user_id):
    return users[user_id]

@app.context_processor
def inject_data():
    if not session.get("user_info",False):
        session["user_info"] = {}
    return dict(user_info=session["user_info"])



@app.route('/')
def main():
    return render_template("index.html", active="home")


@app.route('/notes')
@login_required
def notes():
    files = []
    folder_path = "static/notes/physics"
    if os.path.exists(folder_path):
        file_names = sorted(os.listdir(folder_path))
        files = [(" ".join(f.split(" ")[1::]).split(".")[0], f"{folder_path}/{f}") for f in
                 sorted(file_names, key=lambda f: int(f.split(" ")[0]))]
        files_phy = files

    folder_path = "static/notes/chemistry"
    if os.path.exists(folder_path):
        file_names = sorted(os.listdir(folder_path))
        files = [(" ".join(f.split(" ")[1::]).split(".")[0], f"{folder_path}/{f}") for f in
                 sorted(file_names, key=lambda f: int(f.split(" ")[0]))]

    return render_template("notes.html", active="notes", files_phy=files_phy, files_chem=files)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = 'user_id'
        if user_id in users:
            user = users[user_id]
            login_user(user)
            message = "Login successful"
            return redirect(url_for('notes'))
        else:
            message = "Login failed. Invalid user ID."

        return render_template("login.html", active=None,message=message)
    if current_user.is_authenticated:
        return redirect(url_for("account"))
    return render_template("login.html", active=None)

@app.route("/account")
@login_required
def account():
    return render_template("account.html",user_info=session["user_info"])

@app.route('/google/login')
def google_login():
    print(url_for('google_authorized', _external=True))
    return google.authorize(callback=url_for('google_authorized', _external=True))


@app.route('/google/authorized')
def google_authorized():
    response = google.authorized_response()
    if response is None:
        cprint('Google login failed.', 'red')
        return redirect(url_for('login'))

    access_token= (response['access_token'], '')
    session['google_token'] = access_token
    user_id = "user_id"
    user_info = google.get('https://www.googleapis.com/oauth2/v3/userinfo').data
    session['user_info'] = user_info
    

    # Simulated user database
    if user_id not in users:
        users[user_id] = User(user_id)

    login_user(users[user_id])
    # Store the Google access token in the session

    return redirect(url_for('notes'))


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


@app.route('/google/logout')
@login_required
def google_logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


@app.route('/practice')
@login_required
def practice():
    files = []
    folder_path = "static/questions/physics"
    if os.path.exists(folder_path):
        file_names = sorted(os.listdir(folder_path))
        files = [" ".join(f.split(" ")[1::]).split(".")[0] for f in
                 sorted(file_names, key=lambda f: int(f.split(" ")[0]))]
        files_phy = enumerate(files,start=1)

    folder_path = "static/questions/chemistry"
    if os.path.exists(folder_path):
        file_names = sorted(os.listdir(folder_path))
        files = [" ".join(f.split(" ")[1::]).split(".")[0] for f in
                 sorted(file_names, key=lambda f: int(f.split(" ")[0]))]
        files = enumerate(files,start=1)

    return render_template("practice.html", active="practice", files_phy=files_phy, files_chem=files)

@app.route('/quiz',methods=['GET', 'POST'])
@login_required
def quiz():
    if request.method == "POST":
        if "file" in request.form:
            session['stats'] = {'score':0,'attempted':0}
            file = request.form.get('file')
            session['question_loaded'] = True
            with open(f"static/questions/{file}.csv","r") as f:
                session['datas'] = [line.strip().split(",") for line in f.readlines()]
                session['question_bank'] = deepcopy(session['datas'])
                session['answer_bank'] = [data[1] for data in session['datas']]
                    
            
        else:
            session['stats']['attempted'] +=1
            if session['answer'] == request.form['answer']:
                session['stats']['score'] +=1
            print(session['stats'])
        if not session['datas']:
            return redirect('/answerpage')
        data = session['datas'].pop()
        session['mode'] = data.pop(-1)
        session['answer'] = data[1]
        session['data'] = data
        return redirect('/quiz')
    if 'data' not in session:
        session['data'] = []
    return render_template('quiz.html',data=session['data'])

@app.route('/answerpage')
def answerpage():
    print(session['stats'])
    if 'question_bank' in session:
        return render_template("answerpage.html",data_set=zip(session['question_bank'],session['answer_bank']),stats = session['stats'])
    return "<h1>No data to be shown</h1>"


@app.route('/logout')
def logout():
    logout_user()
    session["user_info"].clear()
    return redirect(url_for('login'))


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.errorhandler(401)
def not_found(e):
    return login()


if __name__ == "__main__":
    app.run(debug=True, port=5000)