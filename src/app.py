from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

from config import config

# Models
from models.UserModel import userModel

# Entities 
from models.entities.User import User

pymysql.install_as_MySQLdb()

app = Flask(__name__)
db = pymysql.connect(
        host= config['development'].DB_HOST,
        user= config['development'].DB_USER,
        password= config['development'].DB_PASSWORD, 
        database= config['development'].DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        
        user= User(0, request.form['username'], request.form['password'])
        logged_user= userModel.login(db, user)
        
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('home'))
            
            flash("Invalid password...")
            return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
        
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/home')
def home():
    return render_template('home.html')

if (__name__ == '__main__'):
    app.config.from_object(config['development'])
    app.run()