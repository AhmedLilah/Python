import cv2 as cv2
import numpy as np

def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

# Create new blank 300x300 red image
width, height = 300, 300

white = (255, 255, 255)
image = create_blank(width, height, rgb_color=white)
cv2.imshow("white", image)
cv2.waitKey(0)
