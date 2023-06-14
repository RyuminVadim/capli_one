import main
def test_area_one():
    file = './image/test.png'
    image, area = main.processing(file)
    #102900
    assert area > 102900 - (102900*0.1)

def test_area_two():
    file = './image/test.png'
    image, area = main.processing(file)
    assert area < 102900 + (102900*0.1)