from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
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

login_manager_app = LoginManager(app)

csrf = CSRFProtect()

@login_manager_app.user_loader
def load_user(id):
    return userModel.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        
        user= User(0, request.form['username'], request.form['password'])
        logged_user= userModel.login(db, user)
        
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            
            flash("Invalid password...")
            return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@app.route('/home')
@login_required
def home():
    return render_template('home.html')


def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return '<h1>Un monkey se robo esta pagina, por eso no existe.</h1>', 404

if (__name__ == '__main__'):
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()