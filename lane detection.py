import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
   ret, frame = cap.read()
   if not ret:
      break
      
# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection to find the edges
edges = cv2.Canny(blur, 50, 150)

# Define a region of interest
height, width = edges.shape
mask = np.zeros_like(edges)
polygon = np.array([[
    (0, height),
    (width, height),
    (width, height//2),
    (width//2, height//2),
    (0, height//2),
]], np.int32)
cv2.fillPoly(mask, polygon, 255)
masked_edges = cv2.bitwise_and(edges, mask)

# Detect the lines using Hough transform
lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 15, minLineLength=40, maxLineGap=20)

# Draw the detected lines on the frame
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('frame', frame)
if cv2.waitKey
