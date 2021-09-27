# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')
n = map(float, raw_input().split())

arr=np.array(n)

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
