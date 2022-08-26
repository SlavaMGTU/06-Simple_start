from pony import orm
from pony.orm import Database,Required,Set,Json,PrimaryKey,Optional
from pony.orm.core import db_session
import datetime
import sqlite3


# Constants and variables
#DB_PATH = './db'
#DB_PATH = 'db_dev\\sqlite_dev\\sqlite_dev\\sqlite_dev.db'
DB_PATH = 'sqlite_dev.db'
db = Database()

#class Scope(db.Entity): name(str); product(m2m) 2й вариант с промежуточной таблицей

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


def setup_db(hash_map: Optional['hashMap'] = None,
             db_path: str = DB_PATH,
             database: Database = db
             ) -> None:
    """
    Creates the database with required tables
    """

    if hash_map:
        db_path = hash_map.get('DB_PATH')

    database.bind(provider='sqlite', filename=db_path, create_db=True)
    database.generate_mapping(create_tables=True)


def add_table_entries(data: dict) -> None:
    """
    Fills the database tables with some data
    """

    for table, records in data.items():

        for record_data in records:
            obj = table.get(name=record_data.get('name'))

            if obj:
                obj.set(**record_data)
            else:
                table(**record_data)


if __name__ == '__main__':
    setup_db()
