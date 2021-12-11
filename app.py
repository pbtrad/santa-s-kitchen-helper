from calendar import monthrange
from datetime import datetime
from authlib.integrations.flask_client import OAuth
import certifi
from flask import (
    Flask, url_for, render_template,
    redirect, request, session, flash, abort)
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo
import bcrypt
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests
from pip._vendor import cachecontrol
import requests
from os import PathLike

if os.path.exists("env.py"):
    import env

from dotenv import load_dotenv
load_dotenv()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)

app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

# mongo envs
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
# Corrects authentication certificate error
client = MongoClient(os.environ['MONGO_URI'], tlsCAFile=certifi.where())
db = client.kitchenHelper

# Google Credentials
app.config["GOOGLE_CLIENT_ID"] = os.environ.get("GOOGLE_CLIENT_ID")
app.config["GOOGLE_CLIENT_SECRET"] = os.environ.get("GOOGLE_CLIENT_SECRET")


mongo = PyMongo(app)

records = db.users


@app.route("/")
def hello_world():
    # displays DB call format and users
    try:
        if session['email']:
            logged_in = 1
    except KeyError:
        logged_in = 0


    users = list(db.users.find())
    return render_template("index.html",
        users=users, logged_in=logged_in
    )


# Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    message = ''
    #if method post in index
    if "email" in session:
        return redirect(url_for("profile"))
    if request.method == "POST":
        user = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        #if found in database showcase that it's found 
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('register.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('register.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('register.html', message=message)
        else:
            #hash the password and encode it
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            #assing them in a dictionary in key value pairs
            user_input = {'name': user, 'email': email, 'password': hashed}
            #insert it in the record collection
            records.insert_one(user_input)
            
            #find the new created account and its email
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            #if registered redirect to logged in as the registered user
            return render_template('profile.html', email=new_email)
    return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("profile"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #check if email exists in database
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            #encode the password and check if it matches
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('profile'))
            else:
                if "email" in session:
                    return redirect(url_for("profile"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)
# Login


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("logout.html")
    else:
        return render_template('register.html')


# Provisional Profile
@app.route("/profile", methods=["GET", "POST"])
def profile():
    # grab session users username from database
    if "email" in session:
        user = records.find_one({"email": session["email"]})
        return render_template('profile.html', user=user)
    else:
        return redirect(url_for("login"))


@app.route("/profile/edit<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if "email" not in session:
        flash("You need to login to perform this action")
        return redirect(url_for('home'))
    user = records.find_one({"_id": ObjectId(user_id)})
    print(user)
    print(user_id)
    if request.method == "POST":
        if request.form.get('username'):
            user['name'] = request.form.get('username')
        if request.form.get('email'):
            user['email'] = request.form.get('email')
        """if request.form.get('password'):
            if check_password_hash(
                    user["password"], request.form.get("old_password")):
                user['password'] = generate_password_hash(
                    request.form.get("password"))"""
        db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user}
        )
    return redirect(url_for('profile'))

    # mongo.db.users.find(user_info)
# Create Event

@app.route("/event", methods=["GET", "POST"])
def event():
    if request.method == "POST":
        event = {
            "name": request.form.get("name"),
            "date": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "event": request.form.get("event_food"),
            "email": session["email"],
            "family": request.form.get("family"),
            "description": request.form.get("description"),
            "active": request.form.get("active"),
        }
        mongo.db.events.insert_one(event)
        flash("Event Successfully Added")
        return redirect(url_for("profile"))
    events = mongo.db.events.find().sort("date_posted", -1)
    return render_template("profile.html", events=events)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


'''
# GOOGLE LOGIN

client_secrets_file = os.path.join(os.PathLike.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=os.environ.get("GOOGLE_CLIENT_ID")
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/profile")
'''

