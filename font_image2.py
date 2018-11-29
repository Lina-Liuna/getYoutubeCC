import pytesseract
from PIL import Image

# open image
image = Image.open('/Users/lina/Desktop/chi_font.jpeg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)