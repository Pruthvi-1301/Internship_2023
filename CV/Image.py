import numpy as np
import cv2 as cv

img = cv.imread(r'E:\Projects\Pruthvi Tata IQ\Dataset\Flower\flower_images\0001.png', 0)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.waitKey(0)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()