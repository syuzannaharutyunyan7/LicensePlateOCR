import cv2
import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Load the image
img = cv2.imread("images/plate.jpg")

# Run OCR on the full image
results = reader.readtext(img)

# Combine all detected text
plate_text = " ".join([res[1] for res in results])

print("Detected text:", plate_text)

# Optionally, draw boxes around detected text
for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img, text, (top_left[0], top_left[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Show the image
cv2.imshow("License Plate OCR", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
