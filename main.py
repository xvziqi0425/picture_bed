from paddleocr import PaddleOCR

# 创建 OCR 对象
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

# 读取图片
img_path = 'your_image.jpg'
result = ocr.ocr(img_path)

# 打印识别结果
for line in result:
    for word_info in line:
        print(word_info[1][0])

