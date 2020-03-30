import cv2
import numpy as np

for i in range(1, 4):
    img = cv2.imread('bahan' + str(i) + '.png', 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_api1 = np.array([0, 0, 0])
    upper_api1 = np.array([255, 255, 200])
    mask1 = cv2.inRange(hsv, lower_api1, upper_api1)

    mask = mask1

    new_img = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow('mask',mask)
    cv2.imshow("hasil" + str(i) + ".png", new_img)
    cv2.imshow('image', img)

    # menunggu tombol key ditekan
    cv2.waitKey(0)
    cv2.destroyAllWindows()
