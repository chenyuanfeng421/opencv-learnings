# -*- coding: utf-8 -*-
import numpy as np
import cv2
import time




def compareRGB(rgb1, rgb2):
    if abs(int(rgb1) - int(rgb2)) > 80:
        return False
    return True


def makeLogo(logo, img, height, width):
    w = 0
    while w < width:
        h = 0
        while h < height:
            if compareRGB(logo[h, w], img[h, w]) == False:
                logo[h, w] = 0
            h += 1
        w += 1
    return logo



def setLogo(logo, width, height):
    w = 0
    while w < width:
        h = 0
        while h < height:
            if logo[h, w] != 0:
                logo[h, w] = 255
            h += 1
        w += 1
    return logo

def makeMode(name):
    cap = cv2.VideoCapture(name)
    fps = cap.get(cv2.CAP_PROP_FPS)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print count/fps%60
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    logo, i = None, 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        if i !=0 and i % int(count/81) == 0:
            try:
                if logo == None:
                    logo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    i += 1
                    continue
            except:
                pass
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            logo = makeLogo(logo, img, height, width)
            print i
        i += 1
    logo = setLogo(logo, width, height)
    kernel = np.ones((10, 10), np.uint8)
    logo = cv2.dilate(logo, kernel, iterations=1)
    cv2.imwrite('image/logo.jpg', logo)
    cap.release()
    cv2.destroyAllWindows()
    # exit()
    return (width, height, fps, logo)

def saveMp4(name):
    width, height, fps, logo = makeMode(name)
    cap = cv2.VideoCapture(name)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))
    i = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        inpainted = cv2.inpaint(frame, logo, 8, cv2.INPAINT_NS)
        # cv2.imwrite('image/' + str(i) + '.jpg', inpainted)  # 存储为图像
        out.write(inpainted)
        # cv2.imshow('frame',inpainted)
        # cv2.waitKey(0)
        print i
        i = i + 1
    cap.release()
    out.release()
    cv2.destroyAllWindows()




if __name__ == "__main__":
    saveMp4("1.mp4")