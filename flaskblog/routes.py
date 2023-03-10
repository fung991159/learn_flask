from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegisterationForm, LoginForm
from flaskblog.models import Post, User


posts = [
    {
        "author": "fung yeung",
        "title": "blog post 1",
        "content": "testing!",
        "date_posted": "2022-12-16",
    },
    {
        "author": "Jack yeung",
        "title": "blog post 2",
        "content": "testing2!",
        "date_posted": "2022-12-18",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f"You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash(f"Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="login", form=form)
