import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original Array:")
print(arr)

arr[:, [0, 1]] = arr[:, [1, 0]]

print("\nArray after swapping columns 1 and 2:")
print(arr)