from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_oauthlib.client import OAuth
from dotenv import load_dotenv
from termcolor import cprint
import secrets
import os

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
        'scope': "email",
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
user_info = {}


@login_manager.user_loader
def load_user(user_id):
    return users[user_id]

@app.context_processor
def inject_data():
    return dict(user_info=user_info)


@app.route('/')
def main():
    print(user_info)
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
        user_id = secrets.token_hex(32)
        print(request.form['password'])
        print(request.form['uname'])
        print(request.form.get('remember',False))
        if user_id in users:
            user = users[user_id]
            login_user(user)
            return redirect(url_for('notes'))
        else:
            message = "Login failed. Invalid username or password."

        return render_template("login.html", active=None,message=message)
    cprint(user_info,'yellow')
    if current_user.is_authenticated:
        return redirect(url_for("account"))
    return render_template("login.html", active=None)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users['qwe'] = User("qwe")

        return render_template("login.html", active=None,message="")
    if current_user.is_authenticated:
        return redirect(url_for("account"))
    return render_template("signup.html", active=None)

@app.route("/account")
@login_required
def account():
    return render_template("account.html",user_info=user_info)

@app.route('/google/login')
def google_login():
    print(url_for('google_authorized', _external=True))
    return google.authorize(callback=url_for('google_authorized', _external=True))


@app.route('/google/authorized')
def google_authorized():
    global user_info
    response = google.authorized_response()
    if response is None:
        cprint('Google login failed.', 'red')
        return redirect(url_for('login'))

    access_token= (response['access_token'], '')
    session['google_token'] = access_token
    user_id = "user_id"
    user_info = google.get('https://www.googleapis.com/oauth2/v2/userinfo').data

    

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
def practice():
    return render_template("practice.html", active="practice")

@app.route('/logout')
def logout():
    logout_user()
    user_info.clear()
    return redirect(url_for('login'))


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.errorhandler(401)
def not_found(e):
    return login()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
