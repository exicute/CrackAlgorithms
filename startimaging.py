#исполняемый файл
from imageobj import processed_image, square
import cv2 as cv
import numpy as np


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
    color_spaces.append(less_mean)

    more_mean = hue_values[:,1]>=hues_mean
    more_mean = hue_values[more_mean]
    more_mean0 = more_mean[:,0]
    

    mStd = more_mean0.std()*2  #среднеквадратичное отклонения для 0 столба(зн-я hue)
                             #подобрать наиболее подходящее значение(на основе процентилей)
    #c - current
    cind = 0
    counter = 0
    while more_mean0.size!=0:
        cnum = more_mean0[cind]
        clist = more_mean0[(more_mean0<cnum+mStd)&(more_mean0>cnum-mStd)]
        
        if clist.size == 1:
            tempInd = np.where(hue_values[:,0]==cnum)
            color_spaces.append(hue_values[tempInd])
            more_mean0 = np.delete(more_mean0, cind)

        elif clist.size > counter:
            counter = clist.size
            cind += 1
            continue
        
        else:
            tempind = np.array([], dtype='int16')
            for i in clist:
                ind = np.where(hue_values[:,0]==i)
                tempind = np.concatenate((tempind, ind[0]))
           
            color_spaces.append(hue_values[tempind])
            temp = np.where(more_mean0[(more_mean0<cnum+mStd)&(more_mean0>cnum-mStd)])[0]
            more_mean0 = np.delete(more_mean0, temp)

            cind = 0
            counter = 0

    return color_spaces


def colored(image, coords, color):
    px = coords[:,0]
    py = coords[:,1]

    image[px,py,0] = color
    image[px,py,1] = 255
    image[px,py,2] = 255

    return image



if __name__ == "__main__":
    #нужно исключить не яркие и не контрастные пиксели(через np.where??)
    path = r'Images/testimg1.jpg'

    #полное изображение
    myImg = processed_image(path)
    n = find_n_filter(myImg.image)-1

    myImg.filtering(n)

    myImg.make_hsv()

    chue_values = myImg.hues()

    #разделение на области
    #Т.к. добавлено разделение на яркости и контрастности
    #необходимо понять один у нас цвет или несколько:
    #при каком то условии убирать разделение по среднему на верхнее и нижнее
    mySqrs = []
    for clist in split_colors(chue_values):
        mySqrs.append(square(myImg.image, clist))
    
    end_image = np.zeros_like(myImg.image)
    for sqrs in mySqrs:
        end_image = colored(end_image, sqrs.find_coords(), sqrs.color)
    
    end_image = cv.cvtColor(end_image, cv.COLOR_HSV2BGR)
    cv.imshow('', end_image)
    cv.waitKey(0)
