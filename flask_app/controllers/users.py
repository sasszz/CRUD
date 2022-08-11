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

@app.route('/show/<int:id>') 
def show_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

@app.route('/delete/<int:id>')
def delete_user(id):
    User.destroy({'id': id})
    return redirect('/')

## ! UPDATE
@app.route('/edit/<int:id>')
def edit_user(id):
    data = {'id': id}
    return render_template('edit_user.html', user = User.get_one(data))

@app.route('/update/user', methods = ["post"])
def update_user():
    print(request.form)
    User.update(request.form)
    return redirect(f"/show/{request.form['id']}")