from image_processor import ImageProcessor

# Запрос пути к файлу у пользователя
path = input("Введите путь к изображению: ")

# Инициализация процессора изображений
processor = ImageProcessor(path)

# Применение черно-белого фильтра
processor.bw_filter()
