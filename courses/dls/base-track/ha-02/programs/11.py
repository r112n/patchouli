import numpy as np
def encode(a):
    arr, cnt = np.array([]), np.array([])

    curr_elem, curr_cnt = a[0], 1
    for i in a[1:]:
        if i == curr_elem:
            curr_cnt += 1
        else:
            cnt, arr = np.append(cnt, curr_cnt), np.append(arr,curr_elem)
            curr_elem, curr_cnt = i, 1
    return np.append(arr, curr_elem), np.append(cnt, curr_cnt)
