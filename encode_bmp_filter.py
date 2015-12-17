from scipy import misc
import scipy
import numpy as np
from PIL import Image

inputImg = scipy.misc.imread('hepburn_grayscale.bmp')
message = list('this is a message')
message = ['{:07b}'.format(ord(x)) for x in message]
message = [[bit for bit in x] for x in message]
message = [int(bit) for sublist in message for bit in sublist]
originalMessage = message

bit_counter = 0
for i in range(0, inputImg.shape[0]):
 	for j in range(0, inputImg.shape[1]):
 		#we use the dark pixels to actually encode our data but our filter will brighten the white pixels to make it seem like a desired effect,
 		#not an encoding
 		if inputImg[i][j] > 155 and originalMessage[bit_counter] == 0:	#if pixel is dark enough and we need to encode a 0, set to 255
			inputImg[i][j] = 255
			bit_counter += 1
		elif inputImg[i][j] > 155 and originalMessage[bit_counter] == 1: #if pixel is dark enough and we need to encode a 1, set to 250
			inputImg[i][j] = 250
			bit_counter += 1 
		elif inputImg[i][j] < 100:	#filter will darken the dark pixels and lighten the light pixels
			inputImg[i][j] = 0
		if bit_counter > len(originalMessage)-1:
			bit_counter = 0 #again will encode the message multiple times in the image

y = np.uint8(inputImg)
j = Image.fromarray(y)
j.save('hepburn_encode.bmp')