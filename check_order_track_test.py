# Марина Маракулина, 11-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

track = sender_stand_request.get_track()

def test_check_order_track():
    order_response = sender_stand_request.check_order()
    assert order_response.status_code == 200