from pony.orm.core import *

from datetime import datetime

from freezer.connection import db
from freezer.models import User, Unity, Category, SubCategory, Meal

db.generate_mapping(check_tables=False)
db.drop_all_tables(with_all_data=True)
db.create_tables()

@db_session
def populate_database():
    if select(u for u in User).count() > 0:
        return
    
    neus = User(name="Neus", password="532683")
    grams = Unity(symbol="g")
    carn = Category(description="carn")
    pollo = SubCategory(description="pollo", category=carn)
    ternera = SubCategory(description="ternera", category=carn)
    porc = SubCategory(description="porc", category=carn)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Osobuco", units=1, weight=263, unity=grams, category=carn, subcategory=ternera, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Costella aguja", units=2, weight=215, unity=grams, category=carn, subcategory=porc, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Costella aguja", units=1, weight=175, unity=grams, category=carn, subcategory=porc, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Costella aguja", units=1, weight=197, unity=grams, category=carn, subcategory=porc, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Costella aguja", units=1, weight=169, unity=grams, category=carn, subcategory=porc, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Costella aguja", units=1, weight=153, unity=grams, category=carn, subcategory=porc, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Costella aguja", units=1, weight=162, unity=grams, category=carn, subcategory=porc, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Costella aguja", units=1, weight=135, unity=grams, category=carn, subcategory=porc, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Filete extra fino pechuga", units=10, weight=317, unity=grams, category=carn, subcategory=pollo, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Filetes de muslo sin piel", units=3, weight=275, unity=grams, category=carn, subcategory=pollo, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Filetes de muslo sin piel", units=3, weight=265, unity=grams, category=carn, subcategory=pollo, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Filetes de muslo sin piel", units=3, weight=359, unity=grams, category=carn, subcategory=pollo, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Filetes de muslo sin piel", units=2, weight=275, unity=grams, category=carn, subcategory=pollo, drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Hueso espinazo (caldo)", units=2, weight=213, unity=grams, category=carn, subcategory=ternera,drawer=5, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Trasero marinado", units=1, weight=364, unity=grams, category=carn, subcategory=pollo,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Carcasa (caldo)", units=1, weight=157, unity=grams, category=carn, subcategory=pollo,drawer=5, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Carcasa (caldo)", units=1, weight=156, unity=grams, category=carn, subcategory=pollo,drawer=5, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Estofado", units=2, weight=300, unity=grams, category=carn, subcategory=ternera,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Estofado", units=2, weight=290, unity=grams, category=carn, subcategory=ternera,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Trasero marinado", units=1, weight=340, unity=grams, category=carn, subcategory=pollo,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Trasero marinado", units=1, weight=335, unity=grams, category=carn, subcategory=pollo,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Resto estofado (caldo)", units=1, weight=60, unity=grams, category=carn, subcategory=ternera,drawer=5, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Carn picada", units=1, weight=145, unity=grams, category=carn, subcategory=ternera,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Carn picada", units=1, weight=300, unity=grams, category=carn, subcategory=ternera,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Hamburguesa", units=1, weight=150, unity=grams, category=carn, subcategory=ternera,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Trasero", units=1, weight=526, unity=grams, category=carn, subcategory=pollo,drawer=4, user=neus)
    Meal(buy_date=datetime(2021, 3, 19), expiration_date=datetime(2022, 3, 19), freezing_date=datetime(2021, 3, 21), description="Carn picada", units=1, weight=265, unity=grams, category=carn, subcategory=ternera,drawer=4, user=neus)
    commit()

if __name__ == '__main__':
    populate_database()