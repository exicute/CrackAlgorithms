import cv2 as cv
import numpy as np



class processed_image():

    def __init__(self, pathofimage):
        self.image = cv.imread(pathofimage)
        self.allsquare = self.image.shape[0]*self.image.shape[1]

   
    def filtering(self, n=5):
        self.image = cv.GaussianBlur(self.image, (n, n), 0)


    def make_hsv(self):
        self.image = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)


    #частотное распределение пикселей по цветам
    def hues(self):
        HueUnique = np.unique(self.image[:,:,0])
        HueUnique = HueUnique.astype('int32')
        HueUnique = HueUnique.reshape(HueUnique.size, 1)
        hue_values = np.concatenate((HueUnique, np.ones((HueUnique.size, 1), dtype='int32')), axis=1)

        for u in range(HueUnique.size):
            hue_values[u, 1] = np.sum(self.image[:,:,0]==hue_values[u, 0])

        return hue_values
            


class square(processed_image):
   
    #c - color
    def __init__(self, image, cspace):
        super().__init__(image)
        self.cspace = cspace
        self.color = int(cspace[:,0].mean())
        self.por = np.sum(self.cspace[:,1])/self.allsquare  #пористость


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
    path = r'Images/blurimg3.jpg'
    print(change_hsv(path))
    cv.imshow('', change_hsv(path))
    cv.waitKey(0)
