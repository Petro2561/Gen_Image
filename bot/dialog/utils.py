from PIL import Image, ImageStat
import io

async def add_logo_to_image(image_bytes: io.BytesIO) -> io.BytesIO:
    # Открываем сгенерированное изображение
    base_image = Image.open(image_bytes).convert("RGBA")
    
    # Пути к логотипам
    black_logo_path = "./bot/photos/VK Знакомства_black.png"
    white_logo_path = "./bot/photos/VK Знакомства_white.png"
    with Image.open(white_logo_path) as logo:

    # Размер логотипа (25% ширины изображения)
        logo_width = int(base_image.width * 0.25)  # Увеличено до 25%
        logo_height = int(logo.height * (logo_width / logo.width)) # Логотип будет квадратным по пропорциям
    
    # Координаты для нижнего правого угла (отступ 10 пикселей)
        position = (base_image.width - logo_width - 10, base_image.height - logo_height - 10)
        
        # Обрезаем участок изображения для анализа фона
        box = (position[0], position[1], position[0] + logo_width, position[1] + logo_height)
    cropped_area = base_image.crop(box)
    
    # Анализ яркости фона
    stat = ImageStat.Stat(cropped_area)
    brightness = sum(stat.mean) / len(stat.mean)  # Средняя яркость пикселей
    
    # Выбор логотипа в зависимости от яркости фона
    if brightness > 128:
        logo_path = black_logo_path  # Светлый фон -> чёрный логотип
    else:
        logo_path = white_logo_path  # Тёмный фон -> белый логотип
    
    # Открываем выбранный логотип
    new_logo = Image.open(logo_path).convert("RGBA")
    
    # Масштабируем логотип
    logo = new_logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

    # Накладываем логотип на изображение
    base_image.paste(logo, position, logo)

    # Сохраняем результат в новый объект BytesIO
    output_bytes = io.BytesIO()
    base_image.save(output_bytes, format="PNG")
    output_bytes.seek(0)
    return output_bytes

