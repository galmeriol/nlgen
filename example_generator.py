from requests import get
from io import BytesIO
from PIL import Image


image_raw = get('https://cdn.openai.com/research-covers/jukebox/2x-no-mark.jpg', verify=False)
image = Image.open(BytesIO(image_raw.content))
width, height = image.size

print(width, height)