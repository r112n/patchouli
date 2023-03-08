import numpy as np

def diag_2k(a):
  diag = np.diagonal(a)
  result = diag[diag % 2 == 0].sum() 
  return result
