import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('image/original.PNG', 0)
# img = cv.medianBlur(img, 5)

kernel = np.ones((3, 2), np.uint8)

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# for i in range(3):
#     th3 = cv.morphologyEx(th3, cv.MORPH_CLOSE, kernel)

print(cv.ADAPTIVE_THRESH_GAUSSIAN_C)
print(cv.ADAPTIVE_THRESH_MEAN_C)

titles = ['Original Image', 'Global Threshold (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
