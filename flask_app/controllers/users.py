from flask_app import app, render_template, request, redirect
from flask_app.models.user import User

# ! CREATE
# ! render form
@app.route('/')
def home():
    return render_template('index.html')

# ! redirect
@app.route('/create/user', methods=["POST"])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/read')

########################################################################################

# ! HOME ROUTE
# ! READ ALL
@app.route('/read')
def index():
    # call the get all classmethod to get all users
    return render_template('read.html', users = User.get_all())

# ! READ ONE
@app.route('/show/<int:id>') 
def show_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

########################################################################################

# ! UPDATE
# ! render form
@app.route('/edit/<int:id>')
def edit_user(id):
    data = {'id': id}
    return render_template('edit_user.html', user = User.get_one(data))

# ! redirect
@app.route('/update/user', methods = ["post"])
def update_user():
    print(request.form)
    User.update(request.form)
    return redirect('/read')
    # return redirect(f"/show/{request.form['id']}")

########################################################################################

# ! DELETE
@app.route('/delete/<int:id>')
def delete_user(id):
    User.destroy({'id': id})
    return redirect('/')