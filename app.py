from flask import Flask, render_template, redirect, url_for, request

app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")
@app.route("/<usr>")
def profile(usr):
	return "<h1>Hello, {usr}!</h1>"
@app.route("/login", methods=["POST","GET"])
def login():
	if request.method=="POST":
		user=request.form["name"]
		return redirect(url_for("./<usr>", usr=user))
	else:
		return render_template("login.html")
@app.route("/signup", methods=["POST","GET"])
def signup():
	if request.method=="POST":
		user=request.form["name"]
		return redirect(url_for("./<usr>", usr=user))
	else:
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
