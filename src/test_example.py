import main

def test_area_one():
    file = 'test.png'
    _, area = main.processing(file)
    #102900
    assert area >= 102900 - (102900*0.1)

def test_area_two():
    file = 'test.png'
    _, area = main.processing(file)
    assert area <= 102900 + (102900*0.1)