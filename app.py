from calendar import monthrange
# from datetime import datetime
import datetime
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
# from pip._vendor import cachecontrol
import requests
# from os import PathLike
if os.path.exists("env.py"):
    import env

# os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)

# app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

# mongo envs
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
# Corrects authentication certificate error
client = MongoClient(os.environ['MONGO_URI'], tlsCAFile=certifi.where())
db = client.kitchenHelper

# Google Credentials
# app.config["GOOGLE_CLIENT_ID"] = os.environ.get("GOOGLE_CLIENT_ID")
# app.config["GOOGLE_CLIENT_SECRET"] = os.environ.get("GOOGLE_CLIENT_SECRET")


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


@app.route("/contact")
def contact():
    return render_template("contact.html")

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
            year = datetime.date.today().year
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            #session['email'] = user_data
            #if registered redirect to logged in as the registered user
            return redirect(url_for('login', email=new_email, 
                user=user_data, year=year))
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
        #userDoc = db.users.find_one({"email": session['email']})
        all_families = list(db.families.find())
        families = list(db.families.find({"members": user["_id"]}))
        test = db.families.find({"members": {"$not": { user['_id']}}})
        #create eventlist
        eventIds = []
        for family in families:
            event_array = family["events"]
            if event_array:
                for event in event_array:
                    eventIds.append(event)
        events = []
        date_list = []
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        year = datetime.date.today().year
        for month in range(1, 13):
            date_list.append([months[month - 1], monthrange(year,month)[1]])

        # join family list
        # returns all families the user is NOT a part of
        join_family = db.families.find({"members": {"$ne": user["_id"]}})

        # in family list
        # returns all families the user IS a part of
        in_family = db.families.find({"members": user["_id"]})

        # All events from all familes user is a part of
        events_list = {}
        events_list["$or"] = []
        # Aggregates family list into events list
        # try:
        for family in db.families.find({"members": user["_id"]}):
            for event in family["events"]:
                events_list["$or"].append({"_id": ObjectId(event)})

        # Splits events into upcoming and previous
        events_list = db.events.find(events_list)
        event_name_list = []
        upcoming_events = []
        previous_events = []

        try:
            for time_check in events_list:
                event_date = time_check['date']
                day = event_date[0:2].replace("-","")

                if datetime.datetime(int(event_date[6:10]), int(event_date[3:5]), int(day) ) > datetime.datetime.now():
                    upcoming_events.append(time_check)
                else:
                    previous_events.append(time_check)

            bring_dish_events = upcoming_events
        except Exception as e:
            print(e)
            print("I have lost events")

        # Creates list with event, and food brought
        for event_name in upcoming_events:
            food_list = []
            for food in event_name['food']:
                try:
                    is_bringing = True
                    event_person_id = db.users.find_one({"_id": food[0]})['email']
                    if event_person_id == user["email"]:
                        food_list += [db.users.find_one({"_id": food[0]})['name']] #name
                    else:
                        is_bringing = False
                except TypeError:
                    print("---------Type error through upcomming events list--------")

                for event in food:
                    somelist = []
                    somelist.append(event)

                for food_item in food[1]:
                    food_list += [food_item]

            if food_list != []:
                event_name_list += [[event_name['name'], food_list]]
            else:
                event_name_list += [[event_name['name']]]

        for event in event_name_list:
            print(event)

        event_name_list_previous = []
        # Creates previous list with event, and food brought
        for event_name in previous_events:
            food_list = []
            for food in event_name['food']:
                try:
                    is_bringing = True
                    event_person_id = db.users.find_one({"_id": food[0]})['email']
                    if event_person_id == user["email"]:
                        food_list += [db.users.find_one({"_id": food[0]})['name']] #name
                    else:
                        is_bringing = False
                except TypeError:
                    print("---------Type error through upcomming events list--------")
                if is_bringing:
                    for food_item in food[1]:
                        food_list += [food_item]

            if food_list != []:
                event_name_list_previous += [[event_name['name'], food_list]]
            else:
                event_name_list_previous += [[event_name['name']]]

        try:
            bring_dish_events_list = []
            for event in bring_dish_events:
                bring_dish_events_list += [[event["_id"], event["name"]]]
        except UnboundLocalError:
            pass

        return render_template(
            'profile.html',
            user=user,
            join_family=join_family,
            families=families,
            # all_events_list=all_events_list,
            date_list=date_list,
            year=year,
            event_name_list=event_name_list,
            event_name_list_previous=event_name_list_previous,
            bring_dish_events_list=bring_dish_events_list,
            test=test,
        )
    else:
        return redirect(url_for("login"))
        # return url_for("login")


