import cv2 as cv
import numpy as np
from PIL import Image, ImageFilter



class processed_image():

    def __init__(self, pathofimage):
        self.image = cv.imread(pathofimage)
        self.allsquare = self.image.shape[0]*self.image.shape[1]
        self.img_path = pathofimage

   
    def filtering(self, n=5):
        im = Image.open(self.img_path).convert('RGB')
        im1 = im.filter(ImageFilter.GaussianBlur(radius = n))
        open_cv_image = np.array(im1) 
        # Convert RGB to BGR 
        self.image = open_cv_image[:, :, ::-1].copy() 


    def make_hsv(self):
        self.image = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)


    def saturationsvalues(self, image):
        saturation = image[:,:,1]
        value = image[:,:,2]

        parts = (saturation[saturation<saturation.mean()//2], value[value<value.mean()//2])
        filtredimg = image[(saturation>saturation.mean()//2)&(value>value.mean()//2)]

        return (filtredimg, parts)


    #частотное распределение пикселей по цветам
    def hues(self, allvalues):
        HueUnique = np.unique(allvalues[:,:,0])
        HueUnique = HueUnique.astype('int32')
        HueUnique = HueUnique.reshape(HueUnique.size, 1)
        hue_values = np.concatenate((HueUnique, np.ones((HueUnique.size, 1), dtype='int32')), axis=1)

        for u in range(HueUnique.size):
            hue_values[u, 1] = np.sum(allvalues[:,:,0]==hue_values[u, 0])

        return hue_values
            


class square(processed_image):
   
    #c - color
    def __init__(self, image, cspace):
        self.image = image  #основное обработанное изображение
        self.cspace = cspace
        self.color = int(cspace[:,0].mean())
        self.por = np.sum(self.cspace[:,1])/self.image.size  #пористость


    def find_coords(self):

        coords = np.array([1, 1], ndmin=2)

        for u in self.cspace[:,0]:
            temp1 = np.where(self.image[:,:,0]==u)
            temp2 = np.ones((temp1[0].size, 2))
                            
            temp2[:,0] = temp2[:,0]*temp1[0]
            temp2[:,1] = temp2[:,1]*temp1[1]
                                        
            coords = np.concatenate((coords, temp2))
        
        coords = coords.astype('int32')

        return coords
        


if __name__ == "__main__":
    path = r'Images/testimg3.jpg'

    image = processed_image(path)
    image.make_hsv()
    end_image = image.saturationsvalues(image.image)[0]

    print(end_image.ndim)
