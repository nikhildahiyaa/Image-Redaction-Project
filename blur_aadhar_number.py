import numpy as np
import cv2
import matplotlib.pyplot as plt
import re
import cv2


image = cv2.imread("aadhar2.jpg")
  
#Converting BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  
#Read image
image = cv2.imread('aadhar2.jpg')

import easyocr

#Reading english words using easyocr
reader = easyocr.Reader(['en'])
output = reader.readtext(image)

#Identify the AADHAR number
#Created a regular expression to check valid Aadhaar number as mentioned below
regex = ("^[2-9]{1}[0-9]{3}\\" +
             "s[0-9]{4}\\s[0-9]{4}$")

for out in output:
    if re.match(regex, out[1]):
        print(out)
        AADHAR=out
        
#Extracted the word which we need to blur and saved the it in the variable name cord
cord = AADHAR[0]
print(cord)

#Catched up the min and max the cordinates of bounding box
x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
print(x_min)
print(y_min)
print(x_max)
print(y_max)

#Created ROI coordinates(region of interest)
topLeft = (x_min, y_min)
bottomRight = (x_max, y_max)
x, y = topLeft[0], topLeft[1]
w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

#Grabbed ROI with Numpy slicing and blur
ROI = image[y:y+h, x:x+w]
blur = cv2.GaussianBlur(ROI, (51,51), 0)

#Inserted ROI back into image
image[y:y+h, x:x+w] = blur
cv2.imshow('image', image)
cv2.waitKey()
