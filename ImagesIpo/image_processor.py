from PIL import ImageDraw, ImageFont
from image_handler import ImageHandler

class ImageProcessor:
    def __init__(self, path):
        # Инициализация обработчика и загрузка изображения
        self.handler = ImageHandler(path)
        self.handler.load()
        # Конвертация в формат RGB для корректной работы с цветом и текстом
        self.image = self.handler.get_image().convert("RGB")

        txt = ImageDraw.Draw(self.image)
        # Загрузка шрифта Arial
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except OSError:
            # Использование стандартного шрифта, если arial.ttf не найден
            font = ImageFont.load_default()

        # Нанесение водняго знака "Вариант 2" в левом верхнем углу
        txt.text((20, 20), "Вариант 2", font=font, fill=(255, 255, 255))

        # Обновление изображения в обработчике и сохранение изменений
        self.handler.img = self.image
        self.handler.save()

    # Применение черно-белого фильтра к изображению.
    def bw_filter(self):
        # Конвертация изображения в режим "L" (градации серого)
        self.image = self.image.convert("L")
        self.handler.img = self.image
        self.handler.save()
