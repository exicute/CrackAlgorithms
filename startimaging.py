#исполняемый файл
import imgprocess
import cv2 as cv
from PIL import Image, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt


#попробовать применить сглаживающие фильтры поверх
#попробовать просмотреть по каналам и находить наибольшее значение интенсивности по каждому каналу
def makeWatershed(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)

    return thresh



if __name__ == "__main__":
    path = r'Images/test.jpeg'
    filtered = imgprocess.filtered_img(path)
    end_img = makeWatershed(filtered)
    cv.imshow('123', end_img)
    cv.waitKey(0)
