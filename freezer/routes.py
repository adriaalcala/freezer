from flask import Blueprint, request, render_template, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from pony.orm.core import commit, select

from freezer.connection import db
from freezer.forms import LoginForm
from freezer.models import User


api = Blueprint('Freezer', __name__)


@api.route('/')
@api.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@api.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        users = select(u for u in User if u.name == form.name.data and u.password == form.password.data)
        if len(users) != 1:
            flash('Invalid name or password')
            return redirct('/login')
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@api.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@api.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        with db.db_session:
            user = User(name=form.name.data, password=form.password.data)
            commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)