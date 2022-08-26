from pony.orm import *


db = Database()
DB_PATH = 'sqlite_dev.db'

class Tag(db.Entity):
    id = PrimaryKey(int, auto=True)
    tag_name = Optional(str)
    products = Set('Product')


class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    Partnumber = Optional(str)
    Measure = Optional(str)
    tags = Set(Tag)
    list_products = Set('List_product')
    incomes = Set('Income')
    buys = Set('Buy')


class List_product(db.Entity):
    id = PrimaryKey(int, auto=True)
    qty_buy = Required(int, default=0)
    qty_income = Required(int, default=0)
    products = Set(Product)


class Income(db.Entity):
    id = PrimaryKey(int, auto=True)
    qty_income = Optional(int, default=0)
    products = Set(Product)


class Buy(db.Entity):
    id = PrimaryKey(int, auto=True)
    qty_buy = Optional(int, default=0)
    products = Set(Product)


db.bind(provider='sqlite', filename=DB_PATH, create_db=True)
db.generate_mapping(create_tables=True)