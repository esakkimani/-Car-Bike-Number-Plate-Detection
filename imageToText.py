import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\Administrator\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open("C:\\Users\\Administrator\\PycharmProjects\\pythonProject5\\photo.jpg")
text = tess.image_to_string(img)
print(text)
