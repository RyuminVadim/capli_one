import main
def test_add_numbers():
    assert main.add_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert main.add_numbers(-2, 3) == 1