from PIL import Image

class ImageHandler:
    def __init__(self, path=None):
        self.path = path
        self.img = None

    # Сохранение изображения по указанному пути
    def save(self):
        if self.img and self.path:
            self.img.save(self.path)

    # Загрузка изображения
    def load(self):
        if self.path:
            self.img = Image.open(self.path)
            self.img.load()

    # Обрезка центральной части изображения 
    def change_size(self):
        if not self.img:
            return
            
        width, height = self.img.size
        # Расчет координат для центральной обрезки
        left = (width - 150) // 2
        top = (height - 150) // 2
        right = left + 150
        bottom = top + 150
        
        # Выполнение операции crop и сохранение
        self.img = self.img.crop((left, top, right, bottom))
        self.save()

    # Поворот изображения на 90 градусов 
    def rotate_image(self):
        if not self.img:
            return
            
        self.img = self.img.rotate(90, expand=True)
        self.save()

    # Возврат текущего объекта изображения 
    def get_image(self):
        return self.img
