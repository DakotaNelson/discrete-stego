# hamming (7,4)
# able to detect/correct for single-bit error
import sys
import textwrap

# cut up message to 4 bit sections to encode
def cut(msg):
  # check if divisible by 4, if not add buffer 0s to front
  if len(msg) % 4 != 0:
    left = 4 - (len(msg) % 4)
    sub_msg = left * '0' + msg

  # slice message into 4 bit chunks
  chunks = textwrap.wrap(sub_msg, 4)

  # run hamming for each chunk
  for group in chunks:
    hamming(group)

def hamming(sub_msg):
  # create parity bits for (1,2,3) (2,3,4) (1,3,4)
  p1 = parity( ,(0, 1, 2))
  p2 = parity( ,(1, 2, 3))
  p3 = parity( ,(0, 2, 3))

  # need to get 3 parity bits using above, then add them to message
  return sub_msg + p1 + p2 + p3

def parity():
  # apply the matrix for general parity
  pass

# TODO: implement decoding of hamming (reverse process + checking)

if __name__ == '__main__':
  input_msg = '011100000110100101110000'
  cut(input_msg)