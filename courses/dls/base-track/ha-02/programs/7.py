import numpy as np
def no_numpy_scalar(v1, v2):
  result = sum(list(map(lambda x,y: x*y, v1, v2)))
  return result

def numpy_scalar(v1, v2):
  return np.dot(v1, v2)
