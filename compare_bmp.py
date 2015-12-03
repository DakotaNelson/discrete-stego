from scipy import misc
import scipy
import numpy as np
from PIL import Image


def compare_images(im1file, im2file):

	im1 = scipy.misc.imread(im1file)
	im2 = scipy.misc.imread(im2file)

	size = im1.shape

	print(size)

	RGBbits = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

	for i in range(0, size[0]):
		for j in range(0, size[1]):
			pixel_diff = im1[i][j]^im2[i][j]
			for k in range(0, size[2]):
				bitstring = '{0:08b}'.format(pixel_diff[k])
				for l in range(0, len(bitstring)):
					if bitstring[l] == '1':
						RGBbits[k][l] += 1


	print("Count of total number of bits flipped in each position for R, G, B")
	print(RGBbits)

	for i in range(0, 3):
		for j in range(0, 8):
			RGBbits[i][j] = (RGBbits[i][j]/(float(size[0]*size[1])))*100

	print("Percentage of red bits flipped in each position")
	print(RGBbits[0])
	print("Percentage of green bits flipped in each position")
	print(RGBbits[1])
	print("Percentage of blue bits flipped in each position")
	print(RGBbits[2])

	return RGBbits

if __name__ == '__main__':
	compare_images('images/hepburn.bmp', 'images/baboon.bmp')

