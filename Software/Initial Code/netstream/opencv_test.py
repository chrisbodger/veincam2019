import cv2

img = cv2.imread('test.jpeg', 0)
cv2.imshow('test', img)
cv2.waitKey()

clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(5, 5))
imghist = clahe.apply(img)

cv2.imshow('hist', imghist)
cv2.waitKey()

clahe2 = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(10, 10))
imghist2 = clahe2.apply(img)

cv2.imshow('hist2', imghist2)
cv2.waitKey()



