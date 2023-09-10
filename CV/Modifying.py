import numpy as np
import cv2 as cv

img = cv.imread(r'E:\Projects\Pruthvi Tata IQ\Dataset\Flower\flower_images\0002.png', 1)
resized_img = cv.resize(img, (600, 400))

for x in range(300):
    for y in range(200):
        resized_img[x][y] = [255, 0, 255]

cv.imshow('Image', resized_img)

cv.waitKey(0)