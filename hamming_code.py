# hamming (7,4)
# able to detect/correct for single-bit error
import sys
import textwrap
import numpy as np

# cut up message to 4 bit sections to encode
def cut(msg, encode):
  # check how to cut message:
  # if encode = 1, cut into 4s
  # if encode = 0, cut into 7s
  if encode == 1:
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

  if encode == 0:
    # slice message into 7 bit chunks
    chunks = textwrap.wrap(msg, 7)

    # run decode for each chunk
    for goup in chunks:
      decode(msg)

def hamming(sub_msg):
  # create parity bits using transition matrix
  transition = np.mat('0,1,1,1,0,0,0;1,0,1,0,1,0,0;1,1,0,0,0,1,0;1,1,1,0,0,0,1')

  result =  sub_msg * transition

  # mod 2 the matrix multiplication
  mod(result)

def decode(msg):
  # organize msg into 1-column matrix
  val = []
  for ch in str(msg):
    val.append([int(ch)])
  msg = np.mat(val)

  # decoding matrix
  transition = np.mat('1,0,0,0,1,1,1;0,1,0,1,0,1,1;0,0,1,1,1,0,1')

  result = transition * msg

  # mod 2 the matrix multiplication
  mod(result)

def mod(msg):
  # reshape matrix to list
  msg = list(np.array(msg).reshape(-1,))

  # mod 2 matrices b/c binary
  for i in range(len(msg)):
    if msg[i] % 2 == 1:
      msg[i] = 1
    elif msg[i] % 2 == 0:
      msg[i] = 0

  print msg

if __name__ == '__main__':
  if len(sys.argv) <= 2:
    print 'Wrong inputs. Example: hamming_code.py 1011 1'
  else:
    cut(str(sys.argv[1]), int(sys.argv[2]))
