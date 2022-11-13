import cv2 as cv
import numpy as np


def can(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_MEAN_C,\
                        cv.THRESH_BINARY_INV,11,2)

    can = cv.Canny(gray, 0, 100)
    end_canny = np.uint8(can*255)

    return thresh


def contours(image, draw):
    contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) 
    end_contours = []
   
    for actContour in contours:
        rect = cv.minAreaRect(actContour)
        box = cv.boxPoints(rect)
        box = np.uint0(box)
    
        longSide = 0
        shortSide = 0
        side1 = np.sqrt((box[0][0]-box[1][0])**2+(box[0][1]-box[1][1])**2)
        side2 = np.sqrt((box[1][0]-box[2][0])**2+(box[1][1]-box[2][1])**2)
        if side1<side2:
            shortSide = side1
            longSide = side2
        else:
            shortSide = side2
            longSide = side1

        areaLength = cv.contourArea(actContour)
        arcL = cv.arcLength(actContour, True)
        print(shortSide, arcL)
        if (areaLength<80) or ((arcL)==0 or ((areaLength)/pow(arcL, 2))>0.02):
            continue
        else:
            end_contours.append(actContour)
            cv.drawContours(draw,[box],0,(0,0,255),2)


    return end_contours


if __name__ == "__main__":
    path = r'Images/resultimg3.png'
    image = cv.imread(path)

    thresh = can(image)
    contour = contours(thresh, image)

    cv.drawContours(image, contour, -1, (0, 255, 0), 3)
    
    cv.imshow('', image)
    cv.waitKey(0)
