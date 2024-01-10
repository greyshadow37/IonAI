from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="Grey"

db=SQLAlchemy(app)

class users(db.Model):
	_id=db.Column("id",db.Integer,primary_key=True)
	name=db.Column(db.String(50))
	email=db.Column(db.String(100))
	def __init__(self,name,email):
		self.name=name
		self.email=email

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    usr = session.get("user", email=email)

    if "user" in session:
        return render_template("user.html")

    if request.method == "POST":
        email = request.form["email"]
        session["email"] = email
        found_user = users.query.filter_by(name=usr).first()
        found_user.email = email
        db.session.commit()
        flash("E-mail was saved!")

    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usr = request.form["uname"]
        found_user = users.query.filter_by(name=usr).first()

        if found_user:
            session["email"] = found_user.email
            db.session.commit()
            flash("Logged in successfully!")
        else:
            user = users(usr, "")
            db.session.add(user)
            db.session.commit()

        return redirect(url_for("user"))

    elif "user" in session:
        flash("Already Logged in")
        return redirect(url_for("user"))
    else:
        return render_template("./login.html")
		
@app.route("/logout")
def logout():
	flash("You have been Logged out!", "info")
	session.pop("user", None)
	session.pop("email", None)
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
