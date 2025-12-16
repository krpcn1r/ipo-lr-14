from image_processor import ImageProcessor

path = input("Введите путь к изображению: ")
processor = ImageProcessor(path)
processor.bw_filter()