@app.route("/profile/edit<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if "email" not in session:
        flash("You need to login to perform this action")
        return redirect(url_for('home'))
    user = records.find_one({"_id": ObjectId(user_id)})
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
        event_name = request.form.get('name')
        event_found = db.events.find_one({"name": event_name})
        if event_found:
            flash('Event name already exists')
            return redirect(url_for('profile'))
        else:
            family_name = request.form.get("family")
            year = request.form.get("date_year")
            day = request.form.get("date_day")
            month = request.form.get("date_month")
            print(year, )
            print(family_name)
            event = {
                "name": request.form.get("name"),
                "date":  str(day) + "/" + str(month) + "/" + str(year),
                "event": request.form.get("event_food"),
                "family": family_name,
                "description": request.form.get("description"),
                "active": request.form.get("active"),
                "food": []
            }
            _id = db.events.insert_one(event).inserted_id
            print(_id)
            #add event to families event list
            family = db.families.find_one({"name": family_name})
            print(family)
            events = family["events"]
            print(events)
            events.append(_id)
            family["events"] = events
            db.families.update_one(
            {"_id": ObjectId(family["_id"])},
            {"$set": family}
            )
            flash("Event Successfully Added")
            print('we got here')
            return redirect(url_for("profile"))
    events = db.events.find().sort("date_posted", -1)
    return render_template("profile.html", events=events)


@app.route("/family", methods=["GET", "POST"])
def family():
    if request.method == "POST":
        family_name = request.form.get('family_name')
        family_found = db.families.find_one({"name": family_name})
        if family_found:
            flash("Family name already exists")
            return redirect(url_for("profile"))
        else:
            user = records.find_one({"email": session["email"]})
            family = {
                "name": family_name,
                "date": datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                "events": [],
                "members": [user["_id"]]
            }
            db.families.insert_one(family)
            flash("Family Successfully Added")
            return redirect(url_for("profile"))


@app.route("/add_dish_event/", methods=["GET", "POST"])
def add_dish_event():
    if request.method == "POST":
        event_id = request.form.get('event_id')
        event_found = db.events.find_one({"_id": ObjectId(event_id)})
        user_id = db.users.find_one({"email": session["email"]})["_id"]
        dish_2 = request.form.get("dish_2").strip()
        dish_3 = request.form.get("dish_3").strip()
        dish_4 = request.form.get("dish_4").strip()
        dishes = []
        dish = []
        dishes.append(user_id)
        dish.append(request.form.get("dish_1"))
        if dish_2:
            dish.append(request.form.get("dish_2"))
        if dish_3:
            dish.append(request.form.get("dish_3"))
        if dish_4:
            dish.append(request.form.get("dish_4"))

        dishes.append(dish)

        iteration = 0
        food_list = event_found["food"]
        list_length = len(event_found["food"])
        if list_length == 0:
                food_list.append(dishes)
        else:
            for find_dishes in event_found["food"]:
                if user_id == find_dishes[0]:
            #         # print(find_dishes)
                    food_list[iteration] = dishes
                    break
                if iteration >= list_length - 2:
                    food_list.append(dishes)
                    break

                iteration += 1

        db.events.update_one(
            {"_id": ObjectId(event_id)},
            {"$set": event_found})
        flash("Dish Successfully Added")
        return redirect(url_for("profile"))



@app.route("/add_to_family/<user_id>", methods=["GET", "POST"])
def add_to_family(user_id):
    if request.method == 'POST':
        family_name = request.form.get("all_families_name")
        print(family_name)
        if db.families.count_documents({"name": family_name}) == 0:
            return redirect(url_for("profile"))
        print(family_name)
        family = db.families.find_one({"name": family_name})
        print(family)
        members = family["members"]
        print(members)
        members.append(ObjectId(user_id))
        print(members)
        family["members"] = members
        print(family)
        db.families.update_one(
            {"_id": family["_id"]},
            {"$set": family}
        )
        return redirect(url_for("profile"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)


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