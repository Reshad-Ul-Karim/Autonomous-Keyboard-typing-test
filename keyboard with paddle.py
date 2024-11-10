from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt
from PIL import Image

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Use `use_gpu=False` by default on macOS

# Define the image path
image_path = 'cal1.jpg'

# Perform OCR on the image
result = ocr.ocr(image_path, cls=True)

# Visualize the results
image = Image.open(image_path).convert('RGB')
boxes = [line[0] for line in result[0]]
texts = [line[1][0] for line in result[0]]
scores = [line[1][1] for line in result[0]]
image_with_boxes = draw_ocr(image, boxes, texts, scores)  # Font path is optional

# Display the image
plt.figure(figsize=(10, 10))
plt.imshow(image_with_boxes)
plt.axis('off')
plt.show()
