import cv2 as cv

cv.namedWindow('Image', 0)
# 预生成多个窗口供显示处理后图片
img = cv.imread('image/66.png')
# 将需要处理的图片读入
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

print(cv.COLOR_BGR2GRAY)
print(img)

ret, img = cv.threshold(img, 127, 255, 4, img)
# 处理图片
print()

print(img)

cv.imshow('Image', img)
# 输出图片到Image窗口

cv.waitKey()
cv.destroyAllWindows()
