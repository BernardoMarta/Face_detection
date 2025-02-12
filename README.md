# Face Detection Project

## About the Project

This project implements a Python script that detects faces in images using the OpenCV library. It utilizes a pre-trained Haar Cascade classifier to identify faces, draws rectangles around the detected faces, and calculates user accuracy by comparing detected faces with a user-provided count.

## How It Works

1.  The script prompts the user to input the path to an image.
2.  It loads the image using OpenCV.
3.  It converts the image to grayscale for better face detection performance.
4.  It uses the Haar Cascade classifier to detect faces in the grayscale image.
5.  It draws rectangles around each detected face.
6.  It displays the image with the face detections.
7.  It prompts the user to manually count the number of faces they see in the image.
8.  It calculates an accuracy score by comparing the detected faces with the user count.
9.  It prints the number of faces detected and the accuracy score.

## Getting Started

### Prerequisites

-   Python 3.x
-   OpenCV library (cv2)

pip install opencv-python

### Installation

1.  Clone the repository:

git clone https://github.com/BernardoMarta/Face_detection
cd Face_detection

## Usage

1.  Run the script from the command line:

python face_detection.py

2.  The script will prompt you to insert the path of the image you want to analyze.

3.  Follow the prompts. The script will display the image with detected faces (if any) and ask you to enter the number of faces you manually counted in the image.

## Example

**Input:**

python face_detection.py
Insert the path of the image you want to analyze: image.jpg

(The script will then display the image in a new window.)

How many faces do you see in the image? 3

**Example Output:**

Number of faces detected: 2
Accuracy score: 66.67%


## Notes

-   The accuracy score relies on both the performance of the face detection algorithm and the user's manual count.
-   Ensure that the path to the image is correct and that the image file exists at that location.

## Features

-   Detects faces in images using OpenCV and Haar Cascade classifiers.
-   Draws rectangles around detected faces in the image.
-   Calculates an accuracy score based on the user's manual face count.
-   Allows the user to specify the image file path.
-   Provides feedback on the number of faces detected and the accuracy score.

## Contributing

Feel free to fork this repository and submit pull requests to [BernardoMarta's repository](https://github.com/BernardoMarta/Face_detection)!

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to OpenCV for providing the libraries and Haar Cascade classifiers used in this project.
