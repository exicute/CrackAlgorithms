#исполняемый файл
from imageobj import processed_image, square
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def find_n_filter(image):
    n = 5
    if image.shape[0]>image.shape[1]:
        n += image.shape[0]//1000
    else:
        n += image.shape[1]//1000

    return n


#нахождение диапозонов цветов с помощью среднеквадратичного отклонения
def split_colors(hue_values):
    hue_values = hue_values[hue_values[:, 0]. argsort ()]

    color_spaces = []  #массив - элементы в котором: массивы с цветами

    hues_mean = hue_values[:,1].mean()
    less_mean = hue_values[:,1]<hues_mean
    less_mean = hue_values[less_mean]
    less_mean0 = less_mean[:,0]

    more_mean = hue_values[:,1]>hues_mean
    more_mean = hue_values[more_mean]
    more_mean0 = more_mean[:,0]
    
    color_spaces.append(less_mean0)

    mStd = int(more_mean0.std())  #среднеквадратичное отклонения для 0 столба(зн-я hue)
    
    #c - current
    while more_mean0.size!=0:
        cind = 0
        counter = 0
        cnum = more_mean0[cind]
        clist = more_mean0[(more_mean0<cnum+mStd)&(more_mean0>cnum-mStd)]
        
        if clist.size == 1:
            color_spaces.append(np.array([cnum]))
            more_mean0 = more_mean0[more_mean0!=cnum]

        elif clist.size > counter:
            counter = clist.size
            cind += 1
            continue

        else:
            color_space.append(hue_values[clist])
            more_mean0 = more_mean0[more_mean0!=clist]
            cind = 0
            counter = 0

    return color_spaces



def colored():
    pass


if __name__ == "__main__":
    path = r'Images/blurimg2.jpg'
