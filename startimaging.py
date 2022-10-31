#исполняемый файл
import imgprocess
import cv2 as cv
from PIL import Image, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt


def find_colors():
    pass



if __name__ == "__main__":
    path = r'Images/test.jpeg'
    filtered = imgprocess.filtered_img(path)
    end_img = makeWatershed(filtered)
    cv.imshow('123', end_img)
    cv.waitKey(0)
