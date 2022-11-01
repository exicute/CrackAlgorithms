import cv2 as cv
import numpy as np



class processed_image():

    def __init__(self, pathofimage):
        self.image = cv.imread(path)
        self.allsquare = self.image.shape[0]*self.image.shape[1]

   
    def filtering(self, n):
        self.image = cv.GaussianBlur(sel.image, (n, n), 0)


    def make_hsv(self):
        self.image = cv.cvtColor(sefl.image, cv.COLOR_BGR2HSV)


    #частотное распределение пикселей по цветам
    def hues(self):
        HueUnique = np.unique(self.image[:,:,0])
        HueUnique = HueUnique.astype('int32')
        HueUnique = HueUnique.reshape(HueUnique.size, 1)
        self.hue_values = np.concatenate((HueUnique, np.ones((HueUnique.size, 1), dtype='int32')), axis=1)

        for u in range(HueUnique.size):
                self.hue_values[u, 1] = np.sum(hsv[:,:,0]==self.hue_values[u, 0])
            


class square(processed_image):
   
    #c - color
    def __init__(self, image, cspace):
        super().__init__(image)
        self.cspace = cspace
        self.coords = np.array([1, 1], ndmin=2)
        self.color = cspace[:,0].mean()
        self.por = np.sum(self.space[:,1])/self.allsquare  #пористость


    def find_coords(self):
        for u in hues[:,0]:
            temp1 = np.where(self.image[:,:,0]==u)
            temp2 = np.ones((temp1[0].size, 2))
                            
            temp2[:,0] = temp2[:,0]*temp1[0]
            temp2[:,1] = temp2[:,1]*temp1[1]
                                        
            self.coords = np.concatenate((self.coords, temp2))
        



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
