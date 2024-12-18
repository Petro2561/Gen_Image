from PIL import Image, ImageStat
import io

async def add_logo_to_image(image_bytes: io.BytesIO) -> io.BytesIO:
    base_image = Image.open(image_bytes).convert("RGBA")
    logo_path = "./bot/photos/VK Знакомства.png"
    with Image.open(logo_path) as logo:
        logo_width = int(base_image.width * 0.10)
        logo_height = int(logo.height * (logo_width / logo.width))
        position = (base_image.width - logo_width - 10, base_image.height - logo_height - 10)        
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        base_image.paste(logo, position, logo)
    output_bytes = io.BytesIO()
    base_image.save(output_bytes, format="PNG")
    output_bytes.seek(0)
    return output_bytes

