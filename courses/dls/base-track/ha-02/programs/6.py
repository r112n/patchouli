import numpy as np

  def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param second: list of "size" lists, each contains "size" floats
    """
    result = list()
    for i in range(len(first)):
        row = list()
        for j in range(len(second[0])):
            elem = 0
            for k in range(len(first[0])):
               elem += first[i][k] * second[k][j]
            row.append(elem)
        result.append(row)

    return result

def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """
    result = np.matmul(first, second)
    return result
