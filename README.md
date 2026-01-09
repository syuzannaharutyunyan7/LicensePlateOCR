# License Plate OCR

A simple Python project to read text from license plate images using **EasyOCR** and **OpenCV**.

## Features
- Detects text from license plates.
- Prints the detected text.
- Draws boxes around text on the image.

## Requirements
- Python 3  
- OpenCV  
- EasyOCR  

Install dependencies:

```bash
pip install opencv-python easyocr
````

## How to Use

1. Put your image in the `images/` folder (or change the path in the script).
2. Run the script:

```bash
python main.py
```

3. See the detected text in the console and the image with highlighted text.

## Notes

* Works best on clear license plate images.
* Currently set to English (`['en']`) in EasyOCR.

```
