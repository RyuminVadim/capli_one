import main

def test_area_GaussianBlur():
    file = 'test.png'
    _, area = main.processing(file,0)
    #102900
    assert   10745.0 - (10745.0*0.01)<= area<= 10745.0 + (10745.0*0.01)

def test_area_adaptiveThreshold():
    file = 'test.png'
    _, area = main.processing(file,1)
    #102900
    assert   10745.0 - (10745.0*0.01)<= area<= 10745.0 + (10745.0*0.01)

