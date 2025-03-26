import cv2
import numpy as np

def detect_edges(image):
    """
    Apply Canny Edge Detection and morphological operations to extract blood smear contours.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 50, 150)
    
    # Apply morphological operations to refine edges
    kernel = np.ones((5, 5), np.uint8)
    edges_dilated = cv2.dilate(edges, kernel, iterations=1)
    edges_closed = cv2.morphologyEx(edges_dilated, cv2.MORPH_CLOSE, kernel)
    
    return edges_closed
