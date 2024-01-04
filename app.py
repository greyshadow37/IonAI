from flask import Flask, render_template, redirect, url_for

app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")
@app.route("/<user>")
def profile(user):
	return render_template("")
@app.route("/login")
def login():
	return render_template("login.html")
@app.route("/signup")
def signup():
	return render_template("signup.html")
@app.route("/home")
def home():
	return render_template("home.html")
@app.route("/about")
def about():
	return render_template("about.html")
@app.route("/news")
def news():
	return render_template("news.html")
@app.route("/forums")
def forums():
	return render_template("forums.html")

if __name__=="__main__":
	app.run(debug=True)
