from PIL import Image

class ImageHandler:
    def __init__(self, path=None):
        self.path = path
        self.img = None

    def save(self):
        if self.img and self.path:
            self.img.save(self.path)

    def load(self):
        self.img = Image.open(self.path)
        self.img.load()

    def change_size(self):
        width, height = self.img.size
        left = (width - 150) // 2
        top = (height - 150) // 2
        right = left + 150
        bottom = top + 150
        self.img = self.img.crop((left, top, right, bottom))
        self.save()

    def rotate_image(self):
        self.img = self.img.rotate(90, expand=True)
        self.save()

    def get_image(self):
        return self.img
