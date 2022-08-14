from flask_app import app, render_template, request, redirect, session, flash, bcrypt
from flask_app.models.user import User


# ! ROOT ROUTE
# ! renders form
@app.route('/')
def home():
    return render_template('index.html')

########################################################################################

# ! REGISTER
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register/user', methods=["POST"])
def register_user():
    print(request.form)
    if not User.validate_user(request.form):
        print("validate")
        return redirect('/')
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : bcrypt.generate_password_hash(request.form['password'])
    }
    print(data)
    user_id = User.save(data)
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    return redirect('/dashboard')

########################################################################################

# ! LOGIN
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/user', methods = ['post'])
def login_user():
    data = {'email': request.form['email']}
    user_in_db = User.get_one_email(data)
    if not user_in_db:
        flash('Invalid email/password')
        return redirect ('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect ('/')
    session['user_email'] = user_in_db.email
    return redirect('/dashboard')

# ! DASHBOARD
@app.route('/dashboard/<int:id>') 
def show_user():
    if 'user_id' not in session:
        return redirect ('/logout')
    data = data
    return f"Welcome {session['first_name']}"
    # data = {'id': id}
    # user = User.get_one(data)
    # return render_template('show_user.html', user = user)

########################################################################################

# TODO LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

########################################################################################
# ! EDIT
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
    return redirect('/dashboard')