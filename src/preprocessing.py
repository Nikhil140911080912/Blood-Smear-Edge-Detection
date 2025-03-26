import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Load and preprocess the image.
    Converts BGR to HSV, applies Gaussian Blur, CLAHE, and Bilateral filter.
    """
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Error loading image. Check the file path.")
    
    # Convert to HSV for better segmentation
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(hsv, (5, 5), 0)
    
    # Apply CLAHE to enhance contrast
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    enhanced_lab = cv2.merge((cl, a, b))
    enhanced_img = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    
    # Apply Bilateral Filter for edge preservation
    filtered = cv2.bilateralFilter(enhanced_img, 9, 75, 75)
    
    return filtered
