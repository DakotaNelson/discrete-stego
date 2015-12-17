from scipy import misc
import scipy
import numpy as np
from PIL import Image

encode = 'this is a message'
message = list(encode)
message = ['{:07b}'.format(ord(x)) for x in message]
message = [[bit for bit in x] for x in message]
message = [int(bit) for sublist in message for bit in sublist]
originalMessage = message #used to catch errors

count_err = 0 #counts the number of errors

test = scipy.misc.imread('baboon_encoded.bmp')

bit_counter = 0
bitstring = [] #will hold the decoded bit values
for i in range(0, test.shape[0]):
	for j in range(0, test.shape[1]):
		if test[i][j]%2 != originalMessage[bit_counter]: #so we have an error
			count_err += 1
		bitstring.append(test[i][j]%2)	#add pixel value mod 2 to the list
		bit_counter+=1
		if bit_counter > len(originalMessage)-1:
			bit_counter = 0


temp = "" #7 bits encode a character so store them in a temp string
outputMessage = [] #list that will hold the characters
for i in range(0, len(bitstring)):	
	temp += str(bitstring[i])
	if len(temp) == 7: #if we have enough bits for a character
		temp = chr(int(temp, 2)) #convert string to int and then from there to character using ASCII
		outputMessage.append(temp)
		temp = "" #clear temp for the next 7 bits

res = ""
for i in range(0, len(outputMessage)):	#take the list of characters and assemble it as a string
	res += outputMessage[i]

print "The expected message we should receive is: " + encode
print "The number of errors in the received message is: " + str(count_err)
print "The received message is: " + res[0:len(encode)]