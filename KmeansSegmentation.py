from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"Images/blurtest.jpeg")
image = cv2.bilateralFilter(image, 9, 150, 150)
#image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pixel_values = image.reshape((-1, 3))
print(pixel_values)
pixel_values = np.float32(pixel_values)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
k = 3
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
labels = labels.flatten()
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(image.shape)
# show the image
cv2.imshow('', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
im = Image.open(r"paint3.jpeg")
output = list(im.getdata())
output = [list(t) for t in output]
print(output[0])
'''
