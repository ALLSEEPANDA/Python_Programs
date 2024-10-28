import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

array[array % 2 != 0] = -1

print("Modified array:")
print(array)