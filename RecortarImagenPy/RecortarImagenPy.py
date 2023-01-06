import os
import cv2
import numpy as np

#1era Solucion

# def imshow(label, image):
#     cv2.imshow(label, image)
#     cv2.waitKey(0)
#     #cv2.destroyAllWindows()

# #read image
# rgb_img = cv2.imread('C:\Users\patit\source\repos\ImagenExtraer')
# rgb_img = cv2.resize(rgb_img, (900, 600))
# gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)

# #canny edge detection
# canny = cv2.Canny(gray_img, 50, 120)

# # Morphology Closing
# kernel = np.ones((7, 23), np.uint8)
# closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

# # Find contours 
# contours, hierarchy = cv2.findContours(closing.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# # Sort Contors by area and then remove the largest frame contour
# n = len(contours) - 1
# contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]

# copy = rgb_img.copy()

# # Iterate through contours and draw the convex hull
# for c in contours:
#     if cv2.contourArea(c) < 750:
#         continue
#     hull = cv2.convexHull(c)
#     cv2.drawContours(copy, [hull], 0, (0, 255, 0), 2)
#     imshow('Convex Hull', copy)

#2da Solucion

# def imshow(label, image):
#     cv2.imshow(label, image)
#     cv2.waitKey(0)
#     #cv2.destroyAllWindows()

# #read image
# rgb_img = cv2.imread('C:\Users\patit\source\repos\ImagenExtraer.jpg')
# rgb_img = cv2.resize(rgb_img, (900, 600))
# gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)

# #canny edge detection
# canny = cv2.Canny(gray_img, 50, 120)

# # Morphology Closing
# kernel = np.ones((7, 23), np.uint8)
# closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

# # Find contours 
# contours, hierarchy = cv2.findContours(closing.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# # Sort Contors by area and then remove the largest frame contour
# n = len(contours) - 1
# contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]

# copy = rgb_img.copy()

# # Iterate through contours and draw the convex hull
# for c in contours:
#     if cv2.contourArea(c) < 750:
#         continue
#     hull = cv2.convexHull(c)
#     cv2.drawContours(copy, [hull], 0, (0, 255, 0), 2)
#     imshow('Convex Hull', copy)

#3era Solucion


# Load image and HSV color threshold

image = cv2.imread('C:\Users\patit\source\repos\ImagenExtraer.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([90, 38, 0])
upper = np.array([145, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)
result[mask==0] = (255, 255, 255)

# Find contours on extracted mask, combine boxes, and extract ROI

cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = np.concatenate(cnts)
x,y,w,h = cv2.boundingRect(cnts)
cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
ROI = result[y:y+h, x:x+w]

cv2.imshow('result', result)
cv2.imshow('mask', mask)
cv2.imshow('image', image)
cv2.imshow('ROI', ROI)
cv2.waitKey()