import cv2
import preprocessing
import edge_detection
import length_estimation
import utils

def main(image_path):
    """
    Main function to execute the blood smear length detection pipeline.
    """
    # Step 1: Preprocess Image
    preprocessed_img = preprocessing.preprocess_image(image_path)
    utils.display_image("Preprocessed Image", preprocessed_img)
    
    # Step 2: Detect Edges
    edges = edge_detection.detect_edges(preprocessed_img)
    utils.display_image("Edge Detection", edges)
    
    # Step 3: Estimate Blood Smear Length
    largest_contour, smear_length = length_estimation.estimate_length(preprocessed_img, edges)
    print(f"Estimated Blood Smear Length: {smear_length} pixels")
    
    # Draw contour and save results
    result_img = preprocessed_img.copy()
    if largest_contour is not None:
        cv2.drawContours(result_img, [largest_contour], -1, (0, 255, 0), 2)
    utils.display_image("Final Detection", result_img)
    utils.save_image(result_img, "output.png")
    
if __name__ == "__main__":
    image_path = "sample_image.jpg"  # Update with the actual image path
    main(image_path)
