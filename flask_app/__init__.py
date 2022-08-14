from flask import Flask, render_template, request, redirect, session, flash
# import the class from user.py
from flask_bcrypt import Bcrypt        

app = Flask(__name__)
app.secret_key = 'Any string you wish, but KEEP DO NOT SHARE IT'

bcrypt = Bcrypt(app)    # we are creating an object called bcrypt