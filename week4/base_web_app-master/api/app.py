import os

from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#from config import Config
from config import Config
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secret"
app.permanent_session_lifetime = timedelta(minutes=1)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


from models import users  # Included at the end of the imports to avoid circular imports Issue
from models import products


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", content=None)


@app.route("/users", methods=["GET"])
def get_users():
    if request.method == "GET":
        users_list = users.get_tables(users.Users)
        print(users_list)
        if len(users_list) < 1:
            response = jsonify({"msg": "No users Stored"})
            response.status_code = 400
            return response
        else:
            data_response = {}
            for user in users_list:
                data_response[user.name] = user.to_json()
            content = json.dumps(data_response, indent=4, sort_keys=True)
            return render_template("users.html", content=content)


@app.route("/email/update/", methods=["GET","POST"])  # url_example = /email/update/?name=jhon&newemail=algo@nn.com
def update_user_email():
    if request.method == "GET":
        argss = request.args.to_dict()

        user = users.get_user_by_name(users.Users, argss["name"])
        user.email = argss["newemail"]
        db.session.commit()
        new_user = users.get_user_by_name(users.Users,  argss["name"])
        return render_template("users.html", content=new_user.to_json())


@app.route("/users/add/", methods=["GET", "POST"])  # url_example = users/add/?name=andy&email=algo3@nn.com&passwd=ref543232
def add_user():
    if request.method == "GET":
        argss = request.args.to_dict()
        if users.get_user_by_name(users.Users, argss["name"]):
            return render_template("users.html", content={"msg": "User Already exist"})
        new_user = users.Users(name=argss["name"], email=argss["email"], password_hash=argss["passwd"])
        db.session.add(new_user)
        db.session.commit()
        new_user = users.get_user_by_name(users.Users, argss["name"])
        return render_template("users.html", content=new_user.to_json())


@app.route("/users/name/<name>/", methods=["GET"])
@app.route("/users/<name>/", methods=["GET"])
def get_user_by_name(name):
    if request.method == "GET":
        user = users.get_user_by_name(users.Users, name)
        return render_template("users.html", content=user.to_json())


@app.route("/users/emails", methods=["GET"])
def get_users_emails():
    if request.method == "GET":
        emails = users.get_users_emails(users.Users)
        return emails


@app.route("/users/email/<email>/", methods=["GET"])
@app.route("/users/emails/<email>/", methods=["GET"])
def get_user_by_email(email):
    if request.method == "GET":
        user = users.get_user_by_email(users.Users, email)
        return render_template("users.html", content=user.to_json())


@app.route("/users/delete/email/", methods=["GET"])
@app.route("/users/delete/byemail/", methods=["GET"])  # url_example = /users/delete/email/?email=john4@nn.com
def delete_user_by_email():
    if request.method == "GET":
        argss = request.args.to_dict()
        email = argss["email"]

        deleted_user = users.delete_user_by_email(users.Users, email=email)
        db.session.commit()
        flash("User deleted by email successfully", "warning")
        return get_users()


@app.route("/users/delete/name/", methods=["GET"])
@app.route("/users/delete/byname/", methods=["GET"])  # url_example = /users/delete/name/?name=john4@nn.com
def delete_user_by_name():
    if request.method == "GET":
        argss = request.args.to_dict()
        name = argss["name"]

        deleted_user = users.delete_user_by_name(users.Users, email=name)
        db.session.commit()
        flash("User deleted by name successfully", "warning")
        return get_users()


@app.route("/create_account", methods=["POST", "GET"])
def create_account():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.does_user_exist(users.Users, name=user)  # If user doesnt exist
        if found_user:
            session["email"] = found_user.email
            session["password_hash"] = found_user.password_hash
        else:
            usr = users.Users(user, "", "", "")
            db.session.add(usr)
            db.session.commit()

        flash("User logged in Successfully", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("user"))
        return render_template("create_account.html")


@app.route("/products", methods=["GET"])
def get_products():
    if request.method == "GET":
        elements = products.get_tables(products.Products)
        content = None
        if len(elements) < 1:
            content = json.dumps({"msg": "No Products Stored"}, indent=4, sort_keys=True)
        else:
            data_response = {}
            for element in elements:
                data_response[element.title] = element.to_json()
            content = json.dumps(data_response, indent=4, sort_keys=True)
        return render_template("products.html", content=content)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.does_user_exist(users.Users, name=user)
        if found_user:
            session["email"] = found_user.email
            session["password_hash"] = found_user.password_hash
        else:
            usr = users.Users(user)
            db.session.add(usr)
            db.session.commit()

        flash("User logged in Successfully", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.does_user_exist(users.Users, user)
            found_user.email = email
            db.session.add
            db.session.commit()
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user2.html", email=email)
    else:
        flash("You're not logged in", "info")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0')
    db.create_all()
    migrate.init_app()
