import cv2
import numpy as np

def estimate_length(image, edges):
    """
    Extracts the largest contour and estimates the length of the blood smear.
    """
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None, 0
    
    # Find the largest contour (assuming it's the smear)
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Compute bounding box dimensions
    x, y, w, h = cv2.boundingRect(largest_contour)
    smear_length = max(w, h)  # Choose the larger dimension as the length
    
    return largest_contour, smear_length
