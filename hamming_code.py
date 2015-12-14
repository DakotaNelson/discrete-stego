# hamming (7,4)
# able to detect/correct for single-bit error
import sys
import textwrap

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
    hamming(group.split())

def hamming(sub_msg):
  # create parity bits using transition matrix
  transition = [[0,1,1,1,0,0,0],
                [1,0,1,0,1,0,0],
                [1,1,0,0,0,1,0],
                [1,1,1,0,0,0,1]]
  pass
  
  # need to get 3 parity bits using above, then add them to message
  # print sub_msg + p1 + p2 + p3
  # return sub_msg + p1 + p2 + p3

def parity(sub_msg, indices):
  # apply the matrix for general parity
# TODO: implement proper parity with matrices
  pass

# TODO: implement decoding of hamming (reverse process + checking)

if __name__ == '__main__':
  input_msg = '1010'
  cut(input_msg)