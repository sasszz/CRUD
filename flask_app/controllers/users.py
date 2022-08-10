from flask_app import app, render_template, request, redirect

from flask_app.models.user import User

@app.route("/")
def index():
    # call the get all classmethod to get all users
    return render_template("index.html")


@app.route('/users/new')
def new_user():
    return render_template("read.html", users = User.get_all())

@app.route('/create/user', methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users/new')