# Image Redaction Project

## Overview
This project contains Python scripts that automate the process of redacting sensitive information from images of PAN and Aadhar cards. The scripts use Optical Character Recognition (OCR) to detect and blur out the PAN or Aadhar numbers to protect personal information.

## Features
- **OCR Integration**: The scripts utilize `easyocr` to extract text from images.
- **Regex Matching**: Specific patterns for PAN and Aadhar numbers are identified using regular expressions.
- **Automatic Redaction**: Detected sensitive information is automatically blurred out in the images.
- **Image Display**: The redacted images are displayed using OpenCV.

## Requirements
- Python 3.x
- Libraries:
  - `numpy`
  - `cv2` (OpenCV)
  - `matplotlib`
  - `easyocr`

## Installation

 Install the required Python libraries:
    ```bash
    pip install numpy opencv-python matplotlib easyocr
    ```

## Usage
1. Place the image files (e.g., PAN card, Aadhar card) in the project directory.
2. Update the script with the correct image file name:
    - For PAN card: update `image = cv2.imread("pancard2.jpg")` with your image filename.
    - For Aadhar card: update `image = cv2.imread("aadhar2.jpg")` with your image filename.
3. Run the script:
    ```bash
    python blur_pan_number.py  # For PAN card redaction
    python blur_aadhar_number.py  # For Aadhar card redaction
    ```
4. The redacted image will be displayed with the sensitive information blurred.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

