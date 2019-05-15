import cv2 as cv

cv.namedWindow('Image', 0)
cv.namedWindow('Image1', 0)
cv.namedWindow('Image2', 0)
# 预生成多个窗口供显示处理后图片
img = cv.imread('image/test3.PNG', 0)
# 将需要处理的图片读入

print(cv.COLOR_BGR2GRAY)

# img = cv.medianBlur(img, 5)
# cv.imshow('Image', img)
ret, img = cv.threshold(img, 255, 127, 1)
cv.imshow('Image1', img)
# 处理图片
print()

cv.imshow('Image2', img)
# 输出图片到Image窗口

cv.waitKey()
cv.destroyAllWindows()
