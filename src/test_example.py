import processing as proc

def test_area_GaussianBlur():
    file = 'test.png'
    image,gray =proc.load_image(file)
    thresh =proc.pre_processing(gray,"Gaussian Blur")
    thresh = proc.noise(thresh,3,3,1)
    thresh = proc.dilate(thresh,3,3,2)
    _,area = proc.contur(image,thresh)
    assert   10745.0 - (10745.0*0.1)<= area<= 10745.0 + (10745.0*0.1)

def test_area_adaptiveThreshold():
    file = 'test.png'
    image, gray = proc.load_image(file)
    thresh = proc.pre_processing(gray, "Adaptive Threshold")
    thresh = proc.noise(thresh, 3, 3, 1)
    thresh = proc.dilate(thresh, 3, 3, 2)
    _, area = proc.contur(image, thresh)
    assert 10745.0 - (10745.0 * 0.1) <= area <= 10745.0 + (10745.0 * 0.1)

