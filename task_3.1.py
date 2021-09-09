
from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 300), (255, 255, 255))
draw = ImageDraw.Draw(im)

draw.ellipse((0, 0, 90, 90), fill='black', outline=(0, 0, 0))

im.show()