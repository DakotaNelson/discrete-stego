import numpy as np
from PIL import Image

def get_histogram(im):
  im = Image.open(im)
  im = im.convert("RGB")
  (width, height) = im.size
  
  # get and store pixel values for each
  colors = {}
  for color in im.getdata():
    colors[color] = colors.get(color, 0) + 1

  pixels = []
  for i in range(width - 1):
    for j in range(height - 1):
      pixels.append(im.getpixel((i, j)))
  print pixels

if __name__ == '__main__':
  get_histogram('images/original/image.jpg')