"""App configuration module."""
from flasgger import Swagger  # type: ignore
from flask import Flask, request, jsonify
from flask_login import LoginManager

from flask_cors import CORS  # type: ignore
from flask_compress import Compress  # type: ignore
from flask_httpauth import HTTPBasicAuth  # type: ignore
from werkzeug.security import check_password_hash

from freezer.constants import VALID_name_PASSWORD_PAIRS
from freezer.models import User
from flask import Blueprint, request, render_template, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from pony.orm.core import commit, select, db_session

from freezer.connection import db
from freezer.forms import LoginForm, RegistrationForm, AddMeal, DeleteMeal
from freezer.models import User, Meal, Unity, Category, SubCategory

app = Flask(__name__, static_url_path='/', static_folder='docs/_build/')
app.config['SECRET_KEY'] = 'you-will-never-guess'

db.generate_mapping()
# Enable cors
CORS(app)
# Compress all responses with gzip
Compress(app)

auth = HTTPBasicAuth()

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(_id):
    with db_session:
        return User.select(lambda u: u.id == int(_id)).first()


@app.route('/')
@app.route('/index')
@login_required
def index():
    with db_session:
        meals = Meal.select(lambda m: m.user == current_user).order_by(Meal.expiration_date, Meal.id)[:]
    return render_template('index.html', title='Home', meals=meals)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        with db_session:
            print(form.name.data, form.password.data)
            user = User.select(lambda u: u.name == form.name.data and u.password == form.password.data).first()
        if not user:
            flash('Invalid name or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        print(next_page)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = redirect('/index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form = RegistrationForm()
    if form.validate_on_submit():
        with db_session:
            user = User(name=form.name.data, password=form.password.data)
            commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)


@app.route('/add_meal', methods=['GET', 'POST'])
def add_meal():
    form = AddMeal()
    with db_session:
        form.unity.choices = [(u.symbol, u.symbol) for u in Unity.select()]
        form.category.choices = [(c.id, c.description) for c in Category.select()]
        form.subcategory.choices = [(s.id, s.description) for s in SubCategory.select()]
    if form.validate_on_submit():
        with db_session:
            meal = Meal(
              buy_date = form.buy_date.data, 
              expiration_date = form.expiration_date.data, 
              freezing_date = form.freezing_date.data, 
              description = form.description.data, 
              units = form.units.data, 
              weight = form.weight.data, 
              unity = Unity.select(lambda u: u.symbol == form.unity.data).first(),
              category = Category.select(lambda u: u.id == form.category.data).first(),
              subcategory = SubCategory.select(lambda u: u.id == form.subcategory.data).first(),
              drawer = form.drawer.data,
              user = current_user
            )
            commit()
        return redirect('/index')
    return render_template('add_meal.html', title='Add Meal', form=form)


@app.route('/delete_meal', methods=['GET', 'POST'])
def delete_meal():
    form = DeleteMeal()
    if form.validate_on_submit():
        with db_session:
            Meal[form.meal_id.data].delete()
            commit()
        return redirect('/index')
    return render_template('delete_meal.html', title='Add Meal', form=form)


@auth.verify_password
def verify_password(name, password):
    if name in VALID_name_PASSWORD_PAIRS and \
            check_password_hash(VALID_name_PASSWORD_PAIRS.get(name), password):
        return name

app.config["SWAGGER"] = {
    "title": "Performance rules",
    "uiversion": 3,
}

swag = Swagger(
    app,
    decorators=[auth.login_required],
    template={
        "swagger": "2.0",
        "info": {
            "title": "Performance rules",
            "version": "1.0",
        },
        "consumes": [
            "application/json",
        ],
        "produces": [
            "application/json",
        ],
    },
)


@app.route('/docs', methods=['GET'])
@app.route('/docs/<path:path>', methods=['GET'])
@auth.login_required
def docs(path='index.html'):
    """Library documentation endpoint.
    ---
    tags:
        - Docs
    parameters:
        - name: path
          in: path
          description: Path to documentation
    responses:
        200:
            description: Documentation
    """
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(debug=True)
