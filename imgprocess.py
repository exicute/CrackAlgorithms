#основная задача - разделить изображение на цвета, заполнить области изображения разными цветами, которые находятся рядом или типо того(к средних, в фотошопе фильтры)
#в небольшой области к-средних определяет цвет трещины
import cv2 as cv
import numpy as np
from PIL import ImageEnhance, Image
from pillow_lut import rgb_color_enhance
from matplotlib import cm



def filtered_img(path):
    img = Image.open(path)
    end_img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    blur = cv.GaussianBlur(end_img, (5, 5), 0)
    end_img = Image.fromarray(blur)
    lut = rgb_color_enhance(50, brightness=-1, contrast=5)
    end_img = end_img.filter(lut)

    return end_img


#увеличить все значения выше среднего на ...(все остальные уменьшить)
def chande_saturation(image):
    pass


def change_hsv(path):
    image = cv.imread(path)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    
    #np.multiply(2, hsv[:,:,1], out=hsv[:,:,1])
    #hsv[:,:,1] = np.where((hsv[:,:,1]<80), hsv[:,:,1]*3, 0)

    HueUnique = np.unique(hsv[:,:,0])
    HueUnique = HueUnique.astype('int16')
    HueUnique = HueUnique.reshape(179, 1)
    hue_values = np.concatenate((HueUnique, np.ones((179, 1), dtype='int32')), axis=1)

    for u in range(HueUnique.size):
            hue_values[u, 1] = np.sum(hsv[:,:,0]==hue_values[u, 0])

    hues = hue_values[:,1]>80
    hues = hue_values[hues]

    hsv[:,:,1] = np.where((hsv[:,:,0] in hues[:,0]), hsv[:,:,1], hsv[:,:,1]//2)
    hsv[:,:,2] = np.where((hsv[:,:,0] in hues[:,0]), hsv[:,:,2],hsv[:,:,2]//2)

    hsv = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    return hsv



if __name__ == "__main__":
    path = r'Images/test.jpeg'
    print(change_hsv(path))
    cv.imshow('', change_hsv(path))
    cv.waitKey(0)
