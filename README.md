Project Title: Color Detection

Introduction
This project is a Python application that allows users to select an image and detect the dominant colors in it. It provides a graphical user interface (GUI) for image selection, displays the detected colors, and allows for pixel-by-pixel RGB value identification. Additionally, the application generates and saves a grayscale version of the selected image and visualizes pixel intensity distribution through histograms and pie charts.

Packages Required:
tkinter - For creating the GUI.
PIL (Python Imaging Library) - For image manipulation.
colorthief - For extracting dominant colors from images.
os - For interacting with the operating system.
numpy - For numerical operations.
opencv (OpenCV) - For image processing.
pandas - For handling CSV files.
matplotlib - For plotting graphs.
argparse - For command-line argument parsing.
Install all packages using the pip command:

bash
Copy code
pip install tkinter pillow colorthief numpy opencv-python pandas matplotlib argparse
Ensure the color.csv file is in the same directory as the main Python program file.

Usage
Run the Python file in either PyCharm or a Python console with the required libraries installed. A graphical user interface will appear upon execution. 

Follow these steps:

Click the "Select Image" button and choose an image from your computer.

Click the "Detect Color" button to display the dominant colors in the corresponding side panel along with their RGB values.

Click the "Info" button to view a pixel intensity distribution histogram and a corresponding pie chart.

After closing the histogram and pie chart, a new window will appear. Click on any part of the image to display the RGB value and color name of the corresponding pixel.

Methodology
GUI Creation: We used the tkinter library to create the graphical user interface.
Image Selection: The filedialog module from tkinter allows users to select an image.
Dominant Color Extraction: The colorthief library extracts dominant colors from the image along with their RGB values.
Pixel Intensity Distribution: Using matplotlib's pyplot, the program plots the pixel intensity distribution in the form of a histogram and pie chart.
Grayscale Image Generation: The program generates a grayscale image of the selected image using OpenCV.
Pixel RGB Value Identification: Using OpenCV and mouse capturing, the program allows users to select a particular pixel and display its RGB value and color name from a predefined CSV file.
