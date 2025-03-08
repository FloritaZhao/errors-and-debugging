def get_3rd_value(my_list):
    return my_list[2] if len(my_list) > 2 else None

def test_get_3rd_value():
    assert get_3rd_value([0, 1, 2]) == 2
    assert get_3rd_value([0, 1]) is None

def get_last_value(my_list):
    return my_list[-1] if my_list else None

def test_get_last_value():
    assert get_last_value([0, 1, 2]) == 2
    assert get_last_value([0]) == 0
    assert get_last_value([]) is None

def runtime_errors():
    test_get_3rd_value()
    test_get_last_value()

