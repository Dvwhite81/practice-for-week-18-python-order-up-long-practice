from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from app.models import db, Employee, Menu, MenuItem, MenuItemType, Order, Table
from app.forms import AssignTableForm, CloseTableForm, AddItemsForm

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/", methods=["POST", "GET"])
@login_required
def index():
    assign_table = AssignTableForm()
    close_table = CloseTableForm()
    add_items = AddItemsForm()

    tables = Table.query.order_by(Table.number).all()
    employees = Employee.query.order_by(Employee.employee_number).all()
    orders = Order.query.filter(Order.finished == False).all()

    filled_tables = [order.table_id for order in orders]
    open_tables = [table for table in tables if table.id not in filled_tables]

    assign_table.tables.choices = [(t.id, f"Table number {t.number}") for t in open_tables]
    assign_table.servers.choices = [(e.id, f"{e.name}") for e in employees]

    your_orders = Order.query.filter(
        Order.employee_id == current_user.id,
        Order.finished == False
    ).all()

    menu_items = (
        MenuItem.query.join(MenuItemType)
        .group_by(MenuItemType.name, MenuItem.id)
        .order_by(MenuItemType.name, MenuItem.name)
    ).all()

    add_items.choices = [
        (item.id, item.name) for item in MenuItem.query.all()
    ]

    if assign_table.validate_on_submit():
        table_id = assign_table.table.data
        employee_id = assign_table.employee.data
        create_order = Order(
            table_id=table_id,
            employee_id=employee_id,
            finished=False
        )

        db.session.add(create_order)
        db.session.commit()
        redirect(url_for(".index"))

    return render_template(
        "orders.html",
        assign_table=assign_table,
        your_orders=your_orders,
        close_table=close_table,
        add_items=add_items
    )
