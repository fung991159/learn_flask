from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
