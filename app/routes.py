import datetime

from flask_login import current_user, login_user, logout_user

from app import app, db
from flask import request, redirect, url_for, flash, render_template

from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/updateplayer/<player_id>-<name>-<level>', methods=['GET'])
def create_player(player_id, name, level):

    return ""


@app.route('/index')
def index():
    return ""


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect((url_for('index')))
    return render_template('base.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/register', methods=['GET', 'POST'])
def register_listener():
    now = datetime.datetime.now()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration complete!")
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)