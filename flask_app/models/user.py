# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the user table from our database

import re
from flask import flash, session

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
DATABASE = "users"

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database


    ## ! READ ALL 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append( User(user) )
        return users

    ## ! READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        user = User(result[0])
        return user

    ## ! READ ONE W/ EMAIL
    @classmethod
    def get_one_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        user = User(result[0])
        return user

    ## ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_user(user:dict):
        is_valid = True
        if len(user['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address")
            is_valid = False
        if user['password'] != user['password_confirmation']:
            flash("Passwords must match.")
        return is_valid

    # ## ! UPDATE
    # @classmethod
    # def update (cls, data):
    #     query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # ## ! DELETE/DESTROY
    # @classmethod
    # def destroy(cls, data):
    #     query = " DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)