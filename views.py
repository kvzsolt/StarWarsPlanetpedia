from flask import render_template, request, redirect, session
import requests
from data_manager import DataManager
from database_connector import Database
import utils

db_instance = Database()
dm = DataManager(db_instance)


def get_user_input():
    username = request.form.get('username')
    password = request.form.get('password')
    return username, password


def index():
    if request.method == 'POST':
        source = request.form.get('nextbutton') or request.form.get('prevbutton')
        if source and source != 'None':
            try:
                data = requests.get(source).json()
            except requests.RequestException:
                return render_template('error.html')

            return render_template('index.html', data=data)

    try:
        data = requests.get('https://swapi.py4e.com/api/planets/').json()
    except requests.RequestException:
        return render_template('error.html')

    return render_template('index.html', data=data)


def register():
    if request.method == 'GET':
        return render_template('register.html')

    username, password = get_user_input()

    if not username or not password:
        return redirect('/register')

    hashed_pw = utils.hash_password(password)
    if dm.get_users_for_login(username):
        return render_template('register.html', taken=True)

    dm.add_user(username, hashed_pw)
    session['username'] = username
    return redirect('/planets')


def login():
    if request.method == 'GET':
        return render_template('login.html')

    username, password = get_user_input()

    if not username or not password:
        return redirect('/login')

    user = dm.get_users_for_login(username)
    hashed_password = dm.get_password_for_login(username)
    if not user or not utils.verify_password(password, hashed_password['password']):
        return redirect('/login')

    session['username'] = username
    return redirect('/planets')


def logout():
    session.pop('username', None)
    return redirect('/')