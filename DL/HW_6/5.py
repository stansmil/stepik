import numpy as np


A = np.arange(20).reshape(4, 5)
AA = A.copy()
print(A)

for idx, row in enumerate(AA):
    row[1::2] = -1
    row[::2] **= 3
    row[:] = row[::-1]

print(AA)
print(np.append(A, AA, axis=1))
print(A)
