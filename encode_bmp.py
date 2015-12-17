from scipy import misc
import scipy
import numpy as np
from PIL import Image

inputImg = scipy.misc.imread('baboon_grayscale.bmp')

message = list('this is a message')
message = ['{:07b}'.format(ord(x)) for x in message]
message = [[bit for bit in x] for x in message]
message = [int(bit) for sublist in message for bit in sublist]
originalMessage = message #list of 1s and 0s to encode in the baboon image
print originalMessage

bit_counter = 0 #will keep track of which bit we are on
for i in range(0, inputImg.shape[0]):
	for j in range(0, inputImg.shape[1]):
		while inputImg[i][j] % 2 != originalMessage[bit_counter]:	#check if the pixel value mod 2 encodes the bit we need it to encode
			inputImg[i][j] += 1 #if it doesn't, increase bit value until it does, should at most run once
			if inputImg[i][j] > 255:	#correct just in case in incremented we accidentally overstep 255
				inputImg[i][j] = 255
		bit_counter+=1 #increment the bit counter to get the next bit
		if bit_counter > len(originalMessage)-1: #reset so we are encoding 'this is a message' in the entire image
			bit_counter = 0


y = np.uint8(inputImg)
j = Image.fromarray(y)
j.save('baboon_encoded.bmp')