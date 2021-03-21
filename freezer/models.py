from datetime import date
from pony.orm.core import PrimaryKey, Required, Optional, Set, select
from freezer.connection import db
from flask_login import UserMixin



class Meal(db.Entity):
    id = PrimaryKey(int, auto=True)
    buy_date = Required(date)
    expiration_date = Required(date)
    freezing_date = Required(date)
    description = Required(str)
    units = Required(int)
    weight = Required(float)
    unity = Required('Unity')
    category = Required('Category')
    subcategory = Optional('SubCategory')
    drawer = Optional(int)
    user = Required('User')


class User(db.Entity, UserMixin):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    password = Required(str)
    meals = Set(Meal)


class Unity(db.Entity):
    symbol = PrimaryKey(str)
    meals = Set(Meal)


class SubCategory(db.Entity):
    id = PrimaryKey(int, auto=True)
    description = Required(str, unique=True)
    category = Required('Category')
    meals = Set(Meal)


class Category(db.Entity):
    id = PrimaryKey(int, auto=True)
    description = Required(str, unique=True)
    subcategories = Set(SubCategory)
    meals = Set(Meal)
