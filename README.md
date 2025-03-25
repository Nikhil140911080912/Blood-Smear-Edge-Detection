Overview

This project aims to determine the length of a blood smear from a microscopic image using image processing techniques. The approach includes edge detection, contour analysis, and color-based segmentation.

How It Works

Preprocessing:

Convert image from BGR to HSV for better color segmentation.

Apply Gaussian Blur and CLAHE (Contrast Limited Adaptive Histogram Equalization) for noise reduction.

Use a bilateral filter to enhance edges while maintaining smoothness.

Edge & Contour Detection:

Detect fine edges using Canny Edge Detection.

Extract the blood smear contour using thresholding & morphological operations.

Combine results from multiple detection methods for accurate segmentation.

Length Estimation:

Identify the upper and lower edges of the blood smear.

Calculate the vertical distance to determine smear length.
