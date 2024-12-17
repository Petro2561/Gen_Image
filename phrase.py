import io
import replicate
import asyncio
import aiofiles


async def generate_image(prompt: str):
    output = await replicate.async_run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": prompt + "сгенерируй фотореалистично в полный рост",
        },
    )

    image_bytes = io.BytesIO(output[0].read())
    image_bytes.seek(0)
    return image_bytes
