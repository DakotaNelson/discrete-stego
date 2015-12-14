# hamming (7,4)
# able to detect/correct for single-bit error
import sys
import textwrap
import numpy as np

# cut up message to 4 bit sections to encode
def cut(msg):
  # check if divisible by 4, if not add buffer 0s to front
  if len(msg) % 4 != 0:
    left = 4 - (len(msg) % 4)
    msg = left * '0' + msg

  # slice message into 4 bit chunks
  chunks = textwrap.wrap(msg, 4)

  # run hamming for each chunk
  for group in chunks:
    # create list of the values for matrix multiplication
    val = []
    for ch in str(group):
      val.append(int(ch))

    hamming(np.mat(val))

def hamming(sub_msg):
  # create parity bits using transition matrix
  transition = np.mat('0,1,1,1,0,0,0;1,0,1,0,1,0,0;1,1,0,0,0,1,0;1,1,1,0,0,0,1')

  result =  sub_msg * transition
  # convert back to list
  result = list(np.array(result).reshape(-1,))

  # replace 2 with 0
  for i in range(len(result)):
    if result[i] % 2 == 1:
      result[i] = 1
    elif result[i] % 2 == 0:
      result[i] = 0

  print result

def decode(message):
  # organize message into 1-column matrix
  val = []
  for ch in str(message):
    val.append([int(ch)])
  message = np.mat(val)

  # decoding matrix
  transition = np.mat('1,0,0,0,1,1,1;0,1,0,1,0,1,1;0,0,1,1,1,0,1')

  result = transition * message
  print result

if __name__ == '__main__':
  if len(sys.argv) > 1:
    decode(sys.argv[1])
  else:
    input_msg = '1010'
    cut(input_msg)