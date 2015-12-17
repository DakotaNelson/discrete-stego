from scipy import misc
import scipy
import numpy as np
from PIL import Image

x = scipy.misc.imread('hepburn.bmp')
y = np.empty([x.shape[0], x.shape[1]], dtype=np.int)

def weightedAverage(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]	#returns the grayscale value of each pixel using weighted RGB channels

for i in range(0, x.shape[0]):
 	for j in range(0, x.shape[0]):
 		 y[i][j] = int(weightedAverage(x[i][j])) #rounds to int

y = np.uint8(y)
j = Image.fromarray(y)
j.save("hepburn_grayscale.bmp")