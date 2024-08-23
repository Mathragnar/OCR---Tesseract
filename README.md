Real-Time OCR with Tesseract and OpenCV

This Python script utilizes Tesseract OCR and OpenCV to perform real-time text recognition from a video stream (webcam). The script specifically searches for a pattern matching three letters followed by a digit, then another letter and finally two digits (e.g., ABC1D12).

Functionality:

Capture Video Stream: Captures video from the default webcam (index 0).

Convert to Grayscale: Converts each frame to grayscale for improved OCR accuracy.

Perform OCR: Uses Pytesseract to perform OCR on the grayscale frame, extracting text.

Pattern Matching: Searches for the specified pattern using regular expressions ([A-Za-z]{3}\d[A-Za-z]\d{2}).

Display Result: Prints the matched pattern to the console, avoiding duplicate prints.

Optional Display: Displays the video feed in a window (optional, can be commented out).

Exit Condition: Allows the user to exit by pressing the 'q' key.

Prerequisites:

Python: Installed and configured.

OpenCV (cv2): Install using pip install opencv-python.

Pytesseract: Install using pip install pytesseract.

Tesseract OCR Engine: Download and install from https://tesseract-ocr.github.io/tessdoc/Downloads.html. Make sure to add the Tesseract installation directory to your system's PATH environment variable.

Configuration:

pytesseract.pytesseract.tesseract_cmd: Update this path to point to the correct location of the Tesseract executable on your system.

Usage:

Save the script as a Python file (e.g., ocr_script.py).

Run the script from the command line: python ocr_script.py.

Note:

The script uses the default webcam (index 0). If you have multiple webcams, adjust the video_capture index accordingly.

The pattern matching can be customized by modifying the regular expression.

The video display is optional and can be commented out if not needed.

Example Output:

Captura: ABC1D12
content_copy
Use code with caution.

Disclaimer:

This script is provided as a basic example and may require adjustments depending on your specific needs and environment.
