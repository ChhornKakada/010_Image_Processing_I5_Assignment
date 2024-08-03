import numpy as np
import random 
# Create a 2D array with shape (3, 4)
shape = (8, 8)
arr = np.zeros(shape)
new_arr = np.zeros(shape)


for x in range(8):
  for y in range(8):
    before = random.randint(0, 256)
    arr[x][y] = before
    after = before + 80
    new_arr[x][y] = 255 if after > 255 else after
    

print(arr)
print(new_arr)