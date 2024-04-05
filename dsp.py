import cv2
import numpy as np

input_image = cv2.imread('C:\\Users\\aarju\\Downloads\\images.jpg')

gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

gaussian_blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

median_blurred_image = cv2.medianBlur(gray_image, 5)

bilateral_filtered_image = cv2.bilateralFilter(gray_image, 9, 75, 75)

degraded_image = cv2.imread('C:\\Users\\aarju\\Downloads\\images.jpg', cv2.IMREAD_GRAYSCALE)
restored_image = cv2.medianBlur(degraded_image, 3)

cv2.imshow('Original Image', gray_image)
cv2.imshow('Gaussian Blurred Image', gaussian_blurred_image)
cv2.imshow('Median Blurred Image', median_blurred_image)
cv2.imshow('Bilateral Filtered Image', bilateral_filtered_image)
cv2.imshow('Restored Image', restored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
