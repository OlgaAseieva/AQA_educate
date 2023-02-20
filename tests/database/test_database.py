import pytest
from moduls.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def check_all_users():
    db = Database()
    users = db.get_all_user()
    print(users)

@pytest.mark.database
def test_check_user_serg():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    new_qnt = db.selected_product_qnt_by_id(1)

    assert new_qnt[0][0] == 25

@pytest.mark.database
def test_product_qnt_insert():
    db = Database()
    db.insert_product(4, 'cake', 'sweet', 30)
    new_qnt = db.selected_product_qnt_by_id(4)

    assert new_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'test', 'test', 999)
    db.delete_product(99)
    qnt = db.selected_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    order = db.get_detailed_order()
    print('Order', order)
    
    assert len(order) == 1

    assert order[0][0] == 1
    assert order[0][1] == 'Sergii'
    assert order[0][2] == "солодка вода"
    assert order[0][3] == "з цукром"
