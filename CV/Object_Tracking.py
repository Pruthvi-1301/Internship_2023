import cv2 as cv
import numpy as np

object_detector = cv.createBackgroundSubtractorMOG2()

img = cv.imread('CV\Object_Tracking.jpg', 1)
mask = object_detector.apply(img)

cv.imshow('mask', mask)
cv.waitKey(0)
cv.destroyAllWindows()