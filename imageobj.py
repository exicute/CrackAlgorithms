import cv2 as cv
import numpy as np
from PIL import ImageEnhance, Image
from pillow_lut import rgb_color_enhance
from matplotlib import cm


class processed_image():

    def __init__(self, pathofimage):
        self.image = cv.imread(path)

   
    def filtering(self):
        n = 5
        if self.image.shape[0]>self.image.shape[1]:
            n += self.image.shape[0]//1000
        else:
            n += self.image.shape[1]//1000

        self.image = cv.GaussianBlur(sel.image, (n, n), 0)


    def make_hsv(self):
        self.image = cv.cvtColor(sefl.image, cv.COLOR_BGR2HSV)


    def hues(self):
        HueUnique = np.unique(self.image[:,:,0])
        HueUnique = HueUnique.astype('int32')
        HueUnique = HueUnique.reshape(HueUnique.size, 1)
        self.hue_values = np.concatenate((HueUnique, np.ones((HueUnique.size, 1), dtype='int32')), axis=1)

        for u in range(HueUnique.size):
                self.hue_values[u, 1] = np.sum(hsv[:,:,0]==self.hue_values[u, 0])

   
    #нахождение диапозонов цветов с помощью среднеквадратичного отклонения
    def split_colors(self):
        self.color_spaces = []

        hues_mean = self.hue_values.mean()
        less_mean = self.hue_values[:,1]<hues_mean
        less_mean = self.hue_values[less_mean]
        more_mean = self.hue_values[:,1]>hues_mean
        more_mean = self.hue_values[more_mean]
        
        self.color_spaces.append(less_mean)

        while more_mean.size!=0:
            counter = 0
            



class square(processed_image):
    
    def __init__(self, image, space):
        super().__init__(image)
        self.space = space


    def find_coords(self):
        pass


    def colored_space(self):
        pass



def change_hsv(path):
    image = cv.imread(path)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    
    #np.multiply(2, hsv[:,:,1], out=hsv[:,:,1])
    #hsv[:,:,1] = np.where((hsv[:,:,1]<80), hsv[:,:,1]*3, 0)

    HueUnique = np.unique(hsv[:,:,0])
    HueUnique = HueUnique.astype('int16')
    HueUnique = HueUnique.reshape(HueUnique.size, 1)
    hue_values = np.concatenate((HueUnique, np.ones((HueUnique.size, 1), dtype='int32')), axis=1)

    for u in range(HueUnique.size):
            hue_values[u, 1] = np.sum(hsv[:,:,0]==hue_values[u, 0])

    hues = hue_values[:,1]>80
    hues = hue_values[hues]

    hsv[:,:,1] = np.where((50<hsv[:,:,0])&(hsv[:,:,0]<98), 255, 0)
    hsv[:,:,2] = np.where((50<hsv[:,:,0])&(hsv[:,:,0]<98), 255, 0)

    hsv = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

    return hsv



if __name__ == "__main__":
    path = r'Images/blurimg3.jpg'
    print(change_hsv(path))
    cv.imshow('', change_hsv(path))
    cv.waitKey(0)
