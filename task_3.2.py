
from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 300), (255, 255, 255))
draw = ImageDraw.Draw(im)

draw.ellipse((100, 100, 150, 200), fill='blue', outline=(0, 0, 0))

im.show()