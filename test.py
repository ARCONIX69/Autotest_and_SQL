import create_orders_and_get_orders
import data

# Романов Юрий, 5-я когорта - Финальный проект. Инженер по тестированию плюс

def test_number_one():
    response_created_orders = create_orders_and_get_orders.post_create_order(data.create_orders)
    assert response_created_orders.status_code == 201
def test_number_two():
    response_get_orders = create_orders_and_get_orders.get_order()
    assert response_get_orders.status_code == 200