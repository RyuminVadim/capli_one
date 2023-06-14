#import cv2
import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_numbers(x, y):
    return x + y



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def inversion(thresh):
    return cv2.bitwise_not(thresh)
def pre_processing(file, val):
    image_color = cv2.imread(file,cv2.IMREAD_UNCHANGED)
    image = cv2.imread(file,0)
    #print(image)
    if(val == 0):
        x, y = image.shape
        median = cv2.GaussianBlur(image, (11, 11), 0)
        median1 = cv2.GaussianBlur(image, (21, 21), 0)
        a = median1 - median
        thresh = 255 - a
    if (val == 1):
        thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    return image_color,thresh
def processing(file):
    image, thresh = pre_processing(file, 1)
    thresh = inversion(thresh)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    #thresh = cv2.erode(thresh, kernel, iterations=1)#тоньше
    thresh = cv2.dilate(thresh, kernel, iterations=2)#тольще

    return contur(image,thresh)
    pass

def contur(image,thresh):
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    t = len(contours[:])
    area = 0
    for u in range(0, t):
        if (np.size(contours[u]) > 100):
            ellipse = cv2.fitEllipse(contours[u])
            (center, axes, orientation) = ellipse
            majoraxis_length = max(axes)
            minoraxis_length = min(axes)
            eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
            if (eccentricity < 0.75):
                area += cv2.contourArea(contours[u])
                cv2.drawContours(image, contours, u, (255, 1, 255), 3)
    return image,area

def print_image(image):
    #fig, ax = plt.subplots(1, 1)
    #ax[0].imshow(image)
    #ax[1].imshow(thresh1)
    #plt.show()
    cv2.imshow('image', image)
    cv2.waitKey(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = './image/test.png'
    #file = './image/1.jpg'


    image,area = processing(file)

    print(f"area = {area}")

    print_image(image)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
