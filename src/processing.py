import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(file):
    """Загрузки изображения."""
    image_collor = cv2.imread(file, 1)
    image = cv2.imread(file, 0)
    return image_collor,image

def inversion(thresh):
    """Инверсии значений в маске."""
    return cv2.bitwise_not(thresh)

def pre_processing(image, val="Gaussian Blur"):
    """
    Создание порогового изображения.
    Применяется адаптивный порог или разница между двумя размытиями по Гауссу с разным ядром.
    """
    if(val == "Gaussian Blur"):
        x, y = image.shape
        median = cv2.GaussianBlur(image, (11, 11), 0)
        median1 = cv2.GaussianBlur(image, (21, 21), 0)
        a = median-median1
        thresh = 255 - a
        thresh = inversion(thresh)
        _,thresh= cv2.threshold(thresh,127,255,cv2.THRESH_BINARY)
    if (val == "Adaptive Threshold"):
        thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
        thresh = inversion(thresh)
    return thresh

def noise(thresh,w,h,iter):
    """Удаления шума."""
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (w, h))
    return cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=iter)#удаление шума

def dilate(thresh,w,h,iter):
    """Увеличение площади обьектов."""
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (w, h))
    return  cv2.dilate(thresh, kernel, iterations=iter)#тольще

def contur(image,thresh):
    """Создание контура по маске, наложение его на изображение и подсчёт общей площади всех выделенных обьектов."""
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
            if (eccentricity < 0.76):
                area += cv2.contourArea(contours[u])
                cv2.drawContours(image, contours, u, (255, 1, 255), 3)
    return image,area

def print_image(image,val=0):
    """Вывод изображения в отдельном окне. """
    if(val == 0):
        cv2.imshow('image', image)
        cv2.waitKey(0)
    if (val == 1):
        imgplot = plt.imshow(image)
        plt.show()


if __name__ == "__main__":
    image_color, image = load_image("../image/1.jpg")
    thresh = pre_processing(image, val="Gaussian Blur")
    thresh = noise(thresh, w=3, h=3, iter=1)
    thresh = dilate(thresh, w=5, h=5, iter=1)
    result_image, area = contur(image_color, thresh)

    print("Area:", area)
