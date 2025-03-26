import cv2
import matplotlib.pyplot as plt

def load_image(image_path):
    """Loads an image from the given path."""
    return cv2.imread(image_path)

def display_image(title, image):
    """Displays an image using Matplotlib."""
    plt.figure(figsize=(6, 6))
    plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

def save_image(image, filename):
    """Saves the processed image."""
    cv2.imwrite(filename, image)
