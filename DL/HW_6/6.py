import numpy as np


a = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
el = np.array([], dtype=np.int32)
amount = np.array([], dtype=np.int32)
idx = 0
while idx < a.size:
    c = a[idx]
    el = np.append(el, c)
    next_idx = idx + 1
    while next_idx < a.size and c == a[next_idx]:
        next_idx += 1
    amount = np.append(amount, next_idx - idx)
    idx = next_idx

print(a)
print(el)
print(amount)
