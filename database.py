from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")

    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    one = Table(number=1, capacity=4)
    two = Table(number=2, capacity=4)
    three = Table(number=3, capacity=4)
    four = Table(number=4, capacity=4)
    five = Table(number=5, capacity=4)
    six = Table(number=6, capacity=6)
    seven = Table(number=7, capacity=6)
    eight = Table(number=8, capacity=8)
    nine = Table(number=9, capacity=8)
    ten = Table(number=10, capacity=8)

    tables = [one, two, three, four, five,
              six, seven, eight, nine, ten
    ]

    db.session.add_all([employee, dinner])
    db.session.add_all(tables)
    db.session.commit()
