from flask import Flask, render_template, redirect, url_for, request, session

app=Flask(__name__)
app.secret_key="Grey"

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/user")
def user():
	usr=session.get("user")
	if "user" in session:
		return render_template("user.html")
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))

@app.route("/login", methods=["POST","GET"])
def login():
	if request.method=="POST":
		usr=request.form["uname"]
		return redirect(url_for("user"))
		flash("Logged in successfully!")
	elif "user" in session:
		flash("Already Logged in")
		return redirect(url_for("user"))
	else:
		return render_template("login.html")
		
@app.route("/logout")
def logout():
	flash("You have been Logged out!", "info")
	session.pop("user", None)
	return redirect(url_for("login"))

@app.route("/signup", methods=["POST","GET"])
def signup():
	if request.method=="POST":
		usr=request.form["uname"]
		return redirect(url_for("user"))
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
