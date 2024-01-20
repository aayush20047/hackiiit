from flask import Blueprint , render_template , url_for ,redirect

auth = Blueprint("auth" , __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/Sign-up")
def signup():
    return render_template("signup.html")

@auth.route("/logout")
def logout():
     return redirect(render_template(url_for("views.home")))
