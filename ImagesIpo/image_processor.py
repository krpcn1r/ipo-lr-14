from PIL import ImageDraw, ImageFont
from image_handler import ImageHandler

class ImageProcessor:
    def __init__(self, path):
        self.handler = ImageHandler(path)
        self.handler.load()
        self.image = self.handler.get_image().convert("RGB")

        txt = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", 40)
        txt.text((20, 20), "Вариант 2", font=font, fill=(255, 255, 255))

        self.handler.img = self.image
        self.handler.save()

    def bw_filter(self):
        self.image = self.image.convert("L")
        self.handler.img = self.image
        self.handler.save()
