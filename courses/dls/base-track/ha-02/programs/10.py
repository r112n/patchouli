import numpy as np

def transform(X, a=1):
    """
    param X: np.array[batch_size, n]
    """
    new_X = np.array(X)
    new_X[:,1::2] = a
    new_X[:,::2] **= 3
    new_X = np.flip(new_X, axis=1)
    return np.concatenate((X, new_X), axis=1)
