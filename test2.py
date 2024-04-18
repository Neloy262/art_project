import cv2
import numpy as np
import string
import random

text = "Hello"
random_number = ''.join(random.choices(string.ascii_uppercase +string.digits, k=5))
(text_with_num_width,text_with_num_height),_=cv2.getTextSize(text+" "+random_number,cv2.FONT_HERSHEY_SIMPLEX,0.7,1)

(text_width,text_height),_ = cv2.getTextSize(text,cv2.FONT_HERSHEY_SIMPLEX,0.7,1)

print(text_height,text_width)
# Load the image
image = cv2.imread('test.jpg')

# Create a copy of the image
overlay = image.copy()

padding = 10

# Define rectangle parameters (start point, end point, color, thickness)
start_point = (100-padding, 100-padding)
end_point = (start_point[0]+text_with_num_width+padding, start_point[1]+text_height+padding)
print(start_point,end_point)
print(end_point[0]-start_point[0],end_point[1]-start_point[1])
color = (0, 0, 0)  # Green color in BGR
thickness = -1  # Fill the rectangle

# Draw the filled rectangle on the overlay
cv2.rectangle(overlay, start_point, end_point, color, thickness)
# Set transparency level (alpha value)
alpha = 0.2

# Combine the original image and the overlay with transparency
cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
cv2.putText(image,text,(start_point[0],start_point[1]+text_height),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),1)
cv2.putText(image,random_number,(start_point[0]+text_width,start_point[1]+text_height),cv2.FONT_HERSHEY_SIMPLEX,0.4,(34, 214, 83),1)
# Display the image
cv2.imshow('Transparent Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
