from PIL import Image
import pytesseract



def read_content(image):
    # image = Image.open('English.png')
    content = pytesseract.image_to_string(image)  # 解析图片
    print(content)
